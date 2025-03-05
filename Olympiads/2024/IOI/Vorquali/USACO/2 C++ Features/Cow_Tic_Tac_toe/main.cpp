#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>

using namespace std;

// Helper function to create a sorted string from a set
string sortedString(unordered_set<char> s) {
    string str(s.begin(), s.end());
    sort(str.begin(), str.end());
    return str;
}

int main() {
    char board[3][3];
    unordered_set<char> individualCows;
    unordered_set<string> teamCows;

    // Read the board
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            cin >> board[i][j];
        }
    }

    // Check for individual cows
    for (int i = 0; i < 3; ++i) {
        // Check rows
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
            individualCows.insert(board[i][0]);
        }

        // Check columns
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i]) {
            individualCows.insert(board[0][i]);
        }
    }

    // Check diagonals for individual cows
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
        individualCows.insert(board[0][0]);
    }
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
        individualCows.insert(board[0][2]);
    }

    // Check for two-cow teams
    for (int i = 0; i < 3; ++i) {
        // Check rows
        unordered_set<char> rowSet = {board[i][0], board[i][1], board[i][2]};
        if (rowSet.size() == 2) {
            string team = sortedString(rowSet);
            teamCows.insert(team);
        }

        // Check columns
        unordered_set<char> colSet = {board[0][i], board[1][i], board[2][i]};
        if (colSet.size() == 2) {
            string team = sortedString(colSet);
            teamCows.insert(team);
        }
    }

    // Check diagonals for two-cow teams
    unordered_set<char> diag1Set = {board[0][0], board[1][1], board[2][2]};
    if (diag1Set.size() == 2) {
        string team = sortedString(diag1Set);
        teamCows.insert(team);
    }
    unordered_set<char> diag2Set = {board[0][2], board[1][1], board[2][0]};
    if (diag2Set.size() == 2) {
        string team = sortedString(diag2Set);
        teamCows.insert(team);
    }

    // Output the results
    cout << individualCows.size() << endl;
    cout << teamCows.size() << endl;

    return 0;
}
