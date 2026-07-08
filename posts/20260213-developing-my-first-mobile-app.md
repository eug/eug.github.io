---
title: Developing my first mobile app
subtitle: Lessons, mistakes, and wins from shipping my first app
tags: [mobile, app-development, learning, product]
created_at: 2026-02-13
---

Building my first mobile app, **Ordr**, has been one of the most challenging (and fun) projects I’ve done—and as I write this, it’s under review on both the Apple App Store and Google Play.

This is a write-up of how I’m hacking my way through it: what I believed going in, what I copied, what I built, and what surprised me.

## 1) The constraint: I only build in proven markets

My personal rule: I don’t try to invent a new category on my first app. I want a market where:

- people are already searching for solutions,
- people already pay (or at least understand the “pay for productivity” pitch),
- I can market by comparison (“like X, but with less friction”).

The downside is obvious: churn is real. People bounce between apps constantly. But that’s also the opportunity—if you solve a sharp pain, you can keep capturing new users.

## 2) The market: productivity apps (because demand never stops)

After some research, I landed on a productivity app. Not because it’s “blue ocean”, but because demand is continuous—and honestly because a lot of apps looked interchangeable.

The pain I kept coming back to: many task apps create *task administration*. Instead of brain-dumping and doing the next thing, you end up:

- labeling,
- setting dates,
- marking urgent,
- moving tasks between “today” and “tomorrow”,
- reorganizing lists endlessly.

And if you don’t nail that flow, a lot of people just go back to pen and paper.

## 3) The bet: “brain dump in, structure out”

I wanted an app that feels less like “manage your tasks” and more like “talk to a helpful organizer”.

The simple version of the idea:

- you type/speak a messy brain dump,
- the app proposes structured tasks/lists/dates/priority,
- you approve/adjust,
- repeat until it looks right. (Longer-term, I want it to learn your preferences so you have to correct it less.)

One concrete example: the “daily planner” use case.

Most people don’t want to do the nightly ritual of dragging tasks from “today” to “tomorrow”. They want to wake up and ask: “What do I have today?” Then negotiate: “Not in the morning”, “push this three days”, “I can only do quick wins”, etc.

I also wanted the app to accept more than plain text. The current MVP takes:

- plain text,
- links,
- YouTube videos,
- and images,

so the system can extract tasks without you manually copying notes into a todo item. Link/video/image extraction is in the current version; “learn my preferences over time” is not (yet).

One practical example: recipes.

Say you find a recipe on a website and you want a shopping list. Or you have a meal plan in a notes app and you just want “everything I need to buy this week”. Today I’d normally copy/paste ingredients, miss half of them, then re-check the page in the grocery store.

With this approach, you can drop in the recipe link, send screenshots, or even share a YouTube video you watched. The app turns that into a clean list (ingredients grouped, quantities preserved when possible) and, if you want, a checklist of steps you can follow while cooking.

## 4) What I copied: teardown of the top apps

Before building anything, I did the most honest thing you can do as a beginner: I copied patterns.

I picked the top ~10 downloaded apps in the App Store and looked at:

- logos,
- screenshots,
- onboarding,
- paywalls,
- core loop,
- feature checklist,
- and how they describe value.

A few observations:

- **Logos**: minimal, usually a checkmark-ish shape, light colors.
- **Screenshots**: extremely polished, “award-winning UI” energy.
- **Onboarding**: top downloaded apps often do longer onboarding; it felt correlated with revenue (not because longer is better, but because it signals “we understand your workflow”).
- **Core loop**: basically the same everywhere: create tasks → reminders → organize → repeat.
- **Keywords**: I spent time hunting for popular keywords that looked both relevant and rankable. “AI daily planner / AI personal assistant” kept popping up as a sweet spot, and it matched the direction I was already heading.

## 5) Naming + branding (a surprisingly non-trivial time sink)

I started without a name, then used a generic working title (“smart todo”), then renamed mid-stream to **ordr** (as in: putting life in order).

The logo idea came from origami: fold a rectangular strip of paper and you get a checkmark shape. Done.

## 6) MVP scope: 3 features (plus 2 “oops I added it” features)

The first three core features I scoped:

1. **Input capture**: dump anything in; the system proposes adds/deletes/renames/completions; show a diff for the user to approve.
2. **Task sort**: instead of sorting by date/alphabetical, the user provides criteria (“impact”, “effort”, “dependencies”), and the system sorts accordingly.
3. **Task breakdown**: turn a scary task into smaller actionable steps, because “I don’t know where to start” is the real blocker.

Then I noticed some apps use **flashcards** instead of lists to reduce the anxiety of “choosing the right task”. That felt more engaging, so I added it. I also added a **timer / distraction blocker** flow. One future idea I want to link to the flashcards is a “feeling lucky” mode that just picks a task for you so you can start immediately.

## 7) Stack choices (aka: speed over purity)

I optimized for “ship something real”:

- **Flutter**: cross-platform from a single codebase (I had zero Dart experience).
- **Supabase**: auth + database + edge functions, because I wanted fewer moving parts.
- **RevenueCat**: centralized subscription/payment plumbing.
- **PostHog**: analytics to understand what people actually do.
- **Gemini**: the model behind the “organize my brain dump” flows.
- **Coding assistants**: Claude Code, Codex, Kimi CLI (rotating when I hit daily limits).

## 8) What surprised me (the unsexy parts)

- **App store mechanics**: configurations and “store-specific weirdness”. Conceptually similar across stores, but the dev experience is different enough that it slowed me down.
- **Screenshots**: multiple experienced devs told me to spend ~a week here. I get why—after studying competitor screenshots, the bar is high. For a first version (with missing features and evolving UX), it felt risky to over-invest… but you still need something decent. I spent ~3 days and produced 8 screenshots. Not perfect, but clear enough to communicate benefits.
- **Payments were simpler than I expected**: I assumed subscriptions would be a minefield, but the integration path felt pretty straightforward. I’m still not 100% confident the current implementation is correct until real transactions go through, but it was less scary than I imagined.
- **Push notifications are more centralized than I realized**: I had no idea how much of it is “talk to Apple/Google’s systems” rather than bespoke infrastructure. Flutter also smooths over a lot of the platform-specific glue here.

If you’re building your first mobile app (or have shipped a dozen), I’d love feedback—especially on the “AI organizer” flow and how to keep it from turning into *more* task admin.

For the next few weeks, my focus is simple: fix bugs based on early feedback, tighten the UX, and start running a few growth experiments to see what actually moves the needle.

The part I’m happiest about right now is less visible: I finally have a workflow I can reuse—research → teardown → build → ship—so the next app should start from a much better place than this first one did.
