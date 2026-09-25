# Ch02 — Beyond the 70%: Maximizing Human Contribution

**Source:** Addy Osmani, *Vibe Coding: The Future of Programming* (O'Reilly, Early Release), Chapter 2 (will be ch4 of the final book).

## The durable 30%
AI reliably produces *code*; it struggles with *engineering*. The human 30% =
understanding complex requirements, architecting maintainable systems,
handling edge cases, guaranteeing correctness. Tim O'Reilly's frame: this is
"the end of programming as we know it," not the end of programming — roles
evolve, they don't evaporate. The shift lowers the value of typing code and
raises the value of deciding *what* to build and orchestrating it.

## Senior engineers: leverage experience
- **Architect + editor-in-chief**: translate requirements into precise
  prompts/specs, then vet every line. Yegge's model — teams of "senior
  associates" who (a) describe tasks and (b) review results. Push back if
  juniors throw raw AI output over the wall; they must verify first.
- **Force multiplier**: *chat-oriented programming (CHOP)* — iterative prompt
  refinement as the working style — makes "wouldn't it be nice" projects
  feasible. Stay the guiding mind; sift suggestions, integrate the pieces.
- **Mentor + set standards**: teach juniors self-review and testing of AI
  code; normalize "disclose AI use and verify it yourself" norms.
- **Domain mastery + foresight**: catch what AI can't — second- and
  third-order effects, "too good to be true" snippets (trust the instinct).
- **Soft skills/leadership**: architecture roadmaps, tool evaluation, AI
  guidelines, cross-team consensus — the parts no tool can do.

## Midlevel engineers: adapt and specialize
The middle band is most squeezed — implementation, basic tests, and
straightforward debugging are automatable. The response is *elevation*:
- **Boundaries**: API design, event schemas, data models; deepen CS
  fundamentals (data structures, distributed systems, DB internals, network
  protocols) to judge generated code.
- **Domain expertise**: financial/regulatory, healthcare/privacy, real-time,
  ML-infra contexts reveal edge cases a generic model doesn't know.
- **Performance + DevOps**: observability, profiling, security/compliance,
  cost management — whole-stack understanding AI only hints at.
- **Code review + QA**: treat AI code like a junior's output; "assume nothing
  works until proven otherwise" (Sewell: AI yields "functional but horribly
  optimized code"). Testing is a durable skill that forces spec understanding.
- **Systems thinking**: the big picture (project history, business goals,
  regulatory constraints) lives in human heads — AI only knows what's fed to
  it. Read design docs; build judgment about what fits.
- **Adaptability**: learn tools constantly; do periodic "AI detox" so raw
  skills don't atrophy.
- **System design**: tradeoffs, scale, failure modes — "solid architecture
  doesn't emerge by accident."
- **Cross-functional communication + product thinking**: translating business
  needs ↔ technical solutions; some UI/UX/product literacy strengthens
  engineers without making them designers.

## Junior developers: thrive alongside AI
Juniors aren't obsolete, but the entry bar rises: fundamentals matter more
because review-and-validate work presupposes them.
- **Don't skip the "why"**: use AI as a tutor (ask it to explain line-by-line),
  keep fundamentals sharp — you need your own mental model to detect wrong
  output.
- **Practice without the safety net**: AI-free days; debug AI-generated bugs
  yourself first (stepping through a debugger teaches more than asking for a
  fix). Treat suggestions as hints, not answers.
- **Test everything**: challenge AI output with unit tests; *you* define what
  to test even if AI writes the tests. Catching an AI-introduced bug is
  demonstrable added value.
- **Maintainability eye**: refactor messy AI code as if reviewing a peer's
  PR — split long functions, rename unclear variables. This internalizes
  design principles and improves future prompting.
- **Prompting (wisely)**: good prompting is usually a proxy for
  understanding the problem; if you can't get the AI to comply, clarify your
  own thinking first. Outline a plain-English solution before asking for code.
- **Mentorship + communication**: ask seniors why they prefer X over AI's Y;
  absorb review comments on AI-written code ("not thread-safe," "scaling
  issues"); pair with AI-fluent seniors to observe their prompts and
  corrections.
- **Mindset: consuming → creating**: treat every AI solution as a learning
  case to dissect, not an answer to copy.

## Future-proofing checklist (the durable set)
System design/architecture; systems thinking; critical thinking,
problem-solving, foresight; specialized domain expertise; review/test/debug/
QA; communication & collaboration; adaptability; continuous learning with
strong fundamentals; and fluency *using* AI.

## Takeaways
AI is a "power tool for power users" (Willison): expertise makes the tool
more valuable, not less. The questions that stay human: *Does this solve the
right problem? Will others maintain it? What are the risks and edge cases?*

## Source
Osmani, *Vibe Coding* (O'Reilly Early Release 2025), ch. 2; based on his
essays "Beyond the 70%" (Mar 13, 2025) and "Future-Proofing Your Software
Engineering Career" (Dec 23, 2024).
