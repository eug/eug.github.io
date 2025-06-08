---
title: My bookmarks are public now
subtitle: Rethinking bookmarks for the next decade
tags: [vibe-code, ssg, python, bookmark]
created_at: 2025-06-01
---

So, [Pocket's shutting down](https://getpocket.com/farewell). Cue the minor existential crisis for a 10-year power user like myself. Over a thousand articles saved – a digital trail of my internet rabbit holes and "aha!" moments. The announcement hit, and it wasn't just about losing a service; it was about realizing how much of that curated knowledge was locked away, just for me. And the big question: migrate to another silo, or... something else?

I chose "something else."

The thought of another decade of private bookmarking, another walled garden of links, just didn't sit right. Why store up all this good stuff? Why not make it a public, evolving resource? And even better, why not let others chip in?

That's the new plan: **Public, collaborative, and interactive bookmarks.**

Here are the details on how I'm pulling this off:

**Public**

First, liberation. I grabbed my Pocket data (shoutout to them for a clean CSV export). Then came the data-janitor phase (it took me several hours to finish it): I did some cleaning, replaced old links with updated ones, pruned the dead links, and removed articles that were well past their sell-by date. This newly-curated treasure trove of links is now living on a plain HTML [bookmarks.html](https://eug.github.io/bookmarks.html) page on my site. Simple and effective.

**Collaborative**

Now, for the collaborative bit – this is where it gets fun (and very GitHub-y). I've added an "Add Bookmark" button. Clicking it doesn't pop up a sleek modal or hit a fancy API. Nope. It throws you straight into the GitHub editor for that [templates/bookmarks.html](https://github.com/eug/eug.github.io/edit/main/templates/bookmarks.html#L14) file.

The idea is beautifully simple:

1.  I/You find a cool link.
2.  I/You click "Add Bookmark."
3.  I/You paste the URL and title into the HTML (minimal formatting needed, I'll tidy it up).
4.  I/You submit a Pull Request.
5.  I review, merge, and boom – my/your contribution is live for everyone.

Is it as slick as Pocket's one-click save? Nah. The beauty is in its transparency and the "good enough" approach. I can quickly paste a link myself without fuss, knowing I'll circle back to format it properly later during a review.

**Interactive**

But just *having* them public is one thing. How about making them truly *interactive*? That's where things get even cooler. I've started playing around with feeding this whole heap of bookmarks into Google's NotebookLM. What's the upshot? Well, it means anyone can now 'chat' with my bookmarks – ask questions, dig for specific topics, or even spot broader themes, all without manually combing through hundreds of links.  You can jump in and query my bookmark collection directly here: [Google NotebookLM](https://notebooklm.google.com/notebook/65911a6f-ce1b-4604-bb7d-178aa88f67ea?original_referer=https%3A%2F%2Fwww.google.com%23&pli=1).

---

This isn't just about replacing a tool; it's an experiment in open knowledge sharing. Will anyone else contribute or interact? Maybe, maybe not. But the door's open. And either way, my digital breadcrumbs are now out in the open, hopefully leading others to some of the awesome corners of the web I've stumbled upon.

Let's see what the next decade of *open* bookmarking brings.
