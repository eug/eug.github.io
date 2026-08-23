---
title: Software Cartography
subtitle: A tentative idea for understanding systems that no person or model can hold in full
tags:
  - software-engineering
  - ai
  - llm
  - maintenance
  - observability
  - code-understanding
created_at: 2026-08-22
---

> **TL;DR:** We are getting much better at producing code than at understanding the systems that code becomes part of. I suspect we need a discipline focused not on representing a whole codebase, but on building small, evidence-based maps for the question at hand. I have been calling it **software cartography**. I am not yet sure where the metaphor breaks, but it seems useful enough to explore.

There is a strange asymmetry emerging in software.

It is becoming remarkably cheap to make a change. An agent can inspect a repository, add an endpoint, modify a schema, write tests, and prepare a pull request in one session. This is useful, and I doubt we are going back.

But the cost of understanding the resulting system does not seem to be falling at the same rate.

The agent that made the change may lose its context. The person who requested it may understand the desired outcome but not the implementation choices. The reviewer may verify the diff without reconstructing the surrounding system. A few months later, another person—or another agent—encounters the code as an archaeological artifact.

We may end up producing more software while being less able to answer basic questions about it:

- Which path does a request actually take in production?
- Where did this value come from?
- Why is this boundary here?
- Which apparently minor module is carrying most of the system's risk?
- Who knows what happens when this integration fails at 2 a.m.?
- What changed between the system that worked on Monday and the one that failed on Tuesday?

These questions are not answered by reading more code alone. They require different views of the same system.

That is where the map metaphor started to make sense to me.

## The repository is not the system

We often treat the repository as if it were the most complete account of the software. It is certainly the most concrete one. You can search it, execute it, and point to a line.

But a running system is larger than its source.

It includes configuration, data, queues, deployment history, traffic patterns, feature flags, failure modes, operator procedures, and assumptions held by people outside engineering. Some code is central in the dependency graph but almost never executes. Some unremarkable function sits on every important request path. Two services may appear independent in their repositories while being coupled by an undocumented operational routine.

The code describes what can happen. Runtime evidence tells us some of what does happen. History tells us how it became possible. People often know why it matters.

None of these is the system by itself.

The [parable of the blind men and the elephant](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant) captures this problem well. One person touches the trunk and describes a snake. Another touches a leg and describes a pillar. Another finds the side and describes a wall. None is simply wrong. The mistake is promoting a locally accurate observation into a complete account of the animal.

We do something similar with software. Static analysis touches dependencies. A trace touches one execution. Version history touches evolution. An operator touches lived failure. Each can produce valid evidence and still describe a different system. Software cartography is not the sighted observer who finally reveals the whole elephant. It is the practice of locating these partial observations relative to one another without pretending that any one of them is the whole.

This resembles a problem cartographers have always had: the territory contains more detail than a useful map can show. A map that attempted to reproduce everything would not be a better map. It would be another territory.

A road map omits elevation and soil composition. A topographic map ignores most restaurants. A transit map distorts physical distance to make connections legible. Each is inaccurate in a deliberate way because each is designed for a question.

Maybe software needs the same kind of purposeful inaccuracy.

## Not one diagram of everything

When I first thought about mapping software, my mind went to the usual architecture diagram: boxes, arrows, databases, perhaps a cloud icon. These are helpful, but they are usually maps of what somebody believes the system to be. They age quickly and tend to preserve the intended structure better than the actual one.

What I have in mind is less like maintaining one canonical world map and more like being able to construct a map on demand.

If I am investigating a slow checkout, I might want the execution paths for checkout requests, weighted by latency and request volume, with the last two weeks of deployments overlaid. If I am changing a customer identifier, I might want a data map showing where that value originates, how it is transformed, where it persists, and which teams consume it. If I am joining an unfamiliar project, I might want a map of the small set of files, people, incidents, and decisions that explain most of its current behavior.

Those are different maps. Trying to merge them into a single representation would probably make all of them worse.

So software cartography, if it is a useful term at all, is not a visualization product. I think it is closer to a practice: gathering evidence from a software system and turning it into a deliberately incomplete representation that helps answer a specific question.

The output might be a graph, a timeline, a table, an annotated trace, or even a short narrative. The important part is not that it looks like a map. The important part is that it says what evidence it used, what it left out, and what question it is good for.

## The theory that disappears

