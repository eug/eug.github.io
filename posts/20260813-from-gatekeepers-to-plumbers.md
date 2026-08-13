---
title: From Gatekeepers to Plumbers?
subtitle: What happens when engineering is no longer where an organization's knowledge comes together
tags: [ai, software-engineering, llm, maintenance, ownership, theory-building]
created_at: 2026-08-13
---

> **TL;DR:** The knowledge needed to understand software is already spread across organizations. Because most production changes passed through engineers, they became an accidental meeting point for that knowledge. Agents may automate the translation from intent to code without reproducing the conversations that translation forced. Engineers may move from approving changes to building the plumbing that routes consequential decisions to the right constraints and people.

Imagine a payment system fails in production.

An operations analyst recognizes the rejected request as part of a manual settlement process. She asks an engineer, who understands the service's state machine but not the partner procedure. Together they direct a coding agent. It adds a fallback and tests. Operations confirms the workflow; engineering confirms the implementation. The fix is locally correct.

It ships. A week later, the risk team discovers that the fallback bypasses a control introduced after an old fraud incident. That decision never appeared in the repository or settlement procedure. It lived in another meeting, another escalation, and another group's memory.

Nobody in this story was simply ignorant. Operations knew the process. Engineering knew the system. Risk knew the control. The agent knew enough of the repository to produce a working change. The failure was that these fragments did not meet before becoming executable.

That problem is older than AI. What AI may change is the mechanism that used to make some of those fragments meet.

## The accidental integration point

The knowledge needed to understand software is already distributed across the organization. Product knows what should happen. Operations knows what happens under pressure. Support knows where users struggle. Legal and risk know the constraints. Engineers know how these realities are encoded. No individual understands the whole.

Historically, engineers were the primary gate through which this knowledge became software. Requests could originate anywhere, but changing production behavior required someone who could turn them into data models, failure modes, and code that fit the existing system. Implementation made engineers gatekeepers, whether or not the organization gave them that title.

The translation was often terrible. Operational practice became a thin ticket. Domain distinctions disappeared inside generic requirements. The gate was slow and lossy.

Yet it had a useful side effect. Because changes converged on engineering, someone had to consider each request against the surrounding system. Engineers did not always find the right people or ask the right questions, but implementation created pressure for partial views to meet. Engineering became an accidental integration point.

AI may remove that bottleneck before we replace its integrating function.

A domain expert can increasingly move from intent to working software through conversation. An engineer may remain a co-author, or a business team may build and deploy the result itself. Both reduce the distance between the person who knows the problem and the system's behavior.

That is a real improvement. It may preserve knowledge that translation would distort. But it also lets a locally valid view become executable without passing through the place where other views used to meet.

AI does not make software understanding collective. It may make software production as distributed as the understanding already is.

If engineering stops being the gate, its replacement may look like plumbing: systems that let teams act locally while routing consequential changes toward the knowledge they depend on.

## Haven't we seen this before?

People outside engineering have built software for decades. Spreadsheets, macros, Microsoft Access, workflow builders, and low-code platforms already created shadow systems throughout organizations. Citizen development is not an invention of large language models.

The difference is not absolute. It is a combination of range and rate.

Earlier tools often constrained either what authors could build or where it could run. Spreadsheets and macros could become general programs, but usually stayed within workbook or application boundaries. Workflow platforms exposed predefined triggers and actions. Shadow systems still became critical, but what they could do and where they could reach were often more bounded.

Coding agents can generate open-ended implementations. A request to "make retries safe" may produce a uniqueness constraint, cache, token table, or distributed lock. The answer silently decides questions about time, storage, failure, and ownership. The requester may specify the outcome without noticing how many other choices arrived with it.

Agents also work faster and cross more boundaries. In one session they can inspect repositories, change schemas, add dependencies, write deployment configuration, and produce a pull request. The old citizen-development problem gains reach and a much higher production rate.

