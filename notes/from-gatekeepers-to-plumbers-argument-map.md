# From Gatekeepers to Plumbers? — argument map

This document maps the claims and reasoning of the essay independently from its prose. It distinguishes established premises, the essay's central proposition, supporting evidence, objections, consequences, and unresolved questions.

```mermaid
flowchart TD
    subgraph B[Background: how software knowledge operated]
        B1[Organizational knowledge is already distributed]
        B2[No individual understands the whole system]
        B3[Implementation skill was scarce]
        B4[Most production changes passed through engineers]
        B5[Engineers translated domain intent into technical behavior]
        B6[Translation was slow, expensive, and lossy]
        B7[Translation also forced some domain and technical views to meet]
        B8([Engineering became an accidental integration point])

        B1 --> B2
        B3 --> B4
        B4 --> B5
        B5 --> B6
        B5 --> B7
        B1 --> B7
        B7 --> B8
    end

    subgraph A[AI changes the production path]
        A1[Agents lower the implementation barrier]
        A2[Domain experts can move more directly from intent to software]
        A3[Benefit: fewer lossy handoffs]
        A4[Risk: a locally valid view can become executable alone]
        A5[Agents generate open-ended implementation decisions]
        A6[Agents increase production speed and cross more system boundaries]

        A1 --> A2
        A2 --> A3
        A2 --> A4
        A5 --> A4
        A6 --> A4
    end

    B6 -. makes valuable .-> A3
    B8 -. may weaken as production decentralizes .-> A4

    T([Central proposition:<br/>AI may automate engineers' translation work<br/>without reproducing the boundary-spanning it compelled])
    A3 --> T
    A4 --> T
    B8 --> T

    subgraph O[Objection and qualification]
        O1{{Objection: non-engineers already built software<br/>with spreadsheets, macros, and low-code tools}}
        O2[The difference is not absolute]
        O3[Agents combine broader implementation range with higher production rate]
        O4[Evidence currently shows acceleration inside engineering]
        O5[Widespread direct production by domain teams remains a hypothesis]

        O1 --> O2
        O2 --> O3
        O4 --> O5
        O3 --> T
        O5 -. limits the strength of .-> T
    end

    subgraph E[Supporting evidence]
        E1[/Microsoft study:<br/>agent adopters merged about 24% more pull requests/]
        E2[/GitLab survey:<br/>output rose while review and validation became bottlenecks/]
        E3[Output is not value]
        E4[Vendor self-reports are not neutral measurements]

        E1 --> O4
        E2 --> O4
        E3 -. qualifies .-> E1
        E4 -. qualifies .-> E2
    end

    subgraph N[Naur as the explanatory lens]
        N1[Programming builds a theory connecting code to the world]
        N2[Individuals possess partial theories]
        N3[Programming teams sustain theory collectively]
        N4[Modern theory may span engineers, domain teams, artifacts, and agents]
        N5[Agents can form useful local technical theories]
        N6[Repositories and agent memory omit some tacit, political, and institutional knowledge]
        N7[Agents do not occupy accountable institutional roles]

        N1 --> N2
        N2 --> N3
        N3 --> N4
        N5 --> N4
        N6 -. constrains .-> N5
        N7 -. constrains .-> N5
    end

    T --> N4

    G([Integration gap:<br/>knowledge required for a sound decision exists,<br/>but the relevant fragments do not meet<br/>before the decision becomes executable])
    T --> G
    N4 --> G

    subgraph D[Important distinctions]
        D1[Not technical integration between services]
        D2[Not equivalent to governance, ownership, approval, or review]
        D3[Does not require everyone to understand every line]
        D4[Does require consequential changes to reach relevant knowledge]

        D1 -. narrows .-> G
        D2 -. narrows .-> G
        D3 -. narrows .-> G
        G --> D4
    end

    subgraph P[Proposed shift: from gatekeeping to plumbing]
        P1[Conventional engineering plumbing enforces known constraints]
        P2[Organizational plumbing must also discover what a change needs to know]
        P3[Route decisions toward relevant expertise and authority]
        P4[Preserve local autonomy without requiring engineering approval everywhere]
        P5[Retain the ability to inspect implementation when risk demands it]

        P1 --> P2
        P2 --> P3
        P3 --> P4
        P5 --> P4
    end

    G --> P2
    D4 --> P3

    subgraph C[Possible consequences and trajectories]
        C1[Governed shared authorship:<br/>domain experts and engineers direct agents together]
        C2[Direct modification:<br/>domain teams act within platforms and constraints]
        C3[Persistent agents may carry rationale and incident history]
        C4[Engineers may design boundaries, routing, evidence, and escalation]
        C5[Failure mode: engineers become an overwhelmed approval gate again]
        C6[Born-dead software:<br/>evolving code exists before an answerable network forms]

        P4 --> C1
        P4 --> C2
        P3 --> C3
        P2 --> C4
        C4 -. can regress into .-> C5
        G -. if persistent and structural .-> C6
    end

    Q{{Open question:<br/>Can the organization bring together the knowledge<br/>a consequential change depends on<br/>without making every change pass through the same gate?}}

    C1 --> Q
    C2 --> Q
    C3 --> Q
    C4 --> Q
    C5 --> Q
    C6 --> Q
```

## Argument in compact form

1. Organizational knowledge was already collective and fragmented.
2. Scarce implementation skill made engineering the default route into production.
3. That route distorted knowledge, but also forced some knowledge boundaries to be crossed.
4. Agents may automate implementation and decentralize production without triggering the same boundary-spanning.
5. The result may be an integration gap: relevant knowledge exists but does not meet the change in time.
6. Conventional guardrails enforce known constraints; they do not discover uncodified dependencies.
7. The proposed “plumbing” must therefore route consequential changes toward relevant knowledge and authority while preserving local autonomy.
8. Whether an organization can build that plumbing without recreating the engineering bottleneck remains unresolved.
