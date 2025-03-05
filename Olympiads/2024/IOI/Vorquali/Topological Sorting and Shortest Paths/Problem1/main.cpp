#include <bits/stdc++.h>

using namespace std;

const int INF = 1e9;

vector<int> dijkstra(int source, const vector<vector<pair<int, int>>>& adj) {
    int n = adj.size();
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, source});
    dist[source] = 0;

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (d > dist[u]) continue;

        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;

    for (int test_case = 1; test_case <= t; ++test_case) {
        int n, m;
        cin >> n >> m;

        vector<vector<pair<int, int>>> adj(n);

        for (int i = 0; i < m; ++i) {
            int a, b, w;
            cin >> a >> b >> w;
            --a; --b;
            adj[a].push_back({b, w});
            adj[b].push_back({a, w});
        }

        long long total_distance = 0;

        for (int i = 0; i < n; ++i) {
            vector<int> dist = dijkstra(i, adj);
            for (int d : dist) {
                total_distance += d;
            }
        }

        cout << "Case #" << test_case << ": " << 2 * total_distance << "\n";
    }

    return 0;
}

