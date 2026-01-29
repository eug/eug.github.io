import os
import markdown
from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import shutil
import json # Added for loading config
import re # Added for parsing JavaScript bookmarks
import html

POSTS_DIR = "posts"
TEMPLATES_DIR = "templates"
OUTPUT_DIR = "dist"
STATIC_DIR = "static"
CONFIG_FILE = "config.json" # Added for config file path


def parse_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Configure markdown with better codehilite settings
    md = markdown.Markdown(extensions=[
        "meta", 
        "fenced_code", 
        "codehilite"
    ], extension_configs={
        'codehilite': {
            'css_class': 'codehilite',
            'use_pygments': True,
            'noclasses': False,
            'guess_lang': True
        }
    })
    html_content = md.convert(content)
    metadata = md.Meta

    # Convert metadata values to appropriate types
    if 'created_at' in metadata:
        try:
            # Ensure created_at is treated as a single value, not a list for parsing
            date_str_to_parse = metadata['created_at'][0] if isinstance(metadata['created_at'], list) else metadata['created_at']
            metadata['created_at'] = datetime.strptime(date_str_to_parse, '%Y-%m-%d')
        except (ValueError, TypeError):
             metadata['created_at'] = datetime.min # Fallback
             print(f"Warning: Could not parse date for {file_path}. Using default.")
    else:
        metadata['created_at'] = datetime.min # Ensure created_at always exists
        print(f"Warning: 'created_at' metadata missing in {file_path}. Using default.")


    if 'tags' in metadata and isinstance(metadata['tags'], list) and len(metadata['tags']) > 0:
        tags_string = metadata['tags'][0]
        if tags_string.startswith('[') and tags_string.endswith(']'):
            tags_string = tags_string[1:-1]
        metadata['tags'] = [tag.strip() for tag in tags_string.split(',') if tag.strip()]
    elif 'tags' in metadata and isinstance(metadata['tags'], str): # Handle case where tags might be a single string
        tags_string = metadata['tags']
        if tags_string.startswith('[') and tags_string.endswith(']'):
            tags_string = tags_string[1:-1]
        metadata['tags'] = [tag.strip() for tag in tags_string.split(',') if tag.strip()]
    else:
        metadata['tags'] = []


    return {
        "html_content": html_content,
        "raw_markdown": content,
        "metadata": {k: v[0] if isinstance(v, list) and len(v) == 1 and k != 'tags' else v for k, v in metadata.items()}
    }

def render_template(template_name, context, env):
    template = env.get_template(template_name)
    return template.render(context)

def load_config():
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
            
        # Validate theme configuration
        valid_themes = ["light", "dark"]
        theme = config.get("theme", "dark")
        if theme not in valid_themes:
            print(f"Warning: Invalid theme '{theme}' in config.json. Using 'dark' as default.")
            config["theme"] = "dark"
            
        return config
    except FileNotFoundError:
        print(f"Error: {CONFIG_FILE} not found. Please create it.")
        return {"theme": "dark"}  # Add default theme
    except json.JSONDecodeError:
        print(f"Error: Could not decode {CONFIG_FILE}. Check its format.")
        return {"theme": "dark"}  # Add default theme

def generate_sitemap(posts, config):
    site_url = config.get("site_url", "")
    if not site_url:
        print("Warning: 'site_url' not found in config.json. Sitemap URLs will be relative.")

    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Add home page
    sitemap_content += '  <url>\n'
    sitemap_content += f'    <loc>{site_url}/</loc>\n'
    sitemap_content += f'    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>\n' # Or a more specific date for home
    sitemap_content += '    <changefreq>weekly</changefreq>\n'
    sitemap_content += '    <priority>1.0</priority>\n'
    sitemap_content += '  </url>\n'

    # Add posts
    for post in posts:
        post_path = f"posts/{post['slug']}.html"
        post_url = f"{site_url}/{post_path}"
        # Try to get modification date from metadata, fallback to now
        last_mod_dt = post["metadata"].get("updated_at") or post["metadata"].get("created_at")
        last_mod_str = last_mod_dt.strftime("%Y-%m-%d") if isinstance(last_mod_dt, datetime) else datetime.now().strftime("%Y-%m-%d")

        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{post_url}</loc>\n'
        sitemap_content += f'    <lastmod>{last_mod_str}</lastmod>\n'
        sitemap_content += '    <changefreq>monthly</changefreq>\n'
        sitemap_content += '    <priority>0.8</priority>\n'
        sitemap_content += '  </url>\n'
    
    sitemap_content += '</urlset>'

    sitemap_dir = os.path.join(OUTPUT_DIR, "sitemap")
    os.makedirs(sitemap_dir, exist_ok=True)
    sitemap_path = os.path.join(sitemap_dir, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"Sitemap generated at {sitemap_path}")

