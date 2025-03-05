#include <bits/stdc++.h>

using namespace std;

// Function to calculate the total distance of a given route
int calculateDistance(vector<vector<int>> &dist, vector<int> &route) {
    int totalDistance = 0;
    for (int i = 0; i < route.size() - 1; ++i) {
        totalDistance += dist[route[i]][route[i + 1]];
    }
    totalDistance += dist[route.back()][route[0]]; // Return to the starting city
    return totalDistance;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    for (int testCase = 1; testCase <= t; ++testCase) {
        int n;
        cin >> n;

        vector<vector<int>> dist(n, vector<int>(n));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> dist[i][j];
            }
        }

        // Generate the initial route (1, 2, ..., n)
        vector<int> route(n);
        iota(route.begin(), route.end(), 0);

        int minDistance = INT_MAX;
        vector<int> bestRoute;

        // Brute-force through all permutations
        do {
            int currentDistance = calculateDistance(dist, route);
            if (currentDistance < minDistance) {
                minDistance = currentDistance;
                bestRoute = route;
            }
        } while (next_permutation(route.begin(), route.end()));

        // Output the best route
        cout << "Case #" << testCase << ": ";
        for (int i = 0; i < bestRoute.size(); ++i) {
            cout << bestRoute[i] + 1; // Cities are 1-indexed in the output
            if (i < bestRoute.size() - 1) {
                cout << " ";
            }
        }
        cout << endl;
    }

    return 0;
}
