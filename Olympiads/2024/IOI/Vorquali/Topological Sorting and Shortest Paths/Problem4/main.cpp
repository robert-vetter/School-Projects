#include <bits/stdc++.h>

using namespace std;

bool isBipartite(vector<vector<int>> &adj, int n) {
    vector<int> color(n, -1);
    for (int start = 0; start < n; ++start) {
        if (color[start] == -1) {
            queue<int> q;
            q.push(start);
            color[start] = 0;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (int v : adj[u]) {
                    if (color[v] == -1) {
                        color[v] = 1 - color[u];
                        q.push(v);
                    } else if (color[v] == color[u]) {
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t, n, m, a, b;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> m;
        vector<vector<int>> adj(n);
        for (int j = 0; j < m; ++j) {
            cin >> a >> b;
            adj[a-1].push_back(b-1);
            adj[b-1].push_back(a-1);
        }
        cout << "Case #" << i << ": " << (isBipartite(adj, n) ? "yes" : "no") << '\n';
    }

    return 0;
}
