#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int findCenter(int n, vector<vector<int>>& adj) {
    vector<int> degree(n, 0);
    queue<int> q;

    // Calculate the degree of each node
    for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1) {
            q.push(i);
        }
    }

    while (n > 2) {
        int sz = q.size();
        n -= sz;

        for (int i = 0; i < sz; i++) {
            int u = q.front();
            q.pop();

            for (int v : adj[u]) {
                degree[v]--;
                if (degree[v] == 1) {
                    q.push(v);
                }
            }
        }
    }

    return q.front() + 1;  // +1 because houses are 1-indexed
}

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        int n;
        cin >> n;

        vector<vector<int>> adj(n);
        for (int j = 0; j < n - 1; j++) {
            int u, v;
            cin >> u >> v;
            u--; v--;  // 0-indexing
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        cout << "Case #" << i << ": " << findCenter(n, adj) << endl;
    }

    return 0;
}
