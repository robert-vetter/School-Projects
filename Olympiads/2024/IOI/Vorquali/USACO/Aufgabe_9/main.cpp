#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  int cows[1000];

  for (int i = 0; i < n; i++){
    cin >> cows[i];
  }

  int minTotalDis = INT_MAX;

  for (int start = 0; start < n; ++start) {
    int currTotalDis = 0;
    for (int i = 0; i < n; ++i) {
      currTotalDis += i * cows[(i + start) % n];
    }
    minTotalDis = min(minTotalDis, currTotalDis);
  }

  cout << minTotalDis << endl;

  return 0;
}
