# Ch6: RAG and Agents

Context construction = feature engineering for foundation models. Two patterns: **RAG**
(retrieve relevant info from external sources) and **agents** (use tools to gather info
and act). Context construction matters even as context windows grow — models use long
contexts poorly (lost-in-the-middle), and every extra token costs latency + money.

## RAG

Retriever + generator. Indexing (process data for fast lookup) + querying (fetch relevant
chunks). Split documents into chunks; join retrieved chunks + prompt → generator.

**Retrieval algorithms**:
- *Term-based (sparse)*: TF-IDF — `Score(D,Q) = Σ_i IDF(t_i)·f(t_i,D)`, `IDF(t) = log(N/C(t))`.
  BM25 (Okapi) normalizes by document length; Elasticsearch uses an inverted index. Fast,
  cheap, works out of the box, hard to improve; suffers term ambiguity ("transformer").
- *Embedding-based (dense)*: embed chunks (vector database), embed query, fetch k nearest
  by cosine similarity. Semantic, handles paraphrase; needs a good embedding model; cost of
  embedding generation, storage, and vector search can be 20–50% of API spend. ANN index
  algorithms: **LSH** (hash similar vectors to buckets), **HNSW** (multi-layer navigable
  graph — high accuracy, big memory), **product quantization** (decompose + lower-dim
  distances), **IVF** (k-means clusters; backbone of FAISS), **Annoy** (random-split trees).
  Trade-off axes: recall, QPS, build time, index size (ANN-Benchmarks). Evaluation: BEIR.
- *Hybrid*: cheap retriever fetches candidates → expensive precise retriever *reranks*
  (e.g., BM25 → vector search, or rerank by recency for time-sensitive data); or ensemble
  rankings via **reciprocal rank fusion**: `Score(D) = Σ_i 1/(k + r_i(D))`, k≈60.

**Retrieval optimization**:
- *Chunking*: equal-size by chars/words/sentences/paragraphs; recursive splitting (sections→
  paragraphs→sentences); overlap (~20 chars) to avoid context loss at boundaries; chunk by
  the generative model's tokenizer (but reindex if you swap models). Smaller chunks = more
  diverse info but more index/embedding overhead and info loss; no universal best size.
- *Query rewriting*: resolve anaphora ("How about Emily Doe?") — rewrite standalone queries;
  if info is missing (his wife), admit it rather than hallucinate.
- *Contextual retrieval*: augment chunks with metadata/tags, expected questions, or an
  AI-generated 50–100-token "situate this chunk in the document" preamble (Anthropic) —
  big retrieval wins.

**Multimodal / tabular RAG**: CLIP joint embeddings for image+text retrieval; tabular data
via text-to-SQL → execute → generate (SQL executor is a tool).

## Agents

An agent perceives its environment and acts on it; capabilities = tool inventory × planner.
Models for agents must be stronger: per-step accuracy compounds (95%^10 ≈ 60%, 95%^100 ≈
0.6%), and tool access raises stakes.

**Tools**: knowledge augmentation (retrievers, SQL, web browsing — prevents staleness),
capability extension (calculator, code interpreter — math is cheap to delegate; Chameleon:
GPT-4 + 13 tools beat GPT-4 alone by 11% on ScienceQA), and **write actions** (email, bank
transfers) — powerful but dangerous: least privilege, human approval for irreversible ops.

**Planning**: decouple planning from execution — generate a plan, validate it (heuristics:
invalid actions, step caps; or AI judge), execute, then reflect. Loop: plan → reflect →
execute → reflect until done. Control flows: sequential, parallel (latency win), if,
for-loop. **Function calling**: declare tool inventory (name, params, docs); per-query
required/none/auto. Inspect actual parameter values. Generate plans in natural language
rather than exact function names (robust to API changes; a cheap translator maps to
executables). **Reflection** (ReAct's interleaved Thought/Act/Observation; Reflexion's
evaluator + self-reflection modules) is cheap to add and gives big wins. LLMs are
questionable planners (LeCun/Kambhampati: they extract knowledge, not plans) — augment
with search + state tracking if needed.

**Agent failure modes & eval**: planning failures (invalid tool, valid tool + invalid params,
valid tool + wrong values, goal failure, reflection errors — "assigns 40 of 50 people and
declares done"), tool failures (wrong outputs, missing tools), efficiency (steps, cost,
duration per task — compare vs baseline). Track plan validity rates, tool-call validity,
per-tool error patterns; plot tool-call distributions; ablate tools (remove → performance
drop? if not, drop the tool). Benchmarks: Berkeley Function Calling Leaderboard, TravelPlanner.

## Memory

Three mechanisms: **internal knowledge** (weights — fixed unless retrained), **short-term**
(context — fast, capacity-limited, per-query), **long-term** (external stores via retrieval —
persistent, deletable). Store rarely-needed info externally; frequently-needed info in
weights; immediate info in context. Memory enables: overflow management in long agent
trajectories, cross-session persistence, consistency ("I remember I gave you an 8").

## Takeaways

- RAG = right info at query time; evaluate retriever AND end-to-end output.
- Agents = tools + planning + reflection; compound failures mean you must instrument and
  evaluate every step.
- Start simple: BM25 before vector databases; small tool sets before big ones.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch6.
