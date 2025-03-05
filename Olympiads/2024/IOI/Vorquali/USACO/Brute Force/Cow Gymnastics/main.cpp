#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int k, n;
  vector<vector<int>> input;

  cin >> k >> n;

  for (int i = 0; i < k; i++) {
    vector<int> temp(n);
    for (int j = 0; j < n; j++) {
      cin >> temp[j];
    }
    input.push_back(temp);
  }

  int countConsistentPairs = 0;

  // Compare each pair (i, j) of cows
  for (int i = 1; i <= n; i++) {
    for (int j = i + 1; j <= n; j++) { // j > i to avoid duplicate pairs
      bool consistent = true;

      // Check each practice session for consistency
      for (int l = 0; l < k; l++) {
        int i_pos = 0, j_pos = 0;

        // Find the positions of i and j in the l-th practice session
        for (int m = 0; m < n; m++) {
          if (input[l][m] == i) {
            i_pos = m;
          }
          if (input[l][m] == j) {
            j_pos = m;
          }
        }

        // Check if pair (i, j) is inconsistent in this practice session
        if ((i_pos < j_pos && input[l][i_pos] != i) || (i_pos > j_pos && input[l][j_pos] != j)) {
          consistent = false;
          break;
        }
      }

      if (consistent) {
        countConsistentPairs++;
      }
    }
  }

  cout << countConsistentPairs << "\n";

  return 0;
}
