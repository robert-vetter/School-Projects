#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;

  vector<long long> a(n);
  for (int i = 0; i < n; i++) cin >> a[i];

  sort(a.begin(), a.end());

  long long max_val = a[n - 1];

  for (int i = n - 1; i >= 0; i--) {
    for (int j = n - 1; j >= 0; j--) {
      if (a[i] * a[j] <= max_val) break;
      for (int k = n - 1; k >= 0; k--) {
        long long temp = a[i] * a[j] * a[k];
        max_val = max(max_val, temp);
      }
    }
  }

  cout << max_val << endl;
  return 0;
}
