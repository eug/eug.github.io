---
title: The Scaffold Must Learn
subtitle: Guardrails encode what an organization knows. The harder problem is finding what a change still needs to know.
tags: [ai, software-engineering, agents, platform-engineering, organizational-knowledge]
created_at: 2026-08-13
---

> **TL;DR:** Software is becoming a building that never stops changing. As agents do more of the construction, engineers may increasingly build the permanent scaffold around it. Part of that scaffold enforces what the organization already knows. The harder part must notice when a change may need knowledge it does not have, route it toward the right people, and learn from what they discover.

Scaffolding is supposed to come down.

It gives builders access to an unfinished structure. Guardrails stop them from falling. Load limits constrain what they can carry. Gates control who may enter. Once the building is complete, the scaffold has done its job.

Software is different because it is never complete. A production system is repaired, extended, and partly rebuilt for as long as it remains useful. If agents perform more of that construction, the scaffold around them may become permanent.

The obvious parts already exist. Permissions control what an agent can reach. Schemas constrain the data it can produce. Tests protect known behavior. Architectural boundaries limit where a change can spread. Deployment policies decide what may reach production.

Platform engineering already has a useful [vocabulary for these controls](https://cloud.google.com/blog/products/application-modernization/platform-engineering-control-mechanisms): golden paths guide, guardrails stop, safety nets recover, and manual checkpoints add judgment. Most begin with a path, hazard, failure, or reviewer the organization already knows to provide.

These are valuable guardrails. They also share one limitation: someone had to know what to guard against.

Every fixed rail is a lesson in the past tense. A test encodes a behavior somebody decided to preserve. A permission reflects a risk somebody identified. A policy makes an earlier judgment repeatable. These mechanisms can stop a known mistake at machine speed. They cannot reliably find a fact that still lives only in another team's experience.

That is the part of the scaffold that must learn.

## When all the checks pass

In [*From Gatekeepers to Plumbers?*](https://eug.github.io/posts/from-gatekeepers-to-plumbers.html), I imagined an agent modifying a payment system after a failed settlement.

Operations understands the manual process. Engineering understands the service. Together they ask an agent to add a fallback. The agent produces a sensible implementation and tests. The change passes review and works as requested.

A week later, risk discovers that the fallback bypasses a control introduced after an old fraud incident. The control was not in the repository or the settlement procedure. It survived in the risk team's memory.

Conventional guardrails would not necessarily help. The change may respect every permission, schema, and architectural boundary. Its tests may be correct. The problem is not that it violates an existing rule. The problem is that the knowledge required to judge it never reached the change.

What would a learning scaffold do differently?

First, it would require the change to carry more than a diff. A short change brief could state the intended outcome, assumptions, affected systems and data, evidence, and remaining uncertainty. The scaffold could enrich that description with weak signals from the work itself: settlement terminology, a partner identifier, nearby incident records, services touched, and people involved in similar changes.

None of these signals proves that the risk team must review the fallback. Together, however, they may justify asking: *Who else could know something that matters here?*

The scaffold could suggest risk as a relevant perspective and explain why. Risk might then surface the old fraud control before deployment. The route, rather than a pre-existing rule, prevents the mistake.

What happens next matters. If the control is stable and general, the organization can turn it into a test, policy, or invariant. The next similar change meets a fixed rail. If the issue depends on a particular partner or changing circumstances, forcing it into a universal rule may be wrong. The scaffold should instead retain the rationale, the disagreement if any, and a route back to the people responsible for that judgment.

Learning does not always mean converting human knowledge into code. Sometimes it means learning whom to ask.

## No one sees the whole elephant

The [parable of the blind men and the elephant](https://en.wikipedia.org/wiki/Blind_men_and_an_elephant) describes people touching different parts of the same animal. One finds a wall, another a rope, another a spear. Each observation reflects something real, but each becomes misleading when mistaken for the whole.

Organizations work like this. Operations touches the workflow. Risk touches the control. Engineering touches the implementation. Support touches the consequences for users. An agent may touch far more of the repository than any of them, but that is still only another part of the animal.

The tempting response is to build a system that sees the whole elephant: collect every document, transcript, incident, and decision, then give it all to a model. That may improve retrieval, but it does not create a complete or neutral account. Some knowledge was never recorded. Some has expired. Some is disputed. Some decisions depend on authority and values, not missing information.

A more modest scaffold would not claim to know the whole. It would help partial observers find one another.

Psychologists call a group's knowledge of who knows what [transactive memory](https://dtg.sites.fas.harvard.edu/DANWEGNER/pub/Wegner%20Transactive%20Memory.pdf). A group does not need every member to remember everything. It needs a workable directory of expertise and a way to retrieve knowledge through the people who hold it.

Agentic production may turn that informal social ability into part of the delivery system. The platform would still store written context, but it would also maintain uncertain, revisable connections among systems, decisions, incidents, and people. Its output would sometimes be an answer. Other times it would be an introduction.

## A scaffold, not another gate

Routing every change to every possible expert would be safe only in the narrowest sense. It would recreate the old bottleneck with more notifications and less attention. The purpose of the scaffold is not universal approval. It is proportional contact.

Low-risk changes within familiar boundaries should move with little friction. Novel, uncertain, or cross-boundary changes should carry more evidence and invite more perspectives. The route should explain its signals so that people can correct it: this incident is irrelevant, that owner has changed, this term means something different here.

The routing mechanism will still fail. Its expertise map will become stale. Weak signals will miss unexpected dependencies and produce irrelevant suggestions. Powerful teams may make their concerns easier to discover than quieter ones. A confident agent may describe a change in ways that hide its uncertainty.

Those are not edge cases. They are reasons to treat the scaffold as a learning system rather than a finished control plane. Routes need feedback. Expertise links need decay and correction. Uncertainty must remain visible. Disagreement should be preserved rather than summarized into false consensus.

Nor can engineering own this system alone. Engineers can build the mechanism: change briefs, evidence trails, policy engines, expertise suggestions, and escalation paths. Domain teams must define and revise the knowledge, responsibilities, and authority those mechanisms point toward. Otherwise engineering remains the gatekeeper, only now behind an internal platform.

The scaffold succeeds when teams can act locally without pretending their local view is complete. That suggests different measures from approval counts alone: Did consequential changes reach the knowledge they depended on? Were irrelevant interruptions reduced? Did repeated discoveries become useful rails? Could the organization still find the right people when a judgment resisted formalization?

As agents make construction cheaper, the scarce capability may be recognizing what the construction does not yet know. Fixed guardrails remain necessary, but they are only the part of organizational knowledge that has already hardened.

The rest requires a scaffold that can ask, route, remember—and learn.