def generate_robots_txt(config):
    site_url = config.get("site_url", "")
    if not site_url:
        print("Warning: 'site_url' not found in config.json. Robots.txt sitemap URL may be incomplete.")

    robots_content = "User-agent: *\n"
    robots_content += "Allow: /\n\n"
    robots_content += f"Sitemap: {site_url}/sitemap/sitemap.xml\n"

    robots_txt_path = os.path.join(OUTPUT_DIR, "robots.txt")
    with open(robots_txt_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"robots.txt generated at {robots_txt_path}")

def generate_syndication(posts, config, env):
    """Generates RSS and/or Atom feeds based on the syndication config."""
    syndication_option = config.get("syndication", "both").lower()
    site_url = config.get("site_url", "http://localhost:8000")
    site_title = config.get("blog_name", "My Blog")
    site_description = config.get("blog_description", "My awesome blog")
    current_year = datetime.now().year # Added to ensure it's available

    if syndication_option in ["atom", "both"]:
        atom_feed_posts_processed = []
        for p_original in posts: # Iterate over the original posts list
            p_for_atom = p_original.copy() # Create a shallow copy of the post dictionary
            full_html_content = p_for_atom.get("html_content", "") # Get original HTML content
            p_for_atom["html_content"] = full_html_content[:50] # Truncate to first 50 characters
            atom_feed_posts_processed.append(p_for_atom)

        atom_xml = render_template("atom.xml", {
            "posts": atom_feed_posts_processed, # Use the list with truncated content
            "site_url": site_url,
            "site_title": site_title,
            "config": config
        }, env)
        atom_path = os.path.join(OUTPUT_DIR, "atom.xml")
        with open(atom_path, "w", encoding="utf-8") as f:
            f.write(atom_xml)
        print(f"Atom feed generated at {atom_path}")

    if syndication_option in ["rss", "both"]:
        rss_xml = render_template("rss.xml", {
            "posts": posts,
            "site_url": site_url,
            "site_title": site_title,
            "site_description": site_description,
            "current_year": current_year # Added current_year
        }, env)
        rss_path = os.path.join(OUTPUT_DIR, "rss.xml")
        with open(rss_path, "w", encoding="utf-8") as f:
            f.write(rss_xml)
        print(f"RSS feed generated at {rss_path}")

def generate_llms_posts_full(posts, config):
    """Generate llms-posts-full.txt containing the full markdown content of all posts."""
    llms_ctx_full_content_parts = []

    for post in posts:
        # Use the raw_markdown from post_data
        if "raw_markdown" in post:
            llms_ctx_full_content_parts.append(post["raw_markdown"])
        else:
            # Fallback if raw_markdown is somehow missing
            post_slug = post.get("slug", "unknown")
            print(f"Warning: raw_markdown not found for post {post_slug}. Skipping for llms-posts-full.txt.")

    # Generate llms-posts-full.txt content
    llms_posts_full_content = "\n___\n".join(llms_ctx_full_content_parts)
    llms_posts_full_txt_path = os.path.join(OUTPUT_DIR, "llms-posts-full.txt")
    
    with open(llms_posts_full_txt_path, "w", encoding="utf-8") as f:
        f.write(llms_posts_full_content)
    
    print(f"llms-posts-full.txt generated at {llms_posts_full_txt_path} with {len(llms_ctx_full_content_parts)} posts")

