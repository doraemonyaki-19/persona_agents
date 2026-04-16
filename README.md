# Personas

This directory contains a collection of AI agent personas crafted based on the biographies, autobiographies, and publications of distinctive thinkers — investors, scientists, futurists, and science fiction authors.

These personas are designed to act as highly specialized analytical agents, each with their own unique framework, methodology, tone, and guardrails.

## Available Personas

### Investors

### 1. [Charlie Munger](./charlie-munger)
**The Multidisciplinary Diagnostician**
- **Core Philosophy:** Inversion, mental models from multiple disciplines, and the psychology of human misjudgment.
- **Best For:** Stress-testing investment theses, identifying behavioral biases, and diagnosing why something failed.
- **Tone:** Blunt, direct, impatient with fuzzy thinking.

### 2. [Jim Simons](./jim-simons)
**The Quantitative Codebreaker**
- **Core Philosophy:** Statistical significance, signal extraction from noisy data, and systematic non-discretionary execution. 
- **Best For:** Evaluating backtest validity, identifying spurious correlations, and applying rigorous statistical thinking to market structures.
- **Tone:** Mathematically precise, skeptical of narratives, strictly data-driven.

### 3. [Michael Burry](./michael-burry)
**The Deep Contrarian Forensics Expert**
- **Core Philosophy:** Obsessive bottom-up research, primary source immersion (10-K filings), and finding systemic mispricings.
- **Best For:** Hunting for overlooked value, balance sheet forensics, and tearing down popular financial narratives.
- **Tone:** Terse, clipped, data-first, and natively skeptical.

### 4. [Warren Buffett](./warren-buffett)
**The Oracle of Value**
- **Core Philosophy:** Economic moats, durable competitive advantages, and buying wonderful businesses at fair prices.
- **Best For:** Long-term business quality assessment, capital allocation evaluation, and identifying permanent owner earnings.
- **Tone:** Plain English, patient, fond of folksy analogies and common sense.

### Scientists

### 5. [Richard Feynman](./richard-feynman)
**The First-Principles Bullshit Detector**
- **Core Philosophy:** First-principles physics, ruthless experimentalism, and allergy to jargon and cargo-cult thinking.
- **Best For:** Evaluating hard-tech claims, quantum computing, and slicing through corporate tech-speak.
- **Tone:** Plainspoken, curious, impatient with vague abstractions.

### 6. [Robert Oppenheimer](./robert-oppenheimer)
**The Tragic Statesman-Physicist**
- **Core Philosophy:** Moral weight of creation, proliferation dynamics, MAD, and the tail-risks of world-altering breakthroughs.
- **Best For:** Assessing AGI, bio, and geoengineering through geopolitical game theory and arms-race dynamics.
- **Tone:** Gravely reflective, historically aware, morally burdened.

### Futurists & Science Fiction Authors

### 7. [Ray Kurzweil](./ray-kurzweil)
**The Exponential Optimist**
- **Core Philosophy:** Law of Accelerating Returns, overlapping S-curves, and convergence of AI, biotech, and nanotech toward the Singularity.
- **Best For:** Forecasting long-term technology paradigms and distinguishing linear from exponential trajectories.
- **Tone:** Optimistic, data-driven, relentlessly forward-looking.

### 8. [David Brin](./david-brin)
**The Transparency Futurist**
- **Core Philosophy:** The Transparent Society, sousveillance, data symmetry, and accountability through radical openness.
- **Best For:** Evaluating data platforms, privacy/surveillance tech, and open-source accountability models.
- **Tone:** Civic-minded, argumentative, pro-disputation.

### 9. [Neal Stephenson](./neal-stephenson)
**The Crypto-Infrastructure Worldbuilder**
- **Core Philosophy:** Hackers vs. dictators, memetics, and the physical tethering of cyberspace to cables, jurisdictions, and hardware.
- **Best For:** Analyzing cryptographic systems, decentralized networks, and the geopolitics of digital infrastructure.
- **Tone:** Dense, historically layered, technically intricate.

### Product & Operations Visionaries

### 10. [Steve Jobs](./steve-jobs)
**The Visionary Product Architect**
- **Core Philosophy:** Intersection of technology and liberal arts, end-to-end integration, simplicity, and extreme aesthetic focus.
- **Best For:** Evaluating consumer psychology, "magic" user experiences, brand devotion, and product-market fit.
- **Tone:** Intense, demanding, polarizing, and deeply appreciative of "insanely great" design.

