
# 8-Queens Problem using Backtracking

def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueen(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_nqueen(board, row + 1, n):
                return True

            # Backtracking
            board[row][col] = 0

    return False


# Main program
n = 8
#if asked about user input 'n'
#n = int(input("Enter number of queens: "))

board = [[0 for j in range(n)] for i in range(n)]

# Place first queen
first_col = int(input("Enter column for first queen (1 to 8): ")) - 1

if first_col < 0 or first_col >= n:
    print("Invalid input")

else:
    board[0][first_col] = 1

    if solve_nqueen(board, 1, n):
        print("\n8-Queens Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists for this first queen position.")


""" 8-Queens Problem using Backtracking

#include <iostream>
using namespace std;

const int N = 8;
int board[N][N];

bool isSafe(int row, int col, int n) {

    // Check column
    for (int i = 0; i < row; i++) {
        if (board[i][col] == 1)
            return false;
    }

    // Check left diagonal
    int i = row - 1;
    int j = col - 1;

    while (i >= 0 && j >= 0) {
        if (board[i][j] == 1)
            return false;
        i--;
        j--;
    }

    // Check right diagonal
    i = row - 1;
    j = col + 1;

    while (i >= 0 && j < n) {
        if (board[i][j] == 1)
            return false;
        i--;
        j++;
    }

    return true;
}

bool solveNQueen(int row, int n) {

    if (row == n)
        return true;

    for (int col = 0; col < n; col++) {

        if (isSafe(row, col, n)) {
            board[row][col] = 1;

            if (solveNQueen(row + 1, n))
                return true;

            // Backtracking
            board[row][col] = 0;
        }
    }

    return false;
}

int main() {

    int n = 8;
    // If asked about user input 'n':
    // cout << "Enter number of queens: ";
    // cin >> n;
    // (Also change N above to a bigger value, e.g. const int N = 20;)

    // Board is all 0 at the start (global arrays are auto-initialized to 0)

    // Place first queen
    int firstCol;
    cout << "Enter column for first queen (1 to 8): ";
    cin >> firstCol;
    firstCol--;

    if (firstCol < 0 || firstCol >= n) {
        cout << "Invalid input" << endl;
    }
    else {
        board[0][firstCol] = 1;

        if (solveNQueen(1, n)) {
            cout << "\n8-Queens Solution:" << endl;
            for (int i = 0; i < n; i++) {
                cout << "[";
                for (int j = 0; j < n; j++) {
                    cout << board[i][j];
                    if (j < n - 1)
                        cout << ", ";
                }
                cout << "]" << endl;
            }
        }
        else {
            cout << "No solution exists for this first queen position." << endl;
        }
    }

    return 0;
}
"""