#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<pair<int, int>> tasks(n);

    for (int i = 0; i < n; i++) {
        cin >> tasks[i].first >> tasks[i].second;
    }

    sort(tasks.begin(), tasks.end());

    long long reward = 0;
    long long time = 0;
    for (int i = 0; i < n; i++){
        time += tasks[i].first;
        reward += tasks[i].second - time;
    }

    cout << reward << "\n";

    return 0;
}