Peter Naur argued in [*Programming as Theory Building*](https://gist.github.com/eug/6d4f2e1dccedc4874979eb41e87b99e8) that a program is not primarily its text. The programmers who build it develop a theory: an understanding of how the solution corresponds to the world, why each part has its shape, and which changes would remain consistent with it.

On this view, maintaining software is not just editing text. It is extending a theory.

I find this framing even more uncomfortable now. Code can increasingly be produced without a durable theory forming in any human mind. A model may have something like a temporary working theory inside its context, but that context disappears. The human may retain the intent while delegating most of the design decisions. The repository remains, but the reasoning that produced it is thinly distributed or gone.

It is tempting to solve this by asking models to write more documentation. I am not convinced that is enough. Generated documentation can describe the implementation, but it may merely restate decisions that nobody examined. It also inherits the same problem as the architecture diagram: it starts becoming stale as soon as the system moves.

Naur was pessimistic about reconstructing a theory from program text and documentation. He may simply have been right. But modern systems leave other evidence: traces, logs, metrics, commits, incidents, review conversations, deployment events, and the knowledge scattered across an organization.

My tentative bet is that we can use this evidence to reconstruct *enough* of the theory for the task in front of us.

Not the whole truth of the program. A local, provisional model that lets us make one change without being completely lost.

## A map should admit uncertainty

There is an obvious danger here. A polished visualization can create more confidence than the underlying evidence deserves.

Imagine a dependency map generated only from static analysis. It may look authoritative while omitting dependencies created through configuration, reflection, shared data, or human procedure. An ownership map built from `git blame` may point to the person who renamed a file rather than the person who understands why it exists. A runtime map based on yesterday's traces may exclude the rare path that matters during an outage.

Perhaps a useful software map should make uncertainty a first-class feature. It should distinguish observed paths from inferred ones, current ownership from historical contribution, and absence of evidence from evidence of absence. It should have a timestamp. It should expose its sources. It should be easy to discard when the question changes.

This may be one of the places where the geographic metaphor is especially helpful. We do not ask whether a map is simply true. We ask what it represents, when it was made, at what scale, and for what journey.

I think we should ask the same of representations of software.

## Why this might matter more with agents

Humans have always inherited systems they did not understand. Every mature codebase contains forgotten decisions, dead ends, and regions people are afraid to touch. Software cartography would not be a response to a brand-new problem.

What agents change may be the rate and the balance.

They can create and modify code faster than people can absorb it. They can also cross boundaries quickly: application code, infrastructure, database migrations, and deployment configuration may all change in one task. At the same time, agents are unusually capable readers and synthesizers of the evidence a map would require.

This creates a slightly paradoxical possibility: the technology that increases the understanding gap may also be the best tool we have for navigating it.

An agent does not need to hold the entire system in its context if it can build the right map before acting. It could start with a question, gather structural and runtime evidence, identify gaps, and expand only the relevant region. Instead of repeatedly ingesting a repository and hoping the important parts fit, it could work from a compact representation whose omissions are explicit.

Humans might benefit from the same maps. In fact, a good test would be whether the representation supports a conversation between an agent, an engineer, and a domain expert—not merely whether it helps a model generate a patch.

I can imagine this becoming part of the normal workflow:

1. State the question or intended change.
2. Build a provisional map from the available evidence.
3. Mark what is observed, inferred, stale, or unknown.
4. Use the map to find the relevant code, behavior, history, and people.
5. Make the change, then update or discard the map.

This sounds somewhat like observability, program analysis, architecture recovery, code search, and organizational knowledge management because it overlaps with all of them. I do not know whether “software cartography” ultimately names a separate discipline or just provides a useful umbrella for techniques that already exist.

For now, the umbrella is the interesting part.

## What I still do not know

There are many unresolved questions.

How do we decide which evidence to trust? How do we map knowledge held by people without turning a useful directory into workplace surveillance? How do maps remain cheap enough to generate and temporary enough not to become another documentation burden? Can we measure whether a map improved a decision, or only whether somebody looked at it? At what point does abstraction hide the very anomaly we needed to see?

I also do not know how much of a program's “theory” can really be reconstructed. Some decisions were never recorded. Some explanations are post-hoc stories. Some parts of software make sense only in the political or commercial situation in which they were created. A trace cannot tell us why a team accepted a risk.

So I do not think maps will restore complete understanding. Complete understanding may be the wrong goal.

The intuition I cannot shake is simpler: when a territory becomes too large and changes too quickly for anyone to hold in their head, navigation becomes its own engineering problem.

We have invested enormous effort in tools for writing software, and we are now accelerating them dramatically. I suspect the next missing layer is not another way to produce code. It is a way to repeatedly answer: *Where are we, what matters here, and what do we still not see?*