Evidence of this acceleration still comes mainly from engineering. A [July 2026 study of Microsoft engineers](https://arxiv.org/abs/2607.01418) found that command-line-agent adopters merged roughly 24% more pull requests. The researchers cautioned that pull requests measure output, not value.

A [June 2026 GitLab survey](https://about.gitlab.com/press/releases/2026-06-23-gitlab-research-reveals-organizations-are-generating-ai-code-faster-than-they-can-control-it/) reported faster code output for 78% of respondents, while 85% said the bottleneck had moved to review and validation. It was a vendor-sponsored survey based on self-reports, but the mismatch is plausible: generation scales more easily than attention.

The broader organizational shift remains a hypothesis. The interesting question is what happens if it continues.

## Naur's theory, beyond the programming team

Peter Naur's 1985 essay [*Programming as Theory Building*](https://gist.github.com/eug/6d4f2e1dccedc4874979eb41e87b99e8) argued that programming is not primarily the production of source code and documentation. Its essential activity is building a theory in the programmers' minds.

"Theory" here means the working understanding that connects a program to the world: what it does, why it is shaped that way, and which changes would preserve its integrity. It includes the distinctions that matter, the invariants that protect money or trust, and the reasons behind ugly exceptions.

Naur placed theory in individual minds while describing programming teams that possessed and sustained it collectively. A program remained alive while such a team controlled its modification. It died when the team dissolved: the code might continue running, but demands for meaningful change could no longer be answered intelligently from the text alone.

For modern systems, the relevant team may extend beyond programmers. Engineers, operators, product managers, support staff, lawyers, and auditors each hold part of the connection between code and the world. Tests, incident records, documentation, and agents can help this network remember, search, and communicate. They do not make it answerable by themselves. No participant needs the whole theory; the needed views must be able to meet when a consequential question appears.

An agent can form a useful local theory. It can search a large repository, test hypotheses, diagnose a failure, and explain how nearby components interact. Longer contexts and persistent memory may improve this technical understanding.

But the full connection between code and the world is not in the repository. A model knows about a support escalation, budget compromise, or regulatory fear only through the traces it can access. Persistent memory can preserve an explanation, but it cannot decide whose interests should prevail or who must answer for the result. The risk is not that AI can never understand code. It is that a local understanding can now become implementation before the wider views have met.

## The integration gap

Call this an **integration gap**: the knowledge required for a sound decision exists somewhere in the organization, but the relevant fragments do not meet before that decision becomes executable.

This is not technical integration between services, nor is it solved by approval alone. A company can restrict who may deploy, require five reviewers, and record a name in `CODEOWNERS` without finding the team whose constraint the change violates. Those controls can assign authority without bringing the needed knowledge together.

Most engineering plumbing enforces what is already known: permissions, schemas, tests, architectural boundaries, and deployment policies. A platform can reject a forbidden database operation. It cannot know that a fallback conflicts with an agreement remembered only by the risk team. The harder task is helping a change find the knowledge it needs before every dependency has been written as a rule.

Nor does integration require everyone to understand every generated line.

> We may not need to understand how every part of a system works. But someone must understand why the system exists, what it must preserve, and what happens when it is wrong.

That "someone" can be an answerable network rather than one person. Operations may know the operational invariants, legal the regulatory boundaries, product the intended behavior, and engineering the architectural constraints. Agents may translate among them. Before a consequential change ships, it must reach the people whose knowledge it depends on.

Humans will need to focus more on intent, invariants, and consequences as machines produce more implementation. But the organization must still be able to inspect the code when risk, novelty, or uncertainty demands it. Engineering cannot become a ceremonial approval layer for a volume of changes it cannot realistically examine.

Neither review nor documentation replaces the old convergence point. Several teams can approve a change without their knowledge ever meeting. A document records only what someone knew and chose to write, and may flatten a real disagreement into one account.

A missed connection does not kill a program; organizations have always survived lost context. The stronger possibility is that software can be built through repeated gaps before an answerable network ever forms. Such a program may be **born dead** in Naur's sense.

This is not because an LLM touched it or because no individual understands every line. It is because software intended to evolve was created without a network able to explain its behavior, bring affected perspectives together, and answer for its consequences. The program may be tested, typed, documented, and executable yet hard to modify intelligently when the world asks an unexpected question.

## From gatekeepers to plumbers

Keeping all software production behind engineering is not the answer. It would preserve the bottleneck along with its accidental benefit. People closest to a problem should be able to act on their knowledge, and engineers were never reliable custodians of every business, legal, or operational concern.

One possible future is shared authorship: domain experts direct agents while engineers remain involved in consequential changes. Another is direct modification, with engineering building the plumbing—platforms, visible boundaries, architectural constraints, and paths to expertise—instead of approving every diff. Persistent agents may help carry incident history and design rationale across teams and sessions.

This would not demote engineers to maintaining pipes after the important decisions have been made. Designing the plumbing is itself systems work: deciding which boundaries must be hard, which decisions need human negotiation, what evidence should travel with a change, and where local autonomy must stop.

The metaphor does not solve the problem. Who decides which changes are consequential? How can a system find a conflict rooted in an undocumented partner agreement? How can engineers guard system-wide invariants without becoming the same overwhelmed gate under a new name?

The scarce skill may no longer be writing the implementation. It may be discovering whose knowledge a decision depends on—and bringing those people in before it becomes software.

The shift from gatekeeping to plumbing is not inevitable, and the metaphor is imperfect. But it points at the missing function more clearly than "review":

**Can the organization bring together the knowledge a consequential change depends on without making every change pass through the same gate?**
