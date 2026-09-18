# Tic-Tac-Toe: Minimax and Alpha-Beta Pruning

E = "_"
X, O = "X", "O"

def win(b):
    lines = [(0,1,2),(3,4,5),(6,7,8),
             (0,3,6),(1,4,7),(2,5,8),
             (0,4,8),(2,4,6)]
    for a,c,d in lines:
        if b[a] != E and b[a] == b[c] == b[d]:
            return b[a]
    return None

def value(b):
    w = win(b)
    return 1 if w == X else -1 if w == O else 0

def minimax(b, maxp, count):
    count[0] += 1
    if win(b) or E not in b:
        return value(b)

    scores = []
    for i in range(9):
        if b[i] == E:
            b[i] = X if maxp else O
            scores.append(minimax(b, not maxp, count))
            b[i] = E

    return max(scores) if maxp else min(scores)


def alphabeta(b, maxp, alpha, beta, count):
    count[0] += 1
    if win(b) or E not in b:
        return value(b)

    if maxp:
        best = -99
        for i in range(9):
            if b[i] == E:
                b[i] = X
                best = max(best, alphabeta(b, False, alpha, beta, count))
                b[i] = E
                alpha = max(alpha, best)

                if alpha >= beta:
                    print(f"Pruned branch: position {i+1}")
                    print(f"Reason: alpha ({alpha}) >= beta ({beta})")
                    break
        return best

    else:
        best = 99
        for i in range(9):
            if b[i] == E:
                b[i] = O
                best = min(best, alphabeta(b, True, alpha, beta, count))
                b[i] = E
                beta = min(beta, best)

                if alpha >= beta:
                    print(f"Pruned branch: position {i+1}")
                    print(f"Reason: alpha ({alpha}) >= beta ({beta})")
                    break
        return best


# Identical position for both algorithms
board = [X, O, X,
         E, X, O,
         O, E, E]

print("Board:")
print(board[:3])
print(board[3:6])
print(board[6:])

# Plain Minimax
m_count = [0]
m_result = minimax(board, True, m_count)

# Alpha-Beta
a_count = [0]
a_result = alphabeta(board, True, -99, 99, a_count)

print("\n--- Comparison ---")
print("Minimax Result    :", m_result)
print("Minimax Nodes     :", m_count[0])

print("Alpha-Beta Result :", a_result)
print("Alpha-Beta Nodes  :", a_count[0])

print("Result Unchanged  :", m_result == a_result)
print("Nodes Saved       :", m_count[0] - a_count[0])
