#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;

  cin >> n;

  vector<pair<int, int>> times(n);  // Change from times[n] to times(n)

  for (int i = 0; i < n; i++) {
    cin >> times[i].first >> times[i].second;
  }

  sort(times.begin(), times.end());

  int endTime = 0;

  for (int i = 0; i < n; i++) {
    if (times[i].first > endTime) {  // Check if the cow arrives after the previous cow has finished
      endTime = times[i].first;      // Update endTime to the arrival time of the current cow
    }
    endTime += times[i].second;      // Add the questioning time
  }

  cout << endTime << endl;

  return 0;
}
