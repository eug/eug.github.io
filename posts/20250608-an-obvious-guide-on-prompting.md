---
title: An Obvious Guide on Prompting
subtitle: Because apparently, this needed to be said.
tags: [critical-thinking, prompting, discipline, ai]
created_at: 2025-06-08
---

Large Language Models (LLMs) are powerful, but their value depends on how you use them. It's easy to treat them like oracles or fall into the convenience trap, which is a waste of their potential and your brainpower. This is not a guide about prompting tricks or clever techniques — it's about how to think *with* AI, not just get answers *from* it.

This guide is for the everyday users: professionals, students, and curious minds who turn to LLMs to solve daily problems, get unstuck on projects, or explore new ideas. This is for those who haven't yet considered what happens when convenience becomes dependence.

>I once thought this guide would be redundant — that its advice was obvious. But observing how many people misuse these tools, it's become clear that's not the case. This is my attempt to state these principles plainly, because the real skill isn't in crafting the perfect prompt, but in maintaining intentional, critical thinking throughout the process.

### The Illusion of the Oracle

It's easy to see an LLM as a digital oracle. We ask, and it answers with confidence and eloquence. This conversational interface is a triumph of design, but it can also be misleading. Underneath the smooth surface is a system that works in a fundamentally non-human way.

The most well-known quirk is "[hallucination](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))", where the model generates plausible but false information. An LLM doesn't "know" facts; it generates statistically likely text. This means it can invent sources or misstate details with complete confidence, making blind trust a risky strategy.

