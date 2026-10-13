"""Shows WHICH branches alpha-beta prunes and WHY the answer is unchanged."""
import sys
from ttt.engine import (parse, render, to_move, play, other, best_move_minimax,
                        best_move_alphabeta, subtree_size)

BOARD = sys.argv[1] if len(sys.argv) > 1 else "XO./.X./O.."
LIMIT = 6   # how many prune events to print


def main():
    b = parse(BOARD)
    p = to_move(b)
    print(f"Position ({p} to move):\n{render(b)}\n")

    m1, v1, s1 = best_move_minimax(b)
    trace = []
    m2, v2, s2 = best_move_alphabeta(b, trace)

    print(f"Plain minimax : best move {m1}, value {v1:g}, nodes visited {s1.nodes}")
    print(f"Alpha-beta    : best move {m2}, value {v2:g}, nodes visited {s2.nodes}")
    print(f"Pruned        : {s1.nodes - s2.nodes} nodes skipped in {s2.cutoffs} cutoffs\n")

    print(f"=== First {LIMIT} prune events (of {len(trace)}) ===")
    for i, ev in enumerate(trace[:LIMIT], 1):
        print(f"\n[{i}] depth {ev.depth}, {ev.player} to move  (alpha={ev.alpha:g}, beta={ev.beta:g})")
        print(render(ev.board))
        print(f"  Move {ev.cutoff_move} gave value {ev.value:g} -> cutoff.")
        print(f"  Pruned moves {ev.pruned_moves}  ({ev.pruned_nodes} nodes never visited)")
        print(f"  WHY: {ev.reason()}")

    print("\n=== Why the result is unchanged ===")
    print("A cutoff happens only when a node's value is already proven to be irrelevant to its")
    print("parent: the parent (on the other side) has a better alternative already in hand.")
    print("Skipped siblings can only push the node's value further in the direction the parent")
    print("already rejects, so the parent's max/min picks the same child as before.")
    assert (m1, v1) == (m2, v2)
    print(f"\nVERIFIED: identical best move ({m1}) and value ({v1:g}) from both algorithms.")


if __name__ == "__main__":
    main()
