---
title: The Engineer as a Learning-System Builder
subtitle: Agent-driven engineering is shifting the work from producing code to improving the system that produces it
tags: [software-engineering, ai, agents, systems-thinking, software-factories, learning-systems]
created_at: 2026-08-29
---

> **TL;DR:** As agents take on more implementation, engineers are moving toward building the system that produces software: its architecture, tools, constraints, verification, and feedback loops. “Software factory” captures the hard machinery this requires, but I think the more useful model is a learning system—one that can revise its own production process without quietly taking consequential choices away from people.

I have been writing around this shift for a while without having a precise name for it.

In [*Engineerification*](https://eug.github.io/posts/engineerification.html), I described people moving from producing an output to shaping a system that repeatedly produces it. In [*Soft Software Needs Hard Factories*](https://eug.github.io/posts/soft-software-needs-hard-factories.html), I argued that cheap, malleable software may require a much harder production core underneath: tests, constraints, permissions, evaluators, and feedback.

Recently I watched three interviews that approached the same change from different levels.

[DHH described](https://youtu.be/NYFGCESmikA?t=5558) moving from deep concentration on one implementation problem to coordinating many agent threads across terminals and machines. [Lauren Tan described](https://youtu.be/Cmoh-yR-usA?t=2725) restructuring a codebase so that architecture, static analysis, CI, skills, and review systems constrain how agents can change it. [Guillermo Rauch described](https://youtu.be/DdbCtAScTsk?t=1747) the new engineering meta-skill as building the machine that produces software rather than working directly on each output.

DHH's factory is personal: models, harnesses, machines, notifications, and review. Tan's is the repository: its architecture, verification, and executable rules. Rauch's is the organization: shared agents, institutional knowledge, cost allocation, and carefully placed human choke points.

They are describing different layers of the same motion. Implementation is becoming delegable, so engineering attention moves toward the conditions under which implementation happens.

“Factory builder” is a good name for part of this. But I do not think it is quite enough.

## When the production system becomes the artifact

The obvious story about coding agents is that they make programmers faster. The more interesting story is that they change what programmers work on.

If an agent can inspect a repository, implement a feature, run tests, and prepare a pull request, manually producing that change is no longer necessarily the highest-leverage task. The engineer can instead improve the environment through which every later change will pass.

That environment includes the prompt, but prompt writing is a small part of it. It also includes which tools the agent can use, how the repository is structured, which dependencies are permitted, how behavior is tested, what evidence reviewers receive, how changes are deployed, and what happens when something fails.

This is why the management analogy only goes so far. An engineer coordinating agents may look like a manager assigning work, but the distinctive work is executable. A good decision can become a test. A recurring warning can become a lint rule. A fragile convention can become an interface that makes misuse difficult. A production failure can change what the next agent is allowed to do.

The engineer is not only supervising workers. The engineer is redesigning the workplace after every important lesson.

This is the part that makes the factory metaphor useful. A factory is not merely a collection of workers. Its output depends on the arrangement around them: tools, stations, inputs, tolerances, inspections, and the path a product takes through the system.

Agent performance has the same property. The effective worker is not the model alone. It is the model plus the environment in which it operates.

## A factory assumes that the recipe is known

The metaphor becomes less convincing when we ask what the factory is producing.

A conventional factory is designed to repeat a process whose desired output is relatively stable. Software rarely works that way. We often discover what a program should do by using it. Requirements change because the environment changes, because users reveal something we did not understand, or because the first implementation makes a better question visible.

The production system therefore cannot only become better at enforcing yesterday's recipe. It needs to learn whether the recipe is still correct.

I have encountered a smaller version of this repeatedly while working with agents. An agent solves the local task and produces a plausible change, but the change damages the larger system. It introduces a second pattern where one should exist, crosses a boundary that was carrying more meaning than the code revealed, or satisfies the immediate request by weakening an assumption elsewhere.

Correcting the prompt may fix that attempt. It does not make the correction durable.

The durable response is to ask what the production system failed to represent. Perhaps the boundary should become an explicit interface. Perhaps a test should exercise the wider behavior. Perhaps the agent needs runtime evidence rather than another paragraph of instructions. Perhaps the relevant organizational constraint never reached the repository at all.

This is iterative systems thinking. The object being improved is not just the software. It is the system that produces, observes, and corrects the software.

By “learning,” I do not mean that the model must retrain itself or that an agent should be free to rewrite its own controls. The learning can be distributed across people and machinery. A failure becomes a test. A repeated correction becomes an interface. Runtime evidence changes an evaluator. A constraint whose original context has disappeared is revised or removed. The next attempt happens in a different environment because of what the previous attempt taught us.

None of this is entirely new. Continuous delivery, DevOps, and SRE already treat software as something improved through operational feedback. What agents change is the balance. Implementation capacity can now expand much faster than human verification capacity, even inside a small team. The feedback system moves from supporting software production to becoming its primary control surface.

## Closing the larger loop

A useful agent workflow now spans something like this:

1. A person states an intent or problem.
2. An agent gathers context and proposes or implements a change.
3. Architecture and permissions limit which paths are available.
4. Tests, evaluators, and reviewers produce evidence about the result.
5. The change reaches a real environment where its behavior can be observed.
6. That evidence changes the context, constraints, or machinery used for the next change.

Imagine an agent adding a bulk-import feature. The feature works and its local tests pass, but it writes directly to a shared table, bypassing the service that normally applies permissions and records an audit trail. Fixing the pull request is necessary, but the learning-system response goes further. The write path becomes an explicit interface, direct access becomes mechanically restricted, and the reason for the boundary travels with the constraint.

Months later, another change needs a faster import path. The agent encounters the boundary. It should not silently bypass it, but neither should the old rule block the new requirement forever. The system surfaces the affected permission and audit constraints to the people responsible for them. They may reject the change, preserve the rule, or design a new audited batch interface. The original failure has improved future production without turning one contextual decision into an unquestionable law.

Most current workflows are strongest in the middle. We can generate code, run tests, and review diffs. The weaker connection is from observed consequence back into the production system.

A failed check may stop one pull request without teaching the next agent why the check matters. A reviewer may leave the same comment on twenty changes. A production incident may result in a document that is never available when a similar decision is made. A rule may remain in CI long after the situation that justified it has disappeared.

A learning system needs more than feedback. It needs a way for feedback to alter future behavior.

Evidence is layered. Tests establish mechanical properties, telemetry reveals operational behavior, users reveal outcomes, and humans judge whether those outcomes are desirable. Without all four, the system can become better at producing the wrong thing.

That makes verification part of production rather than a gate after it. It also changes the role of architecture. Architecture is no longer only about making a system elegant or understandable to its human maintainers. It becomes the terrain through which agents act. Good paths should be obvious and local. Harmful dependencies should be difficult to introduce. Important invariants should be executable where possible.

This does not mean encoding every preference as a permanent prohibition. That would produce a factory that is consistent, fast, and increasingly wrong.

The constraints have to learn too.

## Hard constraints need a lifecycle

I still believe in a hard core and a soft edge.

The soft edge is the product solution: what form an idea takes, which alternatives are explored, and what we learn by putting something in front of a person. This part benefits from ambiguity. Exhaustively specifying the implementation upfront can prevent an agent from finding a better route.

The hard core contains what must remain true: safety properties, permissions, shared data contracts, legal obligations, and architectural boundaries whose violation would affect other people or systems.

This resolves some of the apparent disagreement between DHH's preference for describing outcomes and Tan's heavily constrained codebase. The requested solution can remain open-ended while the consequential invariants remain strict. We can be vague about what should emerge and precise about what it must not break.

But a hard constraint is also a frozen decision. It was created in a particular context, usually after somebody learned something. If the context changes, enforcing it forever is not learning. It is institutional memory without institutional reconsideration.

So constraints need ownership, explanations, and a path to revision. When a proposed change may alter, bypass, or invalidate an existing constraint, the system should surface that constraint explicitly. It should explain why the change touches it and route the decision to the people responsible for that domain.

This is where I want the human in the loop.

Not reading every generated line. Not approving every low-risk action. Those practices turn cheap implementation into an expensive review queue. The meaningful human control point is the moment when the system's governing assumptions may need to change.

## The factory is also a governance system

Once constraints become executable, they stop being only technical details. They determine which actions are easy, which are forbidden, which evidence counts, and which outcomes the system can produce.

Control over software therefore moves toward whoever controls the factory.

This creates an uncomfortable possibility. Agent-driven organizations may become flatter at the visible layer while becoming more centralized underneath. A designer or product manager can ship without waiting for an engineering team, but only inside an environment whose permissions, models, interfaces, and acceptable patterns were chosen elsewhere. A single internal agent can remove many handoffs while becoming an unusually powerful point of control.

The surface feels more malleable. The infrastructure becomes more authoritative.

That does not make shared factories undesirable. Personal collections of prompts and tools are difficult to govern and expensive to reproduce. Shared infrastructure can make good practices available to everyone rather than only to the most sophisticated agent users.

But the constraints in that infrastructure need to be visible and contestable. People affected by them should be able to understand why they exist, challenge them, and participate in changing them. Engineers may maintain the machinery, but they should not silently become the sole authors of organizational policy because policy happened to become code.

The amount of governance should depend on consequence. A temporary local tool can delegate far more to an agent than a system moving money, exposing private data, or changing a shared workflow. The point is not to keep a human attached to every operation. It is to preserve legitimate human authority over the value choices that matter.

Organizations also remain responsible for the systems they deploy. Autonomy changes the mechanism of action; it does not dissolve accountability.

## A role, not necessarily a destination

I think the engineer as a learning-system builder describes a real shift happening now.

The craft moves from producing every implementation toward building boundaries, making outcomes observable, converting repeated failures into reusable controls, and improving the loop through which intent becomes software. This is more than prompt engineering and more than managing a fleet of artificial programmers. It is systems stewardship under a new production model.

I am less certain that it describes a stable profession.

Agents can already help write tests, create evaluators, revise instructions, review architecture, and build the tools used by other agents. If they become capable of improving most of the factory, the human role will move upward again—to choosing objectives, judging unusual consequences, or deciding what should not be optimized.

Perhaps agents will eventually participate deeply in those decisions too.

The factory metaphor suggests that our durable achievement is a machine that produces software. I suspect the more durable achievement is a system capable of changing how it produces software as evidence changes—without quietly taking consequential choices away from the people who must live with the result.

If implementation is no longer the center of engineering, and factory building is only the next delegable layer, what exactly are we trying to keep human?
