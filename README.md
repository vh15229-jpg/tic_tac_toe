Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

🎮 Project Overview

This project implements Tic-Tac-Toe using the Minimax algorithm and Alpha-Beta Pruning in Python.

❌⭕ Tic-Tac-Toe Diagram

     |     |
  X  |  O  |  X
_____|_____|_____
     |     |
  O  |  X  |  O
_____|_____|_____
     |     |
  X  |     |  O
     |     |

🎯 Objectives

- Implement the Minimax algorithm.
- Use Alpha-Beta Pruning to reduce unnecessary searches.
- Compare the number of nodes explored by both algorithms.
- Show which branches are pruned and why.
- Verify that both algorithms give the same optimal score.

  1. Minimax searches possible moves and selects the best outcome. The maximizing player tries to obtain the highest score, while the minimizing player tries to obtain the lowest score.

  
2. Alpha-Beta Pruning
Alpha-Beta Pruning improves Minimax by skipping branches that cannot affect the final decision.
Alpha: Best score currently guaranteed for the maximizing player.
Beta: Best score currently guaranteed for the minimizing player.
Pruning condition: When alpha >= beta, the remaining branches at that node can be skipped.

⚙️ Technologies

- Python
- Visual Studio Code
- Git and GitHub

🧠 Algorithms

- Minimax: Searches possible moves to find the best result.
- Alpha-Beta Pruning: Skips branches that cannot affect the final decision.

▶️ How to Run

python compare.py
python demo_pruning.py
python play.py

📊 Expected Result

- Fewer nodes explored with Alpha-Beta Pruning on suitable positions.
- Pruned branches displayed with cutoff reasons.
- The optimal score remains unchanged.

🏁 Conclusion

Alpha-Beta Pruning improves Minimax efficiency by skipping unnecessary branches while preserving the optimal result.
