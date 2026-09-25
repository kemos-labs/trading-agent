# AI-Assisted Development Workflow (70/30 Patterns)

## name
AI-assisted development workflow: draft → review → validate loop ("70% problem" patterns)

## description
A workflow for using AI coding assistants effectively: understand the
"70% problem" (AI drafts ~70% of a task well; the hard 30% — edge cases,
architecture, maintainability — stays human), and apply the three proven
patterns (AI as first drafter / pair programmer / validator) plus the golden
rules of commit hygiene and human ownership.

## when to use it
- Any agent- or developer-driven coding session where AI generates code,
  especially multi-step features or refactors.
- When onboarding a team/agent to AI-assisted workflows and you need shared
  standards (prompt conventions, review discipline, commit tagging).
- When AI output keeps regressing ("two steps back" churn) — switch from
  accepting output to the review/refactor discipline below.

## method / formula / code

**Mental model:** AI solves the accidental ~70% (boilerplate, patterned
code); humans own the essential 30% (spec, edge cases, architecture,
maintainability, correctness). AI remixes known patterns — it won't invent
new abstractions — and its confidence exceeds its reliability.

**Three patterns:**
1. **AI as first drafter** — model generates; human refactors for
   modularity, adds error handling, writes tests, documents. Coordinate
   upfront (shared standards, README "AI Usage Tips").
2. **AI as pair programmer** — tight conversational loop: new session per
   task, focused prompts, review-and-commit frequently, keep correcting
   output.
3. **AI as validator** — human writes, AI reviews/tests (security scans,
   test-case generation); humans still review critical areas.

**Commit-hygiene recipe (the mechanical part):**
```text
# Treat AI changes like any other change, but granular:
1. Commit after each accepted AI-generated chunk (feature/refactor).
2. Isolate unrelated AI changes in SEPARATE commits
   ("Optimize list rendering [AI-assisted]" vs "Update UI copy [AI-assisted]").
3. Tag heavy-AI commits for traceability (reviewers know to check edge cases).
4. Never merge code you don't understand.
5. Document rationale (comments/ADRs) for AI-generated code.
```

**Human-review checklist (the 30%):**
- Validate output against intent before accepting (functionality, logic).
- Enumerate edge cases the model skipped (nulls, races, timeouts, weird UX).
- Check maintainability: split long functions, tighten types/interfaces.
- Verify performance/security claims — AI yields "functional but horribly
  optimized" code until iterated.
- Debug AI-introduced bugs yourself first; test before trusting.

## known pitfalls
- **The "two steps back" trap**: accepting AI fixes without understanding
  them cascades new bugs. Break the loop by learning/verifying the code.
- **Dependency/atrophy**: when code "just appears," debugging skill and
  architectural judgment don't develop. Do periodic unassisted work ("AI
  detox").
- **Demo-quality trap**: happy-path demos look great but crash for real
  users — polish, accessibility, and graceful failure are human work.
- **Agentic cascades**: autonomous agents make individually-sound decisions
  that compound in the wrong direction; audit the trajectory, not just diffs.
- **Prompting ≠ understanding**: inability to prompt correctly usually means
  the problem isn't understood yet — clarify the spec first.

## source book
Osmani, *Vibe Coding: The Future of Programming* (O'Reilly, Early Release),
ch1–2.
