#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1e5 + 5;

vector<int> adj[MAXN];
vector<int> topo;
bool visited[MAXN];
bool onStack[MAXN];

bool dfs(int v) {
    visited[v] = true;
    onStack[v] = true;
    for (int u : adj[v]) {
        if (onStack[u]) {
            // Found a cycle
            topo.push_back(u);
            topo.push_back(v);
            return true;
        }
        if (!visited[u] && dfs(u)) {
            topo.push_back(v);
            return true;
        }
    }
    onStack[v] = false;
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, a, b;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
    }

    for (int i = 1; i <= n; ++i) {
        if (!visited[i] && dfs(i)) {
            reverse(topo.begin(), topo.end());
            cout << topo.size() << "\n";
            for (int city : topo) {
                cout << city << " ";
            }
            cout << "\n";
            return 0;
        }
    }

    cout << "IMPOSSIBLE\n";
    return 0;
}
