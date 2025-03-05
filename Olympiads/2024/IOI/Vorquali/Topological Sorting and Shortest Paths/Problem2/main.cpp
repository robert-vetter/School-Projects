#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj, adj_rev;
vector<bool> visited;
vector<int> order, component;
vector<int> points;

void dfs1(int v) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs1(u);
        }
    }
    order.push_back(v);
}

void dfs2(int v, int &sum, unordered_set<int> &cycle_nodes) {
    visited[v] = true;
    component.push_back(v);
    cycle_nodes.insert(v);
    sum += points[v];
    for (int u : adj_rev[v]) {
        if (!visited[u]) {
            dfs2(u, sum, cycle_nodes);
        }
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t, n, m, a, b;
    cin >> t;

    for (int i = 1; i <= t; ++i) {
        cin >> n >> m;

        adj.assign(n, vector<int>());
        adj_rev.assign(n, vector<int>());
        points.resize(n);
        visited.assign(n, false);
        order.clear();

        for (int j = 0; j < n; ++j) {
            cin >> points[j];
        }

        for (int j = 0; j < m; ++j) {
            cin >> a >> b;
            --a; --b;  // 0-based indexing
            adj[a].push_back(b);
            adj_rev[b].push_back(a);
        }

        for (int j = 0; j < n; ++j) {
            if (!visited[j]) {
                dfs1(j);
            }
        }

        visited.assign(n, false);
        int max_points = 0;

        unordered_set<int> cycle_nodes;
        for (int j = n - 1; j >= 0; --j) {
            int v = order[j];
            if (!visited[v]) {
                component.clear();
                int sum = 0;
                cycle_nodes.clear();
                dfs2(v, sum, cycle_nodes);
                if (component.size() == 1) {
                    max_points += sum;
                } else {
                    for (int node : cycle_nodes) {
                        for (int dependent : adj[node]) {
                            if (cycle_nodes.find(dependent) == cycle_nodes.end()) {
                                max_points += points[dependent];
                            }
                        }
                    }
                }
            }
        }

        cout << "Case #" << i << ": " << max_points << '\n';
    }

    return 0;
}




