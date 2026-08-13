---
title: From Gatekeepers to Plumbers?
subtitle: What happens when engineering is no longer the default place where organizational knowledge meets
tags: [ai, software-engineering, llm, maintenance, ownership, theory-building]
created_at: 2026-08-13
---

> **TL;DR:** Software knowledge is already distributed across organizations. Because production changes usually passed through engineers, they became gatekeepers and an accidental integration point for that knowledge. AI agents may automate the translation from intent to code without reproducing the boundary-spanning it required. Engineers may shift from approving every change to building the plumbing—platforms, constraints, visibility, and routes to expertise—that lets distributed production remain coherent.

Imagine a payment system fails in production.

An operations analyst recognizes the rejected request as part of a manual settlement process. She asks an engineer, who understands the service's state machine but not the partner procedure. Together they direct a coding agent. It adds a fallback and tests. Operations confirms the workflow; engineering confirms the implementation. The fix is locally correct.

It ships. A week later, the risk team discovers that the fallback bypasses a control introduced after an old fraud incident. That decision never appeared in the repository or settlement procedure. It lived in another meeting, another escalation, and another group's memory.

Nobody in this story was simply ignorant. Operations knew the process. Engineering knew the system. Risk knew the control. The agent knew enough of the repository to produce a working change. The failure was that these fragments did not meet before becoming executable.

That problem is older than AI. What AI may change is the mechanism that used to make some of those fragments meet.

## The accidental integration point

Organizations already understand software collectively. Product knows what should happen. Operations knows what happens under pressure. Support knows where users struggle. Legal and risk know the constraints. Engineers know how these realities are encoded in technical systems. No individual understands the whole.

Historically, however, engineers were the primary gate through which this knowledge became software. Requests could originate anywhere, but production behavior usually required someone who could turn them into data models, state transitions, failure modes, and code that fit an existing system. Engineers were gatekeepers because implementation depended on them, whether or not the organization formally gave them that role.

This translation was often terrible. A detailed operational practice became a thin ticket. A domain distinction disappeared inside a generic requirement. Engineers made assumptions because the relevant expert was unavailable or unknown. The gate was slow, expensive, and lossy.

But gatekeeping had a side effect. Because changes converged on engineering, implementation required someone to consider each request against the surrounding system. Engineers did not always find the right people or ask the right questions, but implementation scarcity created pressure for partial views to meet. Engineering became an accidental integration point for organizational knowledge.

AI may weaken that scarcity before we replace its integrating function.

A domain expert can increasingly move from intent to working software through conversation. Sometimes an engineer remains a co-author or reviewer. Sometimes a business team builds and deploys the result itself. Both arrangements reduce the distance between the person who knows the problem and the behavior of the system.

That is a real improvement. It may preserve knowledge that would otherwise be distorted in translation. But it also lets a locally valid view become executable without passing through the place where other views used to converge.

AI does not make software understanding collective. It may make software production as distributed as the understanding already is.

## Haven't we seen this before?

People outside engineering have built software for decades. Spreadsheets, macros, Microsoft Access, workflow builders, and low-code platforms already created shadow systems throughout organizations. Citizen development is not an invention of large language models.

The difference is not absolute. It is a combination of range and rate.

Earlier tools often constrained either the authoring surface or deployment reach. Spreadsheets and macros could become general programs, but usually remained inside workbook or application boundaries. Workflow platforms exposed predefined triggers and actions. Shadow systems could still become critical, but their available moves or operating scope were often more bounded.

Coding agents can generate open-ended implementations. A request to "make retries safe" may produce a uniqueness constraint, a cache, a token table, or a distributed lock. The answer silently contains decisions about time, storage, failure, and ownership. The person requesting the change may have specified the desired outcome without realizing how many additional choices arrived with it.

Agents also operate at a different speed and can cross more boundaries. They can inspect repositories, change schemas, add dependencies, write deployment configuration, and produce a pull request in one session. The old citizen-development problem does not disappear; it gains reach and a much higher production rate.

