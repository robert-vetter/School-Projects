#include <bits/stdc++.h>

using namespace std;

vector<string> topoSort;
unordered_map<string, vector<string>> adj;
unordered_map<string, int> visited;

bool dfs(string node) {
    visited[node] = 1;
    for (const string& neighbor : adj[node]) {
        if (visited[neighbor] == 1) return true;
        if (visited[neighbor] == 0 && dfs(neighbor)) return true;
    }
    visited[node] = 2;
    topoSort.push_back(node);
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    string s1, rel, s2;
    for (int i = 0; i < n; ++i) {
        cin >> s1 >> rel >> s2;
        if (rel == ">") {
            adj[s2].push_back(s1);
        } else {
            adj[s1].push_back(s2);
        }
    }

    for (auto& [node, _] : adj) {
        if (visited[node] == 0 && dfs(node)) {
            cout << "impossible\n";
            return 0;
        }
    }

    cout << "possible\n";
    return 0;
}
