# Ch25 — MapReduce

**Source:** Grus, *Data Science from Scratch*, Chapter 25.

## Purpose
A programming model for **parallel processing over huge datasets**: split a
computation into a **map** phase (emit key/value pairs) and a **reduce**
phase (aggregate per key). Even though it's "passé" (superseded by Spark),
it's the canonical lesson in moving computation to data.

## The three steps
1. **Map**: a `mapper` function turns each input item into zero or more
   key/value pairs.
2. **Group**: collect all pairs with the same key.
3. **Reduce**: a `reducer` function processes each key's collected values
   into output pair(s).

## Word count (the canonical example)
```python
def wc_mapper(document):            # document -> (word, 1) pairs
    for word in tokenize(document): yield (word, 1)

def wc_reducer(word, counts):       # (word, [1, 1, ...]) -> (word, total)
    yield (word, sum(counts))
```
Single-machine orchestration:
```python
def map_reduce(inputs, mapper, reducer):
    collector = defaultdict(list)
    for input in inputs:
        for key, value in mapper(input):
            collector[key].append(value)
    return [output for key, values in collector.items()
            for output in reducer(key, values)]
```
`sum_reducer = values_reducer(sum)` abstracts "apply a function to each
key's values" — giving `sum`, `max`, `min`, `count_distinct` reducers from
one helper.

## Why MapReduce
- **Move processing to the data**: with billions of documents across 100
  machines, each machine runs the mapper on its local data, emits pairs, and
  only the *pairs* are shuffled to reducer machines (grouped so all pairs
  for a key land on one machine).
- **Horizontal scaling**: double the machines ≈ half the time (each machine
  does less map work; reducers split by key) — modulo fixed overheads.
- Without it, all data must travel to one machine, which processes one item
  at a time — no scaling.

## More general pattern (status-update analytics)
The same `map_reduce` handles richer jobs by choosing smarter mappers:
- **Friends-of-friends / social graph**: mapper emits the sorted pair for
  each friendship edge; reducer counts mutual pairs.
- **Matrix multiplication**: mapper emits `(row_i, col_k)` contributions and
  reducer sums them — MapReduce expresses linear algebra naturally.
- Key design rule: the mapper's keys define the *grouping* you'll reduce
  over, so choose them to express the aggregation you need.

## Key takeaways
- MapReduce = map (emit kv pairs) → shuffle/group (by key) → reduce
  (aggregate per key); the abstraction is the same whether on one machine or
  1000.
- The grouping-by-key step is the heart of it — it's what makes the
  computation parallelisable.
- Any "group by and aggregate" problem fits: word counts, graph stats,
  matrix products.

## Notes
- The book notes MapReduce is mostly legacy — but the *map/group/reduce
  mental model* still structures Spark/Dask/`pandas.groupby` thinking.
- The single-machine `map_reduce` function is a clean reference
  implementation (~15 lines).
