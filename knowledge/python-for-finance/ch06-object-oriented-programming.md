# Chapter 6 — Object-Oriented Programming

## Core idea
OOP models financial entities as **classes** (abstract definitions) and
**objects** (instances), with attributes (features) and methods (operations).
It is the organizing paradigm for the book's DX derivatives library
(ch17–21).

## Core vocabulary
- **Class / object**: `HumanBeing` class; `Sandra` the instance.
- **Attributes**: instance state (`self.first_name`).
- **Methods**: operations (`def walk_steps(self, steps)`); `self` always
  refers to the current instance.
- **Instantiation**: `Sandra = HumanBeing('Sandra', 'blue')` calls
  `__init__`.

```python
class HumanBeing(object):
    def __init__(self, first_name, eye_color):
        self.first_name = first_name
        self.eye_color = eye_color
        self.position = 0
    def walk_steps(self, steps):
        self.position += steps
```

## OOP benefits for finance
- **Natural modeling**: financial instruments as objects with characteristics.
- **Abstraction**: a general `financial instrument` class, specialized by
  inheritance.
- **Modularity**: separate classes for stock, option, portfolio — code is
  decomposed and linked.
- **Inheritance**: European option inherits from derivative, which inherits
  from instrument.
- **Aggregation**: an option object *has* a stock object and a discount-curve
  object as attributes.
- **Encapsulation**: internal state hidden behind methods.

## The DX library pattern (preview)
The book builds `dx` as a set of classes: `market_environment` (data holder),
`constant_short_rate` (discounting), simulation classes
(`geometric_brownian_motion`, `jump_diffusion`, `square_root_diffusion`) and
valuation classes (`valuation_mcs_european`, `valuation_mcs_american`) —
all wired together via inheritance and aggregation. This is OOP applied to
derivatives analytics.

## Pitfalls
- Overuse: OOP adds ceremony; simple scripts are fine without classes
  (the book takes a "neutral stance").
- Mutable default/state bugs; prefer explicit `__init__` parameterization.
- Deep inheritance hierarchies become hard to follow — favor composition
  (aggregation) where natural.

## When OOP pays off in quant work
- A family of instruments with shared behavior (all derivatives have a
  maturity and a payoff; European vs American differ in exercise).
- A library where many objects cooperate (underlying, market environment,
  valuation) — the DX pattern.
- Reusable components across projects (simulation classes, discounting).
- For a one-off script or analysis, procedural/vectorized code is faster to
  write; OOP is a tool for structure and reuse, not a requirement.

## Bottom line
The paradigm chapter. Its payoff is ch17–21, where the entire derivatives
analytics package is built as a hierarchy of cooperating classes — the
cleanest demonstration in the book of OOP-for-finance.
