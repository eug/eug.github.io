---
title: Engineerification
subtitle: Why more professions are becoming engineer-shaped just as engineering itself may be automated
tags: [ai, work, engineering, systems-thinking, agents, mathematics]
created_at: 2026-08-23
---

> **TL;DR:** I have been noticing professionals in very different fields adopting workflows that look increasingly like engineering: repositories, agents, tests, automation, formal specifications, and feedback loops. The deeper change is not that everyone is learning to code. It is that domain experts are becoming responsible for systems that perform parts of their work. I have been calling this **engineerification**. I do not know whether it is desirable, or even durable. The strange possibility is that many of us may become engineer-like just before agents become capable of doing much of the engineering too.

I recently watched a lecture for mathematicians that spent a surprising amount of time on the terminal.

The speakers recommended working in local directories, giving coding agents carefully limited permissions, keeping projects in repositories, committing changes, writing instruction files, running tests, and using Lean to check formal proofs. They demonstrated Claude Code and Codex, discussed which models were better for long sessions, and explained why a mathematician might move work out of Overleaf and onto a local machine.

This was not a software engineering conference. It was a [special lecture on LLMs and mathematics](https://www.youtube.com/watch?v=2hkXQKCh1cE) at Brazil's Institute for Pure and Applied Mathematics.

The practical advice was concrete enough to feel ordinary. A mathematician described starting the day by entering a project directory and launching an agent. Another described numerical experiments that once required learning an unfamiliar programming language and can now be assembled by asking a model for subroutines, testing them, and using the results to develop intuition.

Something about this caught my attention.

Mathematicians have used computers for a long time. Numerical methods, symbolic systems, LaTeX, and proof assistants are not new. But this looked like more than adopting another tool. The shape of the work was changing. A mathematical project was becoming a software project: a collection of files with dependencies, permissions, executable checks, version history, and an agent operating inside it.

After that lecture, I started noticing the same shape elsewhere.

## A profession changing shape

The other talks I had been watching were less instructional and more existential.

In [*The Last Generation of Mathematicians*](https://www.youtube.com/watch?v=6uIJdXmB4vE), Jacob Tsimerman distinguishes concern for mathematics from concern for mathematicians. Mathematics may continue to expand even if the familiar working life of a mathematician does not. He imagines a period in which people solve problems partly by directing language models, while remaining careful about forecasting what comes after it.

In his [ICM 2026 public lecture](https://www.youtube.com/watch?v=M0--ZH1lOzg), Terence Tao approaches the disruption through the values of mathematical practice. Producing a valid argument is not the whole activity. Results must also be verified, explained, digested, connected to existing knowledge, and judged interesting enough to pursue. A machine may accelerate some of these stages without settling what the community should value in the others.

The three lectures seemed to describe different layers of the same transition.

One showed a profession reconsidering its purpose. Another showed anxiety about its identity. The practical lecture showed what people do on Monday morning: open a terminal, navigate to a repository, start an agent, inspect its changes, and decide whether the result can be trusted.

That last layer may be the most revealing. Large changes in work often arrive first as small changes in routine.

## More than learning to code

I have been calling this pattern **engineerification**.

The word is intentionally a little awkward. I do not mean that every mathematician, designer, analyst, or lawyer is becoming a software engineer. I also do not mean that engineering owns systems thinking, or that other professions lacked rigor before Git appeared.

What seems to be spreading is a particular responsibility: domain experts are increasingly expected to create, supervise, and improve systems that perform parts of their domain work.

The important shift is not from natural language to programming language. An agent may hide most of the code. The shift is from doing a task to shaping a process that repeatedly does the task.

That requires a different kind of attention. What information enters the system? Which dependencies does it rely on? How does it behave when the input is strange? What can it modify? How do we know whether its output is correct? How can a change be reviewed, reversed, or reproduced? Who is responsible when a locally reasonable result causes a wider failure?

These are engineering-shaped questions even when the underlying subject is mathematics, design, sales, science, or law.

The code may be generated. The need to reason about boundaries, feedback, failure, and consequences remains.

## Software engineers went first

I had seen an earlier version of this shift inside software development itself.

The first coding assistants mostly completed the code in front of you. By 2024, the unit of delegation was becoming much larger: give a model an issue, let it explore a repository, review its plan, and judge the changes through tests.

[GitHub Copilot Workspace](https://github.blog/news-insights/product-news/github-copilot-workspace/), announced in April 2024, made this explicit. It turned a task into an editable specification, plan, implementation, and test cycle. GitHub described the developer as a “systems thinker”: someone stating intent, constraining the solution, and validating what happened.

Research prototypes followed the same direction. [SWE-agent](https://arxiv.org/abs/2405.15793) asked agents to solve GitHub issues across real repositories. [SWT-Bench](https://arxiv.org/abs/2406.12952) translated issues into tests that could check generated code. Aider's [Architect/Editor workflow](https://aider.chat/2024/09/26/architect.html) separated reasoning about a solution from making the edits.

In GitHub's [2024 survey of 2,000 enterprise workers on software development teams](https://github.blog/news-insights/research/survey-ai-wave-grows/), most respondents said their organizations used AI-generated test cases at least sometimes. They also reported spending some of the time saved on collaboration, learning, and system design.

This does not prove that most engineers had reorganized their work around agents. The survey was self-reported, and product announcements describe aspirations as much as established practice. But 2024 looks like a visible hinge: autocomplete was giving way to delegation, with tests, specifications, and architecture becoming the interface between the engineer and the implementation.

Engineerification may have happened inside engineering first. As programming became more delegable, engineers moved toward designing and supervising the system that produced the code. Other domains may now be repeating that movement.

## The same motion elsewhere

The most explicit example may be go-to-market work. In the manual version described by [Clay's guide to GTM engineering](https://www.clay.com/guides/gtm-engineering), a representative researches accounts across many tabs, exports and cleans lists, qualifies leads, and prepares outreach one record at a time. A GTM engineer tries to turn that motion into a system: signals enter, records are enriched and scored, actions are routed, results are measured, and the workflow is revised. The unit of work moves from the account to the mechanism that processes accounts.

Analytics went through a related transition earlier. Analysts who once produced queries and dashboards now increasingly maintain transformation pipelines as versioned software. The role called [analytics engineering](https://www.getdbt.com/blog/what-is-analytics-engineering) brought modularity, documentation, testing, deployment, and code review into work that still depends on understanding the business meaning of the data.

Design is moving across the old handoff boundary too. At Vercel, [design engineers](https://vercel.com/blog/design-engineering-at-vercel) may sketch in Figma or code, build reusable components, inspect browser performance, handle accessibility, and ship the result. Anthropic describes product designers using Claude Code to implement visual and state changes directly, replacing some cycles of specification and translation with [working prototypes and code changes](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code).

The pattern extends beyond product companies. Research software engineering treats scripts that might once have been disposable by-products as durable scientific infrastructure, bringing version control, continuous integration, testing, and documentation into research. Legal teams are experimenting with agents to build routing and review tools around their own processes. Technical writers practice [docs as code](https://www.writethedocs.org/guide/docs-as-code/), working through Markdown, issues, pull requests, reviews, and automated checks. Compliance rules that once lived only in documents can become [policy as code](https://www.openpolicyagent.org/docs/philosophy), versioned and evaluated automatically inside a system.

These examples are not equally mature, and some come from vendors with an interest in presenting their tools as transformative. I do not think they prove that every profession is moving in one direction. Many people in these fields will never open a terminal, nor should they need to.

But the recurrence seems meaningful. Artifacts become repositories. Procedures become workflows. Rules become tests. Repeated tasks become systems. The professional moves one level up, from producing each output to defining and supervising the conditions under which outputs are produced.

## When everything becomes a system

There is an optimistic interpretation of this.

People closest to a problem can finally change the machinery around it. A mathematician can test a numerical intuition without waiting for a programmer. A designer can explore the real interaction instead of describing it through a static mockup. A lawyer can prototype a routing tool without competing for a place on an engineering roadmap. Domain knowledge can become executable without crossing as many translation layers.

This may make systems thinking a general form of literacy. Not everyone needs to understand every generated line, but more people can inspect inputs and outputs, identify dependencies, make constraints explicit, and build feedback into their own work.

There is also a less comfortable interpretation.

Engineering is powerful partly because it makes parts of the world formal enough to operate on. Inputs need schemas. Success needs signals. Rules need expressions. Failures need categories. Once a workflow becomes a system, the system begins to privilege what it can represent.

That is useful when the omitted detail is noise. It is dangerous when the omitted detail contains the point.

A mathematical proof can be formally correct and still fail to communicate why an idea matters. A sales system can optimize replies while damaging relationships it cannot measure. A legal workflow can route known categories efficiently while missing the unusual case that required judgment. A scientific pipeline can be reproducible and still encode a bad assumption. A design system can make interfaces consistent while making them consistently wrong for someone it did not model.

Engineerification therefore does not merely give a profession new tools. It imports an engineering temptation: to treat what has not been formalized as if it were outside the system, and then to forget that the system is smaller than the world.

Tao's distinction between generating mathematics and digesting it feels relevant here. Verification can tell us that an argument satisfies formal rules. It cannot by itself decide whether the argument created understanding, whether it is worth teaching, or what new questions it should make us ask. Those judgments are not defects waiting to be compiled away. They are part of the practice.

The engineering mindset is most valuable when it includes stewardship rather than only optimization: knowing that a system has boundaries, looking for what falls outside them, and remaining answerable for the consequences.

## The temporary engineer

There is a paradox in the timing of all this.

AI is reducing the amount of implementation skill required to build a working system. That should make engineering less central. Instead, at least for now, it appears to be distributing engineering responsibilities across more professions.

When building becomes cheap, more things become buildable. When more things become systems, more people must decide how those systems should behave. The implementation may arrive through a prompt, but somebody still has to shape the environment, choose the evidence, define the checks, inspect failures, and recognize when the machinery has misunderstood the work.

In [*From Gatekeepers to Plumbers?*](https://eug.github.io/posts/from-gatekeepers-to-plumbers.html), I wondered whether engineers might move from approving every change to building the infrastructure that lets domain experts act safely. Engineerification looks like the corresponding movement from the other side. Domain experts gain the ability to act, but they also inherit responsibility for the systems through which they act.

I do not know whether this arrangement lasts.

The same agents that make engineering workflows accessible are becoming better at navigating repositories, running tests, tracing dependencies, responding to failures, and improving their own instructions. If systems stewardship can be described as a loop, agents may take over more of that loop too.

Perhaps engineerification names a stable future in which systems thinking becomes part of almost every profession. Perhaps it names a brief period in which humans learn to supervise machinery that soon requires much less supervision. Or perhaps the work keeps moving upward: from writing outputs, to building systems, to choosing purposes and accepting responsibility for what the systems do.

I am not sure which of these futures is desirable. Making domain experts more capable seems good. Turning every profession into a collection of pipelines, metrics, and evaluators does not obviously seem good. Removing tedious implementation seems good. Losing the forms of understanding that tedious work sometimes produced may not be.

For now, the pattern is easier to see than its destination.

Are we all becoming engineers because engineering is the future of knowledge work, or because it is the temporary interface between our professions and the systems that may eventually perform them?