def generate_llms_bookmarks_full(config):
    """Generate llms-bookmarks-full.txt by parsing bookmarks from bookmarks.html template."""
    bookmarks_template_path = os.path.join(TEMPLATES_DIR, "bookmarks.html")
    
    if not os.path.exists(bookmarks_template_path):
        print(f"Warning: {bookmarks_template_path} not found. Skipping llms-bookmarks-full.txt generation.")
        return
    
    try:
        with open(bookmarks_template_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract the bookmarks array from the JavaScript
        # Look for the pattern: const bookmarks = [
        pattern = r'const bookmarks = \[(.*?)\];'
        match = re.search(pattern, content, re.DOTALL)
        
        if not match:
            print("Warning: Could not find bookmarks array in bookmarks.html. Skipping llms-bookmarks-full.txt generation.")
            return
        
        bookmarks_js = match.group(1)
        
        # Parse individual bookmark objects
        # Look for pattern: { url: "...", title: "..."}
        # Handle escaped quotes in titles using proper regex
        bookmark_pattern = r'\{\s*url:\s*"((?:[^"\\]|\\.)*)"\s*,\s*title:\s*"((?:[^"\\]|\\.)*)"\s*\}'
        bookmark_matches = re.findall(bookmark_pattern, bookmarks_js)
        
        if not bookmark_matches:
            print("Warning: Could not parse bookmark objects from bookmarks.html. Skipping llms-bookmarks-full.txt generation.")
            return

        total_items = 0     
        bookmarks_markdown_content = ""
        for url, title in bookmark_matches:
            # Unescape quotes in the title (convert \" back to ")
            title_unescaped = title.replace('\\"', '"')
            # Escape any problematic characters in title for markdown
            title_escaped = title_unescaped.replace("]", "\\]").replace("[", "\\[")
            if title_escaped:
                bookmarks_markdown_content += f"- [{title_escaped}]({url})\n"
                total_items += 1
        
        # Generate markdown content
        markdown_content = f"# Bookmarks\n\n"
        markdown_content += f"A collection of {total_items} bookmarks from the blog.\n\n"
        markdown_content += bookmarks_markdown_content

        # Write to file
        llms_bookmarks_full_path = os.path.join(OUTPUT_DIR, "llms-bookmarks-full.txt")
        with open(llms_bookmarks_full_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        print(f"llms-bookmarks-full.txt generated at {llms_bookmarks_full_path} with {total_items} bookmarks")
        
    except Exception as e:
        print(f"Error generating llms-bookmarks-full.txt: {e}")

def generate_llmstxt(posts, config, about_content_md):
    # llms.txt content
    blog_name = config.get("blog_name", "My Blog")
    blog_description = config.get("blog_description", "My awesome blog")
    author_email = config.get("author_email", "your_email@example.com")
    site_url = config.get("site_url", "").rstrip('/')

    llms_txt_content = f"# {blog_name}\n\n"
    llms_txt_content += f"{blog_description}\n\n"
    llms_txt_content += f"Author Email: {author_email}\n"
    llms_txt_content += f"Site URL: {site_url}\n\n"

    # Add About section
    llms_txt_content += "## About\n\n"
    if about_content_md and about_content_md.strip():
        llms_txt_content += f"{about_content_md.strip()}\n\n"
    # else: # If about_content_md is empty or whitespace, just leave a blank line or two already added

    llms_txt_content += "## Bookmarks\n\n"
    llms_txt_content += f"For full bookmarks context please visit [llms-bookmarks-full.txt]({site_url}/llms-bookmarks-full.txt)\n\n"

    llms_txt_content += "## Posts\n\n"
    llms_txt_content += f"For full posts context please visit [llms-posts-full.txt]({site_url}/llms-posts-full.txt)\n\n"

    for post in posts:
        post_title = post["metadata"].get("title", "Untitled Post")
        post_subtitle = post["metadata"].get("subtitle", "")
        post_slug = post["slug"]
        post_url = f"{site_url}/posts/{post_slug}.html"
        
        llms_txt_content += f"[{post_title}]({post_url})"
        if post_subtitle:
            llms_txt_content += f": {post_subtitle}\n"
        else:
            llms_txt_content += "\n"

    llms_txt_path = os.path.join(OUTPUT_DIR, "llms.txt")
    with open(llms_txt_path, "w", encoding="utf-8") as f:
        f.write(llms_txt_content)
    print(f"llms.txt generated at {llms_txt_path}")

def create_template_context(config, **kwargs):
    """Create a common template context with theme and other shared variables."""
    theme = config.get("theme", "dark")
    
    # Determine CSS paths based on context (post pages vs main pages)
    is_post_page = 'post' in kwargs
    css_base_path = "../static/css/" if is_post_page else "static/css/"
    
    meta_description = kwargs.pop("meta_description", "").strip()
    if not meta_description:
        meta_description = config.get("blog_description", "My awesome blog")

    context = {
        "config": config,
        "theme": theme,
        "site_title": config.get("blog_name", "My Blog"),
        "author_email": config.get("author_email", "your_email@example.com"),
        "site_url": config.get("site_url", ""),
        "current_year": datetime.now().year,
        "static_base_css_path": f"{css_base_path}base.css",
        "static_theme_css_path": f"{css_base_path}{theme}.css",
        "meta_description": meta_description,
    }
    context.update(kwargs)
    return context

def build_meta_description(text, fallback, max_length=160):
    if not text:
        return fallback
    # Strip HTML tags and collapse whitespace.
    stripped = re.sub(r"<[^>]+>", " ", text)
    stripped = html.unescape(stripped)
    stripped = re.sub(r"\s+", " ", stripped).strip()
    if not stripped:
        return fallback
    return stripped[:max_length].rstrip()


def main():
    # Load configuration
    config = load_config()

    # Create output directory if it doesn't exist
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)
    os.makedirs(os.path.join(OUTPUT_DIR, "posts"), exist_ok=True)

    # Create .nojekyll file to prevent GitHub Pages from processing with Jekyll
    with open(os.path.join(OUTPUT_DIR, ".nojekyll"), "w") as f:
        pass  # Create an empty file

    # Setup Jinja2 environment
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    # Parse posts
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            file_path = os.path.join(POSTS_DIR, filename)
            post_data = parse_markdown_file(file_path)
            post_data["slug"] = filename.replace(".md", "")
            posts.append(post_data)
    
    # Sort posts by date (newest first)
    posts.sort(key=lambda p: p["metadata"].get("created_at", datetime.min), reverse=True)

    # Generate post pages
    for post in posts:
        meta_description = build_meta_description(
            post["metadata"].get("subtitle") or post.get("html_content", ""),
            config.get("blog_description", "My awesome blog"),
        )
        context = create_template_context(config,
            post=post,
            static_rss_path="../rss.xml",
            static_atom_path="../atom.xml",
            meta_description=meta_description
        )
        post_html = render_template("post.html", context, env)
        output_path = os.path.join(OUTPUT_DIR, "posts", f"{post['slug']}.html")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(post_html)

    # Generate index page
    index_description = build_meta_description(
        config.get("blog_description", "My awesome blog"),
        config.get("blog_description", "My awesome blog"),
    )
    context = create_template_context(config,
        posts=posts,
        static_rss_path="rss.xml",
        static_atom_path="atom.xml",
        meta_description=index_description
    )
    index_html = render_template("index.html", context, env)
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    # Generate about page
    about_content = "" # Placeholder if about.md doesn't exist
    about_metadata = {} 
    if os.path.exists(os.path.join(POSTS_DIR, "about.md")):
        about_data = parse_markdown_file(os.path.join(POSTS_DIR, "about.md"))
        about_content = about_data["html_content"]
        about_metadata = about_data["metadata"]
    
    about_page_title = about_metadata.get("title", config.get("blog_name", "My Blog"))
    about_description = build_meta_description(
        about_content,
        config.get("blog_description", "My awesome blog"),
    )
    context = create_template_context(config,
        page_title=about_page_title,
        content=about_content,
        static_rss_path="rss.xml",
        static_atom_path="atom.xml",
        meta_description=about_description
    )
    about_html = render_template("about.html", context, env)
    with open(os.path.join(OUTPUT_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(about_html)

    # Generate bookmarks page
    bookmarks_description = build_meta_description(
        "Bookmarks curated from the blog.",
        config.get("blog_description", "My awesome blog"),
    )
    context = create_template_context(config,
        static_rss_path="rss.xml",
        static_atom_path="atom.xml",
        meta_description=bookmarks_description
    )
    bookmarks_html = render_template("bookmarks.html", context, env)
    with open(os.path.join(OUTPUT_DIR, "bookmarks.html"), "w", encoding="utf-8") as f:
        f.write(bookmarks_html)

    # Generate syndication feeds (RSS and/or Atom)
    generate_syndication(posts, config, env)

    # Generate sitemap
    generate_sitemap(posts, config)

    # Generate robots.txt
    generate_robots_txt(config)

    # Prepare About content for llms.txt
    about_section_content = "" 
    about_md_path = os.path.join(POSTS_DIR, "about.md")
    if os.path.exists(about_md_path):
        about_data = parse_markdown_file(about_md_path)
        about_section_content = about_data.get("raw_markdown", "").strip()
        if not about_section_content:
            print(f"Info: about.md found but raw_markdown content is empty or only whitespace. 'About' section in llms.txt will reflect this.")
    else:
        try:
            about_html_template_path = os.path.join(TEMPLATES_DIR, "about.html")
            with open(about_html_template_path, "r", encoding="utf-8") as f:
                html_lines_for_about = []
                in_content_block = False
                for line in f:
                    stripped_line = line.strip()
                    if "{% block content %}" in stripped_line:
                        in_content_block = True
                        continue
                    if "{% endblock %}" in stripped_line and in_content_block:
                        # Ensure we break after processing the block, not before processing the endblock line if content is on it
                        in_content_block = False # Mark as out of block
                        break 
                    if in_content_block:
                        # Basic HTML to plain text conversion
                        processed_line = stripped_line.replace("<h2>", "").replace("</h2>", "")
                        processed_line = processed_line.replace("<h3>", "").replace("</h3>", "")
                        processed_line = processed_line.replace("<h4>", "").replace("</h4>", "")
                        processed_line = processed_line.replace("<p>", "").replace("</p>", "")
                        # Remove any other common HTML tags if necessary, e.g., <strong>, <em>
                        processed_line = processed_line.replace("<strong>", "").replace("</strong>", "")
                        processed_line = processed_line.replace("<em>", "").replace("</em>", "")
                        if processed_line:
                            html_lines_for_about.append(processed_line)
            about_section_content = "\n".join(html_lines_for_about).strip()
            if not about_section_content:
                print(f"Info: Parsed templates/about.html but found no text content for 'About' section in llms.txt.")
        except FileNotFoundError:
            print(f"Warning: {about_html_template_path} not found (and about.md does not exist). 'About' section will be empty in llms.txt.")
        except Exception as e:
            print(f"Error reading or parsing {about_html_template_path}: {e}. 'About' section will be empty in llms.txt")


    # Generate LLMS.txt files
    generate_llmstxt(posts, config, about_section_content)

    # Generate llms-posts-full.txt
    generate_llms_posts_full(posts, config)

    # Generate llms-bookmarks-full.txt
    generate_llms_bookmarks_full(config)

    # Copy static files
    if os.path.exists(STATIC_DIR):
        output_static_dir = os.path.join(OUTPUT_DIR, STATIC_DIR) # Define the output/static directory
        os.makedirs(output_static_dir, exist_ok=True) # Create it

        for item in os.listdir(STATIC_DIR):
            s = os.path.join(STATIC_DIR, item)
            d = os.path.join(output_static_dir, item) # Copy items to output/static/
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
                # Also place verification files at the site root (e.g., Google Search Console).
                if item.startswith("google") and item.endswith(".html"):
                    shutil.copy2(s, os.path.join(OUTPUT_DIR, item))

    print("Static site generated successfully!")

if __name__ == "__main__":
    main() 
