#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int t;
  cin >> t;

  for (int case_num = 1; case_num <= t; ++case_num) {
    int n, m;
    cin >> n >> m;

    vector<vector<pair<int, int>>> graph(n + 1);

    for (int i = 0; i < m; ++i) {
      int vi, wi, ci;
      cin >> vi >> wi >> ci;
      graph[vi].push_back({wi, ci});
      graph[wi].push_back({vi, ci});
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    vector<int> dist(n + 1, INT_MAX);

    pq.push({0, 1});
    dist[1] = 0;

    while (!pq.empty()) {
      int d = pq.top().first;
      int u = pq.top().second;
      pq.pop();

      if (d > dist[u]) continue;

      for (auto &edge : graph[u]) {
        int v = edge.first;
        int w = edge.second;

        if (dist[u] + w < dist[v]) {
          dist[v] = dist[u] + w;
          pq.push({dist[v], v});
        }
      }
    }

    cout << "Case #" << case_num << ": " << dist[n] << "\n";
  }

  return 0;
}
