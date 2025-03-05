#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool is_possible(const vector<int>& arrival, int M, int C, int max_wait) {
    int buses = 0;
    int next_bus_time = 0;
    int cows_in_current_bus = 0;
    for (int t : arrival) {
        if (next_bus_time <= t || cows_in_current_bus >= C) {
            buses++;
            next_bus_time = t + max_wait;
            cows_in_current_bus = 0;
        }
        cows_in_current_bus++;
    }
    return buses <= M;
}

int main() {
    int N, M, C;
    cin >> N >> M >> C;
    vector<int> arrival(N);
    for (int i = 0; i < N; ++i) {
        cin >> arrival[i];
    }
    sort(arrival.begin(), arrival.end());

    int low = 0, high = arrival.back() - arrival.front();
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (is_possible(arrival, M, C, mid)) {
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    cout << low << '\n';

    return 0;
}
