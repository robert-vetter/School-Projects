#include <bits/stdc++.h>

using namespace std;

bool works(int positionsHay[], int n, int mid) {
    vector<bool> detonated(n, false);
    for (int i = 0; i < n; i++) {
        if (detonated[i]) continue;
        int r = mid;
        int left = i;
        while (left > 0 && positionsHay[left] - positionsHay[left - 1] <= r) {
            left--;
            r--;
        }
        int right = i;
        r = mid;
        while (right < n - 1 && positionsHay[right + 1] - positionsHay[right] <= r) {
            right++;
            r--;
        }
        for (int j = left; j <= right; j++) {
            detonated[j] = true;
        }
    }
    return all_of(detonated.begin(), detonated.end(), [](bool v) { return v; });
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    int positionsHay[n];
    for (int i = 0; i < n; i++) {
        cin >> positionsHay[i];
    }
    sort(positionsHay, positionsHay + n);

    int low = 0, high = positionsHay[n - 1] - positionsHay[0];
    double ans = high;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (works(positionsHay, n, mid)) {
            ans = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    cout << fixed << setprecision(1) << ans * 0.5 << endl;
    return 0;
}