Foundational model companies like [OpenAI](https://model-spec.openai.com/2025-04-11.html), [Anthropic](https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf), and [Google](https://modelcards.withgoogle.com/model-cards) have published specifications that reveal the guardrails and design principles shaping model behavior. While a step towards transparency, these documents are dense and technical. More illuminating are deep dives into how these models "think". An excellent [Anthropic article](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) demystifies this, showing that what looks like "reasoning" is often a form of sophisticated pattern-matching. It's a powerful tool for generating text, but it's not a conscious thinker. Understanding this distinction is the first step toward using it effectively.

### The Convenience Trap

Our brains are [wired to take the path of least resistance](https://www.sciencedirect.com/science/article/abs/pii/S0028393218303981?via%3Dihub); it's an efficient evolutionary trait. AI systems, designed for ease of use, tap directly into this. The smoother the experience, the more we rely on it, which can create a subtle feedback loop.

Consider a software developer who, instead of wrestling with algorithmic complexity, asks an LLM to "write a function to process this data". The model provides a working solution instantly. The immediate problem is solved, but the developer has bypassed an opportunity to deepen their understanding of data structures, performance trade-offs, and edge cases. Consider a marketing professional who asks the AI to "write a blog post about our new product" and publishes the first output verbatim. They have saved time, but have they produced the most compelling, nuanced, or strategically aligned content?

In both cases, the immediate goal is met, but a learning opportunity is missed. This is the core risk of convenience. Over-relying on AI for [core skills can cause them to fade over time](https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age), turning the tool into a ["velvet cage" that domesticates our intellect](https://francoisxaviermorgand.substack.com/p/what-if-ai-is-making-us-softer-than) through constant validation. It's not that using AI is inherently bad, but that using it *uncritically* makes our own thinking optional. The key is to use it as a tool that assists our thinking, not one that replaces it.

### Don't Outsource Your Brain

Beyond professional skills, how we interact with AI can influence our own thinking habits and resilience. Relying too heavily on a frictionless, validating partner can subtly change how we approach challenges.

Real problem-solving is messy. AI often smooths over the frustrating parts. Relying on this can **make us less willing to do the hard work of thinking**. Researchers warn that this might [affect our cognitive skills](https://www.nature.com/articles/s41562-024-01859-y).

It's also about **intellectual independence**. As highlighted in a recent study on adolescents, while AI dependence may not directly cause mental health problems, individuals with pre-existing issues like anxiety or depression are more likely to use AI as a coping mechanism, leading to [dependence](https://pmc.ncbi.nlm.nih.gov/articles/PMC10944174/). It's easy for the tool to become a crutch, eroding confidence in our own ability to think, write, or create without its assistance.

Finally, you risk creating an **echo chamber** and degrading your social skills. Psychologists have noted that AI can amplify confirmation bias, creating cognitive echo chambers on an [unprecedented scale](https://www.psychologytoday.com/us/blog/harnessing-hybrid-intelligence/202506/the-psychology-of-ais-impact-on-human-cognition). When our worldview is perpetually reinforced, our ability to empathize with different perspectives withers. At the same time, research on users of an AI companion suggests that while such tools can reduce loneliness, an over-reliance can harm real-world interpersonal skills. The AI relationship is inherently one-sided and doesn't require the [reciprocal emotional engagement](https://www.psychologytoday.com/intl/blog/urban-survival/202410/spending-too-much-time-with-ai-could-worsen-social-skills) that builds and maintains human connection.

Keep in the driver's seat. Use these systems consciously, and trade short-term ease for long-term growth and resilience.

### Strategic Prompting: Staying in Control of the Thinking Process

So, how do you get better? Treat AI like a thinking partner, not an answer machine. Here's a simple framework to get you started. It will get you better results and keep your brain from turning to mush.

**1. Decomposition:** Break down a complex request into a series of smaller, logical steps. Instead of "build me a website", a skilled prompter would start with "Outline a sitemap for a personal portfolio website for a software engineer. Include sections for a bio, projects, blog, and contact".

**2. Context Scaffolding:** Provide the necessary context, constraints, and persona for the model. Don't just ask for a summary; specify the audience and purpose.

*   **Weak Prompt:** "Summarize this scientific paper".
*   **Strong Prompt:** "You are a science journalist. Summarize this paper for a technically literate but non-specialist audience. Focus on the core hypothesis, key findings, and their potential real-world implications. Explain the methodology in simple terms. The summary should be no more than 300 words".

**3. Iterative Refinement:** Treat the AI's first response as a starting point, not a final product. Use follow-up prompts to challenge, refine, and deepen the output.

*   **Follow-up:** "That's a good start. Now, expand on the 'potential real-world implications.' What specific industries could this research impact? Are there any ethical considerations the paper overlooks?"

**4. Critical Evaluation:** This is the most crucial step. Always question the output. Is it accurate? Is it biased? Does it make logical sense? A [recent study](https://dl.acm.org/doi/pdf/10.1145/3701716.3715504) highlighted the dominant psychological traits embedded in these models. Understanding these inherent biases is key to knowing where to apply skepticism. Cross-reference claims with reliable sources. Use the LLM to generate ideas, but use your own intellect to validate and synthesize them.

**5. [Know What You Don't Know](https://en.wikipedia.org/wiki/I_know_that_I_know_nothing):** The most important skill is knowing the limits of your own knowledge. How you use an LLM should change depending on how much you know about a topic.

*   **When you are a novice:** On a subject you know little about, an LLM is an extraordinary tool for building a foundational understanding. It can explain complex topics, summarize new fields, and provide a scaffold for learning. Here, the skill is to acknowledge your ignorance and use the AI as a starting point, with the explicit understanding that you must verify this new knowledge against authoritative sources.
*   **When you are an expert:** In your own domain, the AI's role shifts from a teacher to a somewhat unreliable intern. It can accelerate your work by generating boilerplate, brainstorming ideas, or summarizing adjacent information. However, it can also introduce subtle, critical errors that only an expert can detect. Here, the skill is to never fully trust the output. You must critically evaluate its work through the lens of your own deep knowledge, catching flaws and refining its output to meet your high standards.

Knowing what you don't know is the key. It lets you switch between being a student and a master, so you're always in control.

### It's a Tool, Not a Replacement

Using AI well isn't about learning secret tricks. It's about being intentional. Be clear in your questions, use the AI to explore ideas, and always, *always* question the output. It's a tool to help you think, not a replacement for thinking.

The future is not about humans *versus* AI, but humans *with* AI. The nature of that partnership, however, is up to you. You can be a passive consumer, letting your own critical skills take a backseat to the convenience of automated answers. Or you can be active, discerning collaborators, using these tools to push your own thinking further. This second path requires effort and intention, but it's how you transform prompting from a simple query into a core skill for the future. The choice is yours to make with every query you type.

### The Obvious Conclusion

This isn't a threat, it's an opportunity. This technology, for all its imperfections and seductive ease, offers a chance 
to become more intentional about how we think. It's not just about getting better answers from a machine — it's about asking better questions and thinking critically. That kind of thinking is a muscle. It requires training, and while it can be hard, it's worth it to ensure the most important thinking is still your own.
