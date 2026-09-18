# Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

## Overview

This project implements an intelligent Tic-Tac-Toe agent using the **Minimax algorithm** with **Alpha-Beta pruning**.

The project compares plain Minimax and Alpha-Beta Minimax on the **same board position** and measures the number of nodes explored by each algorithm.

## Features

* Tic-Tac-Toe game state evaluation
* Plain Minimax algorithm
* Minimax with Alpha-Beta pruning
* Node-count comparison
* Pruned branch demonstration
* Verification that pruning does not change the final result

## Algorithms

### Minimax

Minimax explores possible game states and selects the optimal game value.

* `+1` → X wins
* `0` → Draw
* `-1` → O wins

### Alpha-Beta Pruning

Alpha-Beta pruning improves Minimax by avoiding branches that cannot affect the final decision.

Pruning occurs when:

```text
alpha >= beta
```

The program displays the pruned branch and the Alpha-Beta values that caused the pruning.

## Node Count Comparison

Both algorithms are executed using the same Tic-Tac-Toe board position.

The program displays:

* Plain Minimax result
* Plain Minimax node count
* Alpha-Beta result
* Alpha-Beta node count
* Number of nodes saved
* Pruned branches
* Whether both results are unchanged

## Example Board

```text
X | O | X
---------
_ | X | O
---------
O | _ | _
```

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python tic_tac_toe.py
```

## Project Structure

```text
tic-tac-toe-alpha-beta/
│
├── tic_tac_toe.py
├── README.md
└── LICENSE
```

## Conclusion

The project demonstrates that Alpha-Beta pruning can reduce unnecessary node exploration while preserving the Minimax game value.

The pruned branches cannot affect the final decision because of the Alpha-Beta bounds.

