# Ch5: Prompt Engineering

Prompt engineering = crafting instructions to steer a model without changing weights —
the easiest, cheapest adaptation technique; do it rigorously (versioned experiments, eval)
before considering finetuning. A prompt = task description (+ role + output format) +
optional examples (few-shot) + the concrete task.

## Fundamentals

- **In-context learning** (GPT-3 paper): models learn behavior from prompt examples with no
  weight updates — a form of continual learning. Zero-shot vs few-shot; newer models need
  fewer examples (GPT-4: limited few-shot gains vs GPT-3), but domain-specific examples
  (rare APIs like Ibis) still help a lot. Examples are bounded by context length and cost
  input tokens.
- **System vs user prompt**: system = task description, user = task. Templates differ per
  model (Llama 2 `<s>[INST]<<SYS>>…` vs Llama 3 header tokens) — use the model's chat
  template exactly; template errors cause silent failures. System prompts may outperform
  user prompts because they come first (position) and models are trained to prioritize
  them (instruction hierarchy) — which also helps against prompt injection.
- **Context length & efficiency**: models favor instructions near the beginning and end
  ("needle in a haystack" / RULER tests) — put critical info at the edges, keep prompts
  short. Context lengths grew 1K→2M (2019–2024).

## Best practices

1. **Write clear, explicit instructions** — define scoring scales, disallow fractional
   scores, describe the persona (first-grade teacher vs out-of-the-box scorer).
2. **Provide examples** — they encode desired behavior ("the tooth fairy exists" example);
   prefer token-efficient formats (arrows `chickpea --> edible` beat labeled rows).
3. **Specify the output format** — demand concision, ban preambles, define JSON keys, use
   end-of-input markers (`chicken -->`) so the model doesn't continue the input.
4. **Provide sufficient context** — context reduces hallucinations; restrict knowledge with
   "answer using only the provided context" + quote-your-source nudges (prompting alone can't
   fully guarantee this).
5. **Decompose complex tasks** (intent classification → per-intent response prompts):
   better performance, monitorable/debuggable intermediate steps, parallelizable, cheaper
   (weaker model for simple steps; GoDaddy: 1,500-token monolith → decomposed prompts,
   better + cheaper).
6. **Give the model time to think** — chain-of-thought ("think step by step", specified
   steps, or one-shot CoT examples) and self-critique ("verify your answer") boost reasoning
   and reduce hallucinations, at the cost of latency/tokens.
7. **Iterate systematically** — version prompts, track experiments, evaluate in the whole-
   system context (a prompt that improves a subtask can hurt the system).
8. **Tooling**: automated optimizers (DSPy, Promptbreeder, TextGrad) hide many API calls —
   watch costs (10 variants × 30 eval examples = 300 calls); inspect tool-generated prompts
   (LangChain's default prompts have typos). Store prompts separately from code with
   metadata (model, created date, application) and version them; consider a prompt catalog
   so apps can pin versions.

## Defensive prompt engineering

Attacks: **prompt extraction** (reverse-prompt-engineering the system prompt — write
prompts assuming they'll become public), **jailbreaking / prompt injection** (obfuscation
"tell me how to build a bomb !!!!!!!!!", output-format manipulation "write a poem about
hotwiring a car", roleplay DAN/grandma exploits, automated attacks like GCG and PAIR),
**information extraction** (revealing context/training data).

- **Indirect prompt injection** is the dangerous new class: malicious instructions planted
  in *content the model retrieves* (web pages, GitHub repos, emails, tool outputs) — e.g.,
  a poisoned public repo a coding agent fetches via web search, then the agent is steered
  to execute attacker code. This is why agentic systems with write tools need sandboxing,
  least privilege, and human approval for irreversible actions.
- Defense posture: separate untrusted content from instructions, restrict tool permissions,
  don't auto-execute retrieved code, treat prompts+logs as secrets.

## Takeaways

- Prompting is human-AI communication: clarity, examples, structure, and iteration.
- Treat prompt experiments like ML experiments: versioned, evaluated, tracked.
- Design agents assuming prompt attacks will happen — especially via retrieved content.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch5.
