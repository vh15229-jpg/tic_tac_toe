# Intelligent Tic-Tac-Toe Agent
# Minimax with Alpha-Beta Pruning

E = " "
X, O = "X", "O"


# Check whether a player has won
def win(b):
    lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, c, d in lines:
        if b[a] != E and b[a] == b[c] == b[d]:
            return b[a]

    return None


# Utility function
def value(b):
    w = win(b)

    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


# Plain Minimax
def minimax(b, maxp, count):
    count[0] += 1

    # Terminal state
    if win(b) or E not in b:
        return value(b)

    if maxp:
        best = -99

        for i in range(9):
            if b[i] == E:
                b[i] = X

                score = minimax(b, False, count)

                b[i] = E
                best = max(best, score)

        return best

    else:
        best = 99

        for i in range(9):
            if b[i] == E:
                b[i] = O

                score = minimax(b, True, count)

                b[i] = E
                best = min(best, score)

        return best


# Minimax with Alpha-Beta Pruning
def alphabeta(b, maxp, alpha, beta, count):

    count[0] += 1

    # Terminal state
    if win(b) or E not in b:
        return value(b)

    if maxp:
        best = -99

        for i in range(9):

            if b[i] == E:
                b[i] = X

                score = alphabeta(
                    b, False, alpha, beta, count
                )

                b[i] = E

                best = max(best, score)
                alpha = max(alpha, best)

                # Alpha-Beta pruning
                if alpha >= beta:
                    print(
                        f"Pruned branch: position {i + 1}"
                    )
                    print(
                        f"Reason: alpha ({alpha}) >= "
                        f"beta ({beta})"
                    )
                    break

        return best

    else:
        best = 99

        for i in range(9):

            if b[i] == E:
                b[i] = O

                score = alphabeta(
                    b, True, alpha, beta, count
                )

                b[i] = E

                best = min(best, score)
                beta = min(beta, best)

                # Alpha-Beta pruning
                if alpha >= beta:
                    print(
                        f"Pruned branch: position {i + 1}"
                    )
                    print(
                        f"Reason: alpha ({alpha}) >= "
                        f"beta ({beta})"
                    )
                    break

        return best


# --------------------------------------------------
# Identical board position for both algorithms
# --------------------------------------------------

board = [
    X, O, X,
    E, X, O,
    O, E, E
]

print("===================================")
print("   INTELLIGENT TIC-TAC-TOE AGENT")
print("===================================")

print("\nBoard:")
print(board[0], "|", board[1], "|", board[2])
print("--+---+--")
print(board[3], "|", board[4], "|", board[5])
print("--+---+--")
print(board[6], "|", board[7], "|", board[8])


# --------------------------------------------------
# Plain Minimax
# --------------------------------------------------

m_count = [0]

m_result = minimax(
    board,
    True,
    m_count
)


# --------------------------------------------------
# Alpha-Beta Pruning
# --------------------------------------------------

a_count = [0]

a_result = alphabeta(
    board,
    True,
    -99,
    99,
    a_count
)


# --------------------------------------------------
# Comparison
# --------------------------------------------------

print("\n===================================")
print("          COMPARISON")
print("===================================")

print("Minimax Result      :", m_result)
print("Minimax Nodes       :", m_count[0])

print()

print("Alpha-Beta Result   :", a_result)
print("Alpha-Beta Nodes    :", a_count[0])

print()

print("Result Unchanged    :", m_result == a_result)

print(
    "Nodes Saved         :",
    m_count[0] - a_count[0]
)

if m_count[0] != 0:
    saving = (
        (m_count[0] - a_count[0])
        / m_count[0]
    ) * 100

    print(
        "Search Reduction    :",
        round(saving, 2),
        "%"
    )

print("===================================")
