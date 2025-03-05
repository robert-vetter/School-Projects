#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <set>

using namespace std;

// Function to apply Dijkstra's algorithm
long long dijkstra(int P, vector<vector<pair<int, int>>>& adj) {
    vector<long long> dist(P, LLONG_MAX);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

    dist[0] = 0;
    pq.push({0, 0});

    while (!pq.empty()) {
        int u = pq.top().second;
        long long d = pq.top().first;
        pq.pop();

        if (d > dist[u]) continue;

        for (auto& p : adj[u]) {
            int v = p.first;
            int weight = p.second;

            if (dist[v] > dist[u] + weight) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }

    return dist[P - 1];
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        int P, T;
        cin >> P >> T;

        vector<vector<pair<int, int>>> adj(P);

        for (int j = 0; j < T; ++j) {
            int pi1, pi2, len;
            cin >> pi1 >> pi2 >> len;
            adj[pi1].push_back({pi2, len});
            adj[pi2].push_back({pi1, len});
        }

        long long shortestPathLength = dijkstra(P, adj);
        cout << "Case #" << i << ": " << 2 * shortestPathLength << endl;
    }

    return 0;
}
