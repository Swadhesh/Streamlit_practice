import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def is_valid(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0
    return False

def solve_n_queens(n):
    board = np.zeros((n, n), dtype=int)
    if not solve_n_queens_util(board, 0):
        return None
    return board

def main():
    st.title("8 Queens Problem Solver")
    n = st.slider("Select the size of the chessboard:", min_value=4, max_value=10, value=8)
    solution = solve_n_queens(n)
    
    if solution is not None:
        fig, ax = plt.subplots()
        
        # Draw chessboard with border lines
        chessboard = np.zeros((n, n), dtype=int)
        chessboard[1::2, ::2] = 1
        chessboard[::2, 1::2] = 1
        ax.matshow(chessboard, cmap="gray_r")
        
        for i in range(n):
            for j in range(n):
                if solution[i][j] == 1:
                    # Surround Q with grey background
                    rect = plt.Rectangle((j - 0.5, i - 0.5), 1, 1, fill=True, color='gray', alpha=0.5)
                    ax.add_patch(rect)
                    ax.text(j, i, "Q", ha="center", va="center", fontsize=20, color="red")
        
        ax.set_xticks([])
        ax.set_yticks([])
        st.pyplot(fig)
    else:
        st.error("No solution found for the selected chessboard size.")

if __name__ == "__main__":
    main()