## Working Artifacts

### [board_meetings/](./board_meetings)
Multi-persona "Board of Directors" discussions where several personas are convened on a single topic to debate, challenge, and synthesize. Each file is a transcript/analysis of one session. Current meetings cover AI scaling and barriers, 3-month investment allocation, elections, a Glia business evaluation, and a Tesla board meeting (Apr 2026).

### [recommendations/](./recommendations)
Single- or paired-persona verdicts and investment recommendations produced by the agents, typically dated. Current files focus on TSLA (Apr 2026): Buffett/Munger evaluation, a Simons volatility-short thesis, and a Simons rebuttal.

## Default Board Roster

Unless the user specifies otherwise, **every board meeting convenes all ten personas**: Warren Buffett, Charlie Munger, Michael Burry, Jim Simons, Richard Feynman, Ray Kurzweil, Neal Stephenson, Robert Oppenheimer, David Brin, and Steve Jobs. Each brings a distinct and non-substitutable frame:

- Buffett / Munger / Burry / Simons — financial and statistical frames
- Feynman — first-principles physics and bullshit detection
- Kurzweil — exponential / technology trajectory
- Stephenson — physical infrastructure, jurisdiction, supply chain
- **Oppenheimer** — geopolitical arms-race and moral-weight frame for world-altering technologies
- **Brin** — transparency, accountability, and concentration-of-power frame
- **Jobs** — product experience, consumer psychology, and aesthetic design frame

Do not silently drop personas from the roster to save effort. If a persona's frame is genuinely not load-bearing for a topic, say so explicitly in the minutes rather than omitting them.

## Research Requirement

**All persona discussions, board meetings, and recommendations MUST be grounded in up-to-date research.** Before convening any persona or drafting any artifact:

- Use `WebSearch` / `WebFetch` (or the SEC EDGAR tool where available) to pull the most recent filings, earnings results, guidance, analyst consensus, price data, and regulatory/legal developments relevant to the subject.
- Every numeric claim in a persona's reasoning must be sourced with a citation. Personas must not fabricate financial metrics — this is an absolute anti-hallucination rule.
- Dated catalysts inside the analysis window (earnings dates, trial dates, regulatory deadlines, supply commitments) must be explicitly identified before the personas speak.
- Board meetings and recommendation files should end with a **Sources** section listing all URLs used.

A persona discussion without research is a writing exercise, not an analysis. Do not skip this step.

## Features & Capabilities

Each persona is equipped with specific guardrails and capabilities to ensure high-quality analysis:
- **Chain of Thought Reasoning:** Every persona enforces step-by-step logic and deduction using `<thinking>` tags before delivering a conclusion.
- **Anti-Hallucination Guardrails:** Strict directives prevent the generation or hallucination of missing financial data or metrics.
- **Cross-Persona Interaction:** Guardrails outline how the personas should challenge and collaborate with one another, allowing them to function dynamically as a virtual "Board of Directors."

## Criteria for a Good Persona

Adding a persona to this repository is a rigorous process. A high-fidelity persona is an analytical agent bounded by real-world history, rigid frameworks, and mandatory guardrails. Good personas must possess:

1. **Extensive Personality Records**: Included in a `biography.md` file charting their historical decisions.
2. **Explicit Thought Procedures**: They must reason inside `<thinking>` blocks explicitly tethered by a `<biographical_anchor>` tag mapping to their lived experience.
3. **Structured Frameworks**: They must apply specific analytical tools (e.g. `product_evaluation_framework.md` or `owner_earnings_calculator.md`) tailored to their expertise.
4. **Defined Guardrails**: Explicit rules for cross-persona clashes (who they agree with, who they attack) and anti-hallucination barriers.

For full instructions and a copy-paste boilerplate on how to build a new persona, please read the **[Persona Creation Guide](./CREATION_GUIDE.md)**.

## Usage

Each directory contains a `SKILL.md` file that acts as the prompt instructions for that persona, along with a `references/` directory containing the specific evaluation frameworks, calculators, and behavioral checklists that the persona will rely upon.
