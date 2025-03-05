#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  vector<int> tune(n);
  for (int i = 0; i < n; ++i) {
    cin >> tune[i];
  }

  double length = 0.0;
  for (int i = 0; i < n; ++i) {
    switch (tune[i]) {
      case 0:
        length += 2.0;
        break;
      case 1:
        length += 1.0;
        break;
      case 2:
        length += 0.5;
        break;
      case 4:
        length += 0.25;
        break;
      case 8:
        length += 0.125;
        break;
      case 16:
        length += 0.0625;
        break;
    }
  }

  cout << fixed << setprecision(6) << length << endl;

  return 0;
}
