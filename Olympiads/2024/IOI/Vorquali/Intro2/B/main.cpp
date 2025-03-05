#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, m;
  cin >> n >> m;

  vector<int> keys(n);
  for (int i = 0; i < n; ++i) {
    cin >> keys[i];
  }

  // Sort the keys
  sort(keys.begin(), keys.end());

  for (int i = 0; i < m; ++i) {
    int y, k;
    cin >> y >> k;

    // Decrypt the message
    int x = y - keys[k - 1];
    cout << x << endl;
  }

  return 0;
}
