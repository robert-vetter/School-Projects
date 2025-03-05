#include <bits/stdc++.h>
using namespace std;

bool possible(int n, long long t, long long timeNeeded, long long time[]){
    long long cnt = 0;
    for (int i = 0; i < n; i++){
        cnt += timeNeeded / time[i];
        if(cnt >= t) return true;
    }
    return false;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  long long t;

  cin >> n >> t;

  long long time[n];

  for (int i = 0; i < n; i++){
    cin >> time[i];
  }

  long long low = 1, high = *max_element(time, time + n) * t, ans;

  while (low <= high){
    long long mid = low + (high - low) / 2;
    if (possible(n, t, mid, time)){
        ans = mid;
        high = mid - 1;
    } else {
        low = mid + 1;
    }

  }

  cout << ans << endl;

  return 0;
}

