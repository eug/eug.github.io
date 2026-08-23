---
title: Soft Software Needs Hard Factories
subtitle: As interfaces become fluid and code becomes disposable, the machinery underneath may need to become much more rigid
tags: [software-engineering, ai, agents, generative-ui, software-factories, human-computer-interaction]
created_at: 2026-08-23
---

> **TL;DR:** Cheap code generation seems to be pulling software in two opposite directions. At the surface, software is becoming more personal, temporary, and malleable. Underneath, producing it reliably requires specifications, harnesses, tests, and increasingly automated factories. I suspect these are not competing futures. The soft edge may only be possible because of a hard core.

Software has always had a slightly misleading name.

It is “soft” compared with hardware because changing instructions is easier than rebuilding a machine. But most software does not feel soft to the person using it. It arrives as a finished application with a fixed interface and a menu of decisions its creators anticipated. If the workflow does not fit, the user adapts—or submits feedback and waits.

In practice, software has been editable for its producers and rigid for everyone else.

The [Ink & Switch essay on malleable software](https://www.inkandswitch.com/essay/malleable-software/) argues for reversing this: software that people can reshape at the point of use, with a gentle slope from user to creator. Not just more settings, but tools that can be adjusted, combined, and gradually rewritten around local needs.

This is an old dream in computing. What feels different now is that producing a new behavior has become cheap enough that the dream no longer depends entirely on teaching everyone to program.

A user can describe the change instead.

That sounds like a small substitution—natural language for code—but I think it may alter what we consider the software itself.

## The interface for this moment

Most applications are built around predictions. A product team predicts which tasks matter, which controls people need, and how those controls should be arranged. The result is compiled into an interface and distributed to everyone.

Generative interfaces weaken that sequence.

[Google's work on generative UI](https://research.google/blog/generative-ui-a-rich-custom-visual-interactive-user-experience-for-any-prompt/) describes models generating complete interactive experiences in response to a prompt: visual explanations, simulations, tools, and small applications assembled for the question at hand. Projects such as [CopilotKit's generative UI examples](https://github.com/CopilotKit/generative-ui) show a more constrained version of the same direction, where an agent emits declarative UI that a host application can safely render.

The distinction matters. One approach can generate almost any interface; the other generates within a known component system. But both suggest that the interface is no longer necessarily a durable artifact designed before the user arrives. It can be a temporary interpretation of intent.

The same idea is appearing in developer tools. [Pi](https://pi.dev/) describes itself as a minimal coding-agent harness that should adapt to your workflow, rather than asking your workflow to adapt to it. If Pi lacks a command, tool, or interface tweak, you can ask it to modify itself, reload, and continue.

This is more than customization as we normally understand it. Settings let a user choose among decisions the developer already made. Plugins expose specific surfaces the developer prepared. A self-modifying tool or generated interface moves part of development into the act of use.

The boundary starts to blur:

- Using the tool reveals the need.
- Describing the need changes the tool.
- The changed tool becomes the new way of working.

Software begins to resemble a workspace that can be rearranged while work is happening.

I find this genuinely exciting. A physician should not need to wait for a national product roadmap to remove three pointless fields from a local workflow. A researcher should be able to turn the same dataset into the interface required by today's question. A developer should be able to shape an agent around a project without waiting for the vendor to ship a feature.

But there is a less visible requirement hidden inside this flexibility. If software can vary for every person and every moment, the number of versions we need to trust increases dramatically.

Malleability at the edge creates a verification problem at the core.

## When the code stops being the asset

For most of software history, code was expensive to create. We treated it as a durable asset partly because replacing it was costly. Teams accumulated frameworks, abstractions, and products around the assumption that implementation effort was scarce.

Cheap generation changes the economics.

Chris Loy calls this [the rise of industrial software](https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software/): software production moving from craft toward manufacture, including a new class of disposable artifacts that may be created, used, shared, and abandoned at enormous scale. The comparison is uncomfortable because industrial abundance does not produce only good things. It also produces fast fashion, junk food, and objects designed to be replaced rather than understood or repaired.

Still, “disposable” is not necessarily an insult. A small program written for a single analysis might deserve to disappear after answering the question. A generated interface may be valuable precisely because nobody has to maintain it for ten years. The mistake may be assuming that every useful piece of software should become a product.

If code can be regenerated cheaply, its value starts to move elsewhere: into the intent that shaped it, the data it operates on, the constraints it must respect, and the process that can produce another correct version.

This is the premise behind the emerging [software factory](https://www.mager.co/blog/2026-03-19-software-factory/): not merely an agent that writes code, but a system that receives a specification, coordinates work, executes it, verifies the result, deploys it, and learns from feedback.

The factory, rather than any individual output, becomes the durable artifact.

That creates a strange symmetry. At one end, a user asks for an interface that may exist for five minutes. At the other, an increasingly permanent machine turns intent into working software. The visible layer becomes softer because the production layer becomes harder.

Or at least, that seems to be the direction. Most of us have the cheap generation already. The hard production layer is much less complete.

## Climbing the abstraction ladder on credit

Over the past few years, the industry has moved through a sequence of attempts to steer generated code.

First we improved prompts. Then we gave agents tools, repositories, and terminals. Now the vocabulary is shifting toward specifications, plans, context engineering, harnesses, evaluators, and loops. Each step moves attention away from typing the implementation and toward shaping the conditions under which an implementation can emerge.

[Kiro's spec-driven development](https://kiro.dev/blog/introducing-kiro/) is one example. A request becomes explicit requirements, a technical design, and sequenced tasks before it becomes code. The specification is not only documentation for humans; it is an input surface for the agent and an artifact against which the result can be inspected.

The [advanced context engineering](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md) work from HumanLayer goes further into the development loop. It argues for making architecture and program design concrete before implementation: data flows, contracts, call-stack shapes, file-tree changes, types, and vertical slices that can be exercised as the system grows. The interesting part is not that these techniques are new. It is that cheap implementation makes the decisions around implementation more visible as the scarce work.

This is what I mean by climbing the abstraction ladder. Instead of directly arranging statements, we arrange requirements, constraints, tools, context, and feedback. The agent operates on the level below.

But we may be climbing on credit.

Many codebases do not have reliable tests, explicit invariants, clean interfaces, reproducible environments, or fast feedback. They were built for humans who could notice ambiguity, ask a colleague, and use experience to decide whether a passing test really meant the change was safe. Giving these systems a much faster implementation engine does not automatically give them a better steering system.

We have raised the level of instruction before strengthening the foundation that interprets it.

## The velocity has to go somewhere

[The velocity paradox](https://www.abahgat.com/blog/the-velocity-paradox/) describes what happens when generation outruns verification. An agent may collapse the inner loop of writing code, but if it cannot deterministically check its work, the loop closes through a human. The agent produces faster; the person reviews more. The promised multiplier turns into a queue.

I suspect this is the central constraint on both malleable software and software factories.

If every generated variation needs careful manual inspection, software cannot really become fluid. It can only create review work at fluid speed. A dark factory is not autonomous because no humans are visible. It is autonomous only to the extent that consequences can feed back into production without requiring a person to reconstruct the entire situation each time.

That makes tests and evaluators more than quality practices. They become part of the production medium. So do permissions, schemas, sandboxes, observability, provenance, rollback, and boundaries on what may be generated at all.

This hard core does not need to eliminate uncertainty. It probably cannot. But it needs to turn enough outcomes into signals that the system can correct itself, while knowing when the remaining uncertainty requires judgment.

The better this machinery becomes, the more variation the edge can tolerate. A browser can render arbitrary pages because the platform defines strong boundaries. A database can support countless applications because its contracts are relatively stable. Perhaps generative software will follow the same pattern: open-ended behavior above a small set of heavily defended invariants.

The edge can improvise because the core rehearses.

## When the factory turns inward

The far end of this trajectory is not a factory that only produces applications. It is a factory that improves the machinery doing the production.

Anthropic's essay on [recursive self-improvement](https://www.anthropic.com/institute/recursive-self-improvement) describes a progression from models helping write snippets, to agents running longer experiments, to systems that may eventually contribute to building their own successors. The important step is closing the loop: the output of the system changes the system that produces the next output.

There are many reasons to be cautious about extrapolating from today's coding agents to full recursive improvement. Humans still choose most goals, construct evaluations, provide infrastructure, and decide what counts as progress. A loop is not autonomous simply because an agent executes several iterations inside it.

Even so, the direction sharpens the same question. The more the production system can modify itself, the less we can rely on inspecting each generated artifact after the fact. We need durable constraints around the process: what it may optimize, which evidence it trusts, how changes are evaluated, who can stop it, and which parts it cannot rewrite.

The hard core must remain hard even when the factory works on itself.

## A soft edge and a hard core

I do not think fixed applications are about to disappear. Many tasks benefit from a stable interface shared by millions of people. Predictability, accessibility, security, and support are easier when everyone is using roughly the same thing. Nor do I think every implementation will become disposable. Infrastructure with long-lived state and real-world obligations resists casual regeneration.

But the pattern across these experiments seems meaningful to me.

At the surface, software is becoming less like a finished object and more like a response: an interface for this question, a tool shaped around this workflow, a small program created for this moment. Underneath, the durable value moves into specifications, data, component systems, agent harnesses, verification, and feedback loops.

This is not quite the end of software engineering. It may be a redistribution of it.

Some engineering moves upward into deciding what should happen and how success can be recognized. Some moves downward into building the platforms and constraints that make variation safe. The middle—the manual production of each implementation—becomes thinner.

I am still unsure how far this model goes. A hard core can protect users, but it can also concentrate control in whoever defines the components, evaluators, and permitted goals. A generated interface may feel personal while remaining constrained by an invisible factory the user cannot inspect. Malleable software could restore agency at one layer while removing it at another.

So the interesting question may not be whether software becomes malleable or industrial. It appears to be becoming both.

The question is whether we can build production machinery rigid enough to make software fluid, without making the people using it rigid too.