There are signs of this acceleration inside engineering, although current evidence does not establish that domain teams are modifying production systems at scale. A [July 2026 study of Microsoft engineers](https://arxiv.org/abs/2607.01418) found that adopters of command-line agents merged roughly 24% more pull requests. The researchers cautioned that pull requests measure output, not value. A [June 2026 GitLab survey](https://about.gitlab.com/press/releases/2026-06-23-gitlab-research-reveals-organizations-are-generating-ai-code-faster-than-they-can-control-it/) reported that 78% of respondents saw faster code output while 85% said the bottleneck had moved to review and validation. It was a vendor-sponsored survey based on self-reports, but the mismatch is plausible: generation scales more easily than attention.

The broader organizational shift remains a hypothesis. The interesting question is what happens if it continues.

## Naur's theory, beyond the programming team

Peter Naur's 1985 essay [*Programming as Theory Building*](https://gist.github.com/eug/6d4f2e1dccedc4874979eb41e87b99e8) argued that programming is not primarily the production of source code and documentation. Its essential activity is building a theory in the programmers' minds.

"Theory" here means the working understanding that connects a program to the world it addresses. Someone possessing it can explain what the program does, why it is shaped that way, and which modifications would preserve its integrity. The theory includes which distinctions matter, which invariants protect money or trust, why an ugly exception exists, and what happens when the system is wrong.

Naur placed theory in individual minds while describing programming teams that possessed and sustained it collectively. A program remained alive while such a team controlled its modification. It died when the team dissolved: the code might continue running, but demands for meaningful change could no longer be answered intelligently from the text alone.

Modern systems suggest a broader unit than the programmer team. The relevant theory may be distributed across engineers, operators, product managers, support staff, lawyers, auditors, incident histories, tests, and agents. Artifacts can support this network, but they do not make it answerable by themselves. No participant needs the entire theory. What matters is whether the necessary views can be found and composed when a consequential question appears.

This is where AI creates a particular tension. An agent can form a useful local theory. It can search a million-line repository, test hypotheses, diagnose a failure, and explain how nearby components interact. Longer contexts and persistent memory may improve this technical understanding.

But the code-to-world theory is not all in the repository. A model knows about a support escalation, budget compromise, regulatory fear, or power struggle only through traces made available to it. More importantly, it does not occupy an accountable role in the institution that produced those facts. Memory can preserve an explanation; it cannot decide whose interests should prevail or who must answer for the result.

The problem is not that an AI can never understand code. It is that a local theory can now become implementation before the relevant wider views have been assembled.

## The integration gap

Call this an **integration gap**: the knowledge required for a sound decision exists somewhere in the organization, but the relevant fragments do not meet before that decision becomes executable.

This is not technical integration between services. It is not the same as governance, ownership, or approval. A company can restrict who may deploy, require five reviewers, and record a name in `CODEOWNERS` without surfacing the team whose constraint the change violates. Those controls can assign authority without integrating knowledge.

Most engineering plumbing governs what is already known: permissions, schemas, tests, architectural boundaries, and deployment policies. The harder plumbing described here must also help discover what a change needs to know. It must route decisions toward relevant expertise before every dependency has been formalized as a rule.

A platform can reject a forbidden database operation. It cannot automatically know that a fallback conflicts with an agreement remembered only by the risk team. Good organizational plumbing would help that knowledge meet the change without requiring an engineer to stand at every gate.

Nor does integration require everyone to understand every generated line.

> We may not need to understand how every part of a system works. But someone must understand why the system exists, what it must preserve, and what happens when it is wrong.

That "someone" may be an answerable network rather than a person. Operations can hold operational invariants, legal can hold regulatory boundaries, product can hold intended behavior, and engineering can hold architectural constraints. Agents may translate among these layers. The requirement is that changes with meaningful cross-boundary risk reach the relevant parts of the network before becoming behavior.

Abstraction remains necessary. Human attention should move toward intent, invariants, and consequences as machines produce more implementation. But abstraction discards information. The network must retain the ability to inspect code when risk, novelty, or uncertainty demands it. Engineering cannot become a ceremonial approval layer for a volume of changes it cannot realistically examine.

Review alone is not a replacement for the old convergence point. Several teams can approve a change without their relevant knowledge ever meeting. Documentation alone is not a replacement either. It records what somebody knew and chose to write, and can flatten unresolved disagreement into a single account.

An integration gap does not by itself kill a program; organizations have always survived missed context. The more provocative possibility is that software production can begin and continue through such gaps before an answerable network ever forms. That program may be **born dead** in Naur's sense—not because an LLM touched it, or because no individual understands every line, but because software intended to evolve was created without a network capable of discovering why it behaves as it does, integrating affected perspectives, and identifying who has authority to answer for its consequences. It may be tested, typed, documented, and executable while remaining unintelligibly modifiable when the world asks an unexpected question.

## From gatekeepers to plumbers

Keeping all software production behind engineering is not the answer. It would preserve the bottleneck along with its accidental benefit. People closest to a problem should be able to act on their knowledge, and engineers were never reliable custodians of every business, legal, or operational concern.

One possible future is governed shared authorship: domain experts direct agents while engineers remain involved in consequential changes. Another is direct modification, with engineering building the plumbing—platforms, observable boundaries, architectural constraints, and paths to expertise—rather than approving every diff. Persistent agents may become part of that connective tissue, carrying incident history and design rationale across teams and sessions.

This would not demote engineers to maintaining pipes after the important decisions have been made. Designing the plumbing is itself systems work: deciding which boundaries must be hard, which decisions need human negotiation, what evidence should travel with a change, and where local autonomy must stop.

The metaphor does not solve the problem. Who determines which changes are consequential? How does a platform detect a conflict rooted in an undocumented partner agreement? How does an agent preserve disagreement rather than turn it into one confident explanation? How can engineers guard system-wide invariants without becoming the same overwhelmed gate under a new name?

The scarce capacity may no longer be implementation or even isolated understanding. It may be the ability to discover which partial theories a decision touches and bring them together before that decision becomes real.

Engineering has performed some of this integration because much production software has passed through engineers. As that convergence weakens, can engineers and domain teams build plumbing that preserves the integration without recreating the gate?

The shift from gatekeeping to plumbing is not inevitable, and the metaphor is imperfect. But it points at the missing function more clearly than "review":

**Can the organization bring together the knowledge a consequential change depends on without making every change pass through the same gate?**
