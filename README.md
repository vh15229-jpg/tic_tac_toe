# Tic-Tac-Toe with Minimax + Alpha-Beta Pruning

Tic-Tac-Toe solved with plain minimax and with alpha-beta pruning, with a node-count
comparison on identical positions and a demo of which branches get pruned and why.

Pure Python 3.8+, no dependencies.

## Run

```bash
python compare.py        # node-count comparison + exhaustive equivalence check
python demo_pruning.py   # shows pruned branches and the reason for each
python demo_pruning.py "X../.O./..X"   # try any position (X/O/. , '/' optional)
python play.py           # play against the alpha-beta AI
python -m unittest discover -s tests -t .   # tests (~5s)
```

## Results

| Position              | Minimax | Alpha-Beta | Saved |
|-----------------------|--------:|-----------:|------:|
| Empty board           | 549,946 |     20,866 | 96.2% |
| X center (O to move)  |  55,505 |      2,459 | 95.6% |
| X corner (O to move)  |  59,705 |      2,788 | 95.3% |
| Mid-game (X to move)  |     182 |         97 | 46.7% |
| Mid-game (O to move)  |   1,053 |        356 | 66.2% |
| Late-game (X to move) |       8 |          6 | 25.0% |

Across all 5,478 reachable positions: 2,126,493 vs 310,611 nodes (85.4% fewer), **0 mismatches**.

## Why pruning never changes the result

alpha = best value MAX can already guarantee; beta = best value MIN can already guarantee.
When alpha >= beta at a node, the opponent above already has a better alternative, so it will
never choose this node. Unexplored siblings could only push this node's value further in the
direction its parent already rejects, so the parent's max/min picks the same child.
`demo_pruning.py` prints each cutoff with its alpha/beta window and number of skipped nodes,
and asserts both algorithms return the same move and value.

## Layout

```
ttt/engine.py            minimax, alpha-beta, stats, prune trace
compare.py               node-count comparison
demo_pruning.py          pruned-branch demonstration
play.py                  interactive game
tests/test_equivalence.py
```
