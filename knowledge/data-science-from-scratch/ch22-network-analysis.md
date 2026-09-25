# Ch22 — Network Analysis

**Source:** Grus, *Data Science from Scratch*, Chapter 22.

## Purpose
Model relationships as **graphs**: nodes connected by edges (friendships,
hyperlinks), and measure which nodes matter. Two centralities: betweenness
and PageRank.

## Basic definitions
- Graph = nodes + edges; **undirected** edges (Facebook friendship — mutual)
  vs **directed** edges (web hyperlinks — one-way).
- Represent adjacency as `Dict[int, List[int]]` (node → neighbors).

## Betweenness centrality
- **Degree centrality** (ch1: count friends) is a poor key-connector metric:
  a connector with few but pivotal links ranks low.
- **Betweenness centrality** of node i = sum over all other pairs (j, k) of
  the *fraction of shortest paths between j and k that pass through i*.
- Computation:
  1. **All-pairs shortest paths** via **breadth-first search** from each
     node: a `frontier` queue of `(prev, node)` pairs; keep *all* shortest
     paths per target; only enqueue never-seen neighbors; when revisiting a
     node, keep new paths only if they're no longer than the known shortest.
  2. For each (source, target) pair, add `1/num_paths` to each node on each
     shortest path.
- Who wins: the "connector" node (bridging two halves of the graph) scores
  high despite low degree — the insight ch1 lacked.

## PageRank
- **Idea**: a node is important if important nodes link to it. Modelled as a
  random surfer who follows links randomly, with a small **damping
  probability** of jumping to a random page (so dead ends / link farms
  don't trap the walk).
- **Iterative algorithm**: initialise each node's rank to `1/N`; repeatedly
  redistribute:
  - each node passes `rank / num_links` to each node it links to;
  - nodes with no outgoing links distribute their rank over *all* nodes;
  - renormalise with damping: `rank = (1 − d)/N + d·(link-received rank)`,
    with d ≈ 0.85.
- Iterate until ranks converge (a few dozen rounds is plenty); the
  steady-state ranks are PageRank. Ranks are relative — "important" pages
  score above the uniform baseline.
- This is the algorithm that powered Google's search ranking; it's
  implemented in ~40 lines.

## Key takeaways
- Two families of importance: *path-based* (betweenness: who bridges) and
  *eigenvector-like* (PageRank: who is linked to by the important).
- BFS with a frontier queue is the workhorse for shortest paths in
  unweighted graphs; remember to track *all* equal-length paths for
  betweenness.
- PageRank's damping factor handles disconnected/trapped structures — a
  reminder that real graphs are messy.

## Notes
- The book also implements **clustering coefficients** (degree-2 connectedness
  ratio) for "friends of friends" analysis in the exercises.
- Production: `networkx` has all of this built in (ch27).
