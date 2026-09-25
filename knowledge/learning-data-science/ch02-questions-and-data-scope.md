# Ch02 — Questions and Data Scope

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 2.

## Purpose
Connects the research question to the **scope** of the data: exactly which
units the conclusions can legitimately be extended to. Scope errors are the
most common way analyses go wrong, and no amount of modeling fixes them.

## Three levels of scope
- **Target population** — the set of units your question is really about
  (e.g. all US voters, all donkeys in rural Kenya).
- **Access frame** — the set of units you *could* have reached (e.g. voters
  in the phone book, donkeys brought to deworming sites). Ideally ≈
  population.
- **Sample** — the units you actually measured. Ideally representative of
  the frame, which is representative of the population.

## Sources of bias (the checklist to run on any dataset)
- **Coverage bias**: the frame misses part of the population (e.g. only
  monitored news outlets, only landline phones).
- **Selection bias**: the sample is not drawn randomly from the frame (e.g.
  only the most "newsworthy" claims get fact-checked; only healthy donkeys
  brought to the vet get weighed).
- **Measurement bias**: the measurement itself is systematically wrong
  (e.g. uncalibrated scale, self-reported data, leading questions).
- **Drift**: data from the past may not describe the present (e.g. news
  topics, market regimes).

## Question refinement
A vague question ("why is my bus always late?") is refined into a
data-answerable one ("how late are buses at one stop vs their schedule?")
before any collection. The refinement chooses the scope.

## Reproducibility
Document where data came from, how it was collected, and when — so the
analysis can be re-run and its conclusions re-checked.

## Key takeaways
- State the population/frame/sample explicitly; name the biases you can
  think of even if you can't fix them.
- Random sampling (ch3) is the main defense against selection bias.
- Conclusions only generalize to the population, not the whole world.

## Notes
- The chapter's running example is the 2016 US election polling failure:
  polls over-represented certain groups (coverage/selection bias) despite
  huge sample sizes — more data does not fix bias (ch3's simulation shows
  this).
