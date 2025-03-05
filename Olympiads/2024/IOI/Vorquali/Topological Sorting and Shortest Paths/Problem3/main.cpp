#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t, n, b, h, w;
  cin >> t;

  for (int case_num = 1; case_num <= t; ++case_num) {
    cin >> n >> b >> h >> w;
    int min_cost = INT_MAX;

    for (int i = 0; i < h; ++i) {
      int p;
      cin >> p;

      for (int j = 0; j < w; ++j) {
        int a;
        cin >> a;

        if (a >= n) {
          int cost = n * p;
          min_cost = min(min_cost, cost);
        }
      }
    }

    cout << "Case #" << case_num << ": ";
    if (min_cost <= b) {
      cout << min_cost << '\n';
    } else {
      cout << "stay home" << '\n';
    }
  }

  return 0;
}
