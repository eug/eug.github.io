# Euge's Blog

This is a simple vibe-coding friendly static blog generator written in Python.

## How it Works

The blog uses a Python script (`main.py`) to generate static HTML files from Markdown posts.
- Posts are stored in the `posts/` directory as Markdown files.
- Templates for the HTML pages are located in the `templates/` directory.
- The static HTML files are generated in the `dist/` directory.
- Static assets (CSS, JS, images) are served from the `static/` directory.
- Configuration for the blog (like site title) is in `config.json`.

## Managing Blog Posts

### Creating a New Post

1.  Create a new Markdown file (e.g., `my-new-post.md`) in the `posts/` directory.
2.  Add frontmatter to the beginning of the Markdown file. The frontmatter should include at least `title` and `date`. For example:
    ```markdown
    ---
    title: My New Awesome Post
    date: 2023-10-27
    ---

    This is the content of my new post.
    ```
3.  Write your blog post content using Markdown.

### Updating a Post

1.  Open the Markdown file for the post you want to update in the `posts/` directory.
2.  Make your changes to the frontmatter or content.
3.  Save the file.

### Deleting a Post

1.  Delete the Markdown file for the post you want to remove from the `posts/` directory.

## Generating the Static Blog

To generate a new static version of the blog:

1.  Ensure you have Python installed and the required dependencies. You can install dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the `main.py` script from the root of the project:
    ```bash
    python main.py
    ```
3.  The generated static files will be available in the `dist/` directory. You can then deploy these files to any static web hosting service.

## Configuration

Blog settings like the site title can be modified in the `config.json` file.
After changing the configuration, regenerate the blog for the changes to take effect.

## Project Structure

The blog is composed of the following main components:

-   **`main.py`**: The core Python script responsible for:
    -   Parsing Markdown files from the `posts/` directory.
    -   Loading HTML templates from the `templates/` directory.
    -   Generating static HTML pages for posts, the index page, and an about page into the `dist/` directory.
    -   Handling blog configuration from `config.json`.
    -   Generating sitemap (`sitemap.xml`), `robots.txt`, RSS/Atom feeds (`rss.xml`, `atom.xml`), and LLM-specific text files (`llms.txt`, `llms-ctx-full.txt`).
    -   Copying static assets (CSS, JS, images) from `static/` to `dist/static/`.
-   **`posts/`**: This directory contains your blog posts written in Markdown format.
    -   Each `.md` file represents a single blog post.
    -   Frontmatter (metadata like title, date, tags) is included at the top of each Markdown file.
    -   An `about.md` file can be placed here to generate the content for the "About" page.
-   **`templates/`**: This directory holds the Jinja2 HTML templates used to structure the generated pages:
    -   `index.html`: Template for the main blog page listing all posts.
    -   `post.html`: Template for individual blog post pages.
    -   `about.html`: Template for the "About" page.
    -   `atom.xml` / `rss.xml`: Templates for generating syndication feeds.
-   **`dist/`**: This is where the generated static website is stored. The contents of this directory can be deployed to any static web hosting service.
    -   `dist/posts/`: Contains the generated HTML files for individual posts.
    -   `dist/static/`: Contains copied static assets.
-   **`static/`**: This directory is for your static assets like CSS stylesheets, JavaScript files, and images. These files are copied directly to the `dist/static/` directory during generation.
-   **`config.json`**: A JSON file for configuring blog-wide settings such as the site title, site URL, blog description, author email, and syndication preferences.
-   **`requirements.txt`**: Lists the Python dependencies required to run the blog generator (e.g., Markdown, Jinja2).

## Extending the Blog

The blog's functionality can be extended by modifying the `main.py` script and/or the templates. Here are some common ways to extend it:

### Adding New Page Types

1.  **Create a new template**: If you want a new type of page (e.g., a "Projects" page), create a new HTML template in the `templates/` directory (e.g., `projects.html`).
2.  **Add data source (optional)**: If this new page needs to display dynamic content (like a list of projects), decide how this data will be provided. It could be from a new directory of Markdown files, a JSON file, or directly within `main.py`.
3.  **Modify `main.py`**:
    -   Add logic to parse any new data sources.
    -   Add a new function or modify the `main()` function to render your new template with the necessary context.
    -   Ensure the generated page is saved to the `dist/` directory.

### Customizing Existing Pages

1.  **Modify templates**: To change the layout or appearance of existing pages (index, post, about), edit the corresponding HTML files in the `templates/` directory. You can add new HTML elements, change styling (by modifying `static/style.css` or adding new CSS), or alter how data is displayed.
2.  **Adjust `main.py`**: If you need to pass new data to the templates:
    -   Modify the data parsing functions (e.g., `parse_markdown_file`) if the new data comes from post frontmatter.
    -   Update the context dictionary passed to the `render_template` function for the relevant page(s).

### Adding New Data to Posts

1.  **Update frontmatter**: Add new fields to the frontmatter of your Markdown posts in the `posts/` directory.
2.  **Modify `parse_markdown_file` in `main.py`**: Ensure the new frontmatter fields are correctly parsed and processed. You might need to handle data type conversions or default values.
3.  **Update `post.html` template**: Modify the `post.html` template (or other relevant templates) to display this new data.

### Changing Static Asset Handling

-   To add new CSS, JavaScript, or images, place them in the `static/` directory. They will be automatically copied to `dist/static/`.
-   Link to new CSS or JS files in your HTML templates as needed (e.g., in the `<head>` section or before the closing `</body>` tag).

### Modifying Generation Logic

-   The `main()` function in `main.py` orchestrates the entire generation process. You can modify this function to change the order of operations, add new steps, or remove existing ones.
-   Helper functions like `generate_sitemap`, `generate_robots_txt`, `generate_syndication`, and `generate_llmstxt` can be customized to alter the content or format of these generated files.

Remember to regenerate the blog by running `python main.py` after making any changes to see them reflected in the `dist/` directory.

## Deployment
This site is automatically deployed to GitHub Pages using GitHub Actions. The site is built and deployed to the `gh-pages` branch. 