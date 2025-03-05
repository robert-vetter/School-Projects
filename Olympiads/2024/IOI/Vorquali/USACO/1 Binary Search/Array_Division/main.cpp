#include <bits/stdc++.h>
using namespace std;

bool isPossible(int arr[], int n, int k, long long max_sum) {
    int partitions = 1;
    long long current_sum = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] > max_sum) return false;
        if (current_sum + arr[i] > max_sum) {
            partitions++;
            current_sum = arr[i]; // Reset current_sum to arr[i] for the new partition
            if (partitions > k) return false; // Check if the number of partitions exceeds k
        } else {
            current_sum += arr[i];
        }
    }
    return partitions <= k;
}


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;
  cin >> n >> k;

  int arr[n];

  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }

  long long low = *max_element(arr, arr + n), high = accumulate(arr, arr + n, 0LL), ans = high;

  while (low <= high) {
    long long mid = low + (high - low) / 2;
    if (isPossible(arr, n, k, mid)) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  cout << ans << '\n';

  return 0;
}
