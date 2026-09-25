# Ch01 — The 70% Problem: AI-Assisted Workflows That Actually Work

**Source:** Addy Osmani, *Vibe Coding: The Future of Programming* (O'Reilly, Early Release), Chapter 1 (will be ch3 of the final book).

## The 70% problem
AI coding tools routinely carry a task ~70% of the way: boilerplate, routine
functions, and scaffolded prototypes come fast and look plausible. The final
30% — edge cases, real architecture, maintainability, production behavior — is
where AI stalls and "two steps back" churn begins. In Fred Brooks' terms, AI
handles the *accidental/incidental* complexity (repetitive, patterned code)
but not the *essential* complexity (understanding and shaping the problem).

Key limitations to internalize:
- AI output is convincing-but-sometimes-wrong; it hallucinates functions and
  libraries. Confidence far exceeds reliability (Steve Yegge: "wildly
  productive junior developers").
- Current LLMs do **not** create fundamentally new abstractions or algorithms
  beyond their training data — they remix known patterns. No novel strategy or
  architecture will be invented for you.
- AI takes no responsibility; the human must own the *what / how / why*.

## Failure patterns to expect
1. **Two-steps-back loop**: fix one bug → AI fix breaks something else → new
   fix creates two more problems. Worst for novices who lack the mental model
   to judge the fixes (the "knowledge paradox": seniors use AI to accelerate
   what they know; juniors try to use it to learn *what* to do).
2. **Demo-quality trap**: happy path shines, real users crash it — nonsense
   error messages, unhandled edge cases, messy UI states, no accessibility,
   slow on modest hardware. Polish (error copy, discoverability, graceful
   degradation) is the human 30% AI won't generate.

A deeper risk: when code "just appears," the user never builds debugging
skills or architectural judgment, creating dependency on the tool. This
worsens with **agentic** AI (Cline, Devin, Claude Code) that plans/executes
whole tasks: individually-sound agent decisions can cascade the project in
the wrong direction, and a user without foundational knowledge can't audit
them.

## Two usage camps
- **Bootstrappers** (Bolt, v0, screenshot-to-code): zero → MVP in hours/days;
  fine for validation, not production.
- **Iterators** (Cursor, Cline, Copilot, Windsurf): daily-driver completion,
  refactoring, test/doc generation. Seniors succeed here by *constantly
  reshaping* AI output — splitting into focused modules, adding the error
  handling AI skipped, tightening types and interfaces — rather than
  accepting it.

## Three workflow patterns that work
1. **AI as first drafter** — AI drafts; humans refine/refactor/test. Team
   coordination first: agree on standards and prompting conventions (e.g. an
   "AI Usage Tips" README section: "functional components only," "Fetch API
   over Axios"), share winning prompts, and use version control as the safety
   net — **commit frequently and isolate AI changes in separate commits**
   (e.g. tag with `[AI-assisted]`) so missteps are bisectable/revertible.
2. **AI as pair programmer** — constant conversation, tight loops, minimal
   context. Best practices: new session per distinct task; focused, concise
   prompts; review + commit frequently; continuously correct the AI's output.
   Human-human pairing still wins for ambiguous, high-nuance design work;
   human-AI pairing shines for speed and solo contexts.
3. **AI as validator** — human writes, AI reviews (DeepCode, Snyk: injection/
   insecure-config checks; Qodo/TestGPT: test generation). Use AI for initial
   scans, but reserve critical areas (complex logic, UX, anything AI is weak
   on) for human review.

## Golden rules (condensed)
Be specific; always validate output against intent; treat AI as a supervised
junior; use AI to extend — not replace — thinking; coordinate upfront;
normalize AI talk in the team; isolate AI changes in git; review *all* code
equally; **never merge code you don't understand**; document decisions (ADRs);
share proven prompts; reflect and iterate on the workflow itself.

## Takeaways
The 70/30 split is a durable mental model for agent-assisted work: draft with
the model, but keep the shaping, validation, and ownership human. Discipline
in review, commit hygiene, and documentation converts AI speed into
maintainable software.

## Source
Osmani, *Vibe Coding* (O'Reilly Early Release 2025), ch. 1; based on his
*Elevate with Addy Osmani* essay "The 70% Problem" (Dec 4, 2024).
