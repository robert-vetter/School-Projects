#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  cin >> n;

  long long arr[n];

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  sort(arr, arr+n);

  int ans = 1; // at least 1 distinct value exists
  for (int i = 1; i < n; i++) {
    if (arr[i] != arr[i-1]) {
      ans++;
    }
  }

  cout << ans << endl;

  return 0;
}

