#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> adj[2001]; // Adjacency list for the tree
bool visited[2001]; // Track visited nodes

// This pair will hold two values:
// first - the maximum number when including the current node
// second - the maximum number when excluding the current node
pair<int, int> dfs(int node) {
    visited[node] = true;
    int inc = 1; // Including this node
    int exc = 0; // Excluding this node

    for (int child : adj[node]) {
        if (!visited[child]) {
            auto child_res = dfs(child);
            inc += child_res.second; // If we include this node, we can only add the excluding count of children
            exc += max(child_res.first, child_res.second); // If we exclude this node, we take the max for each child
        }
    }
    return {inc, exc};
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        int n;
        cin >> n;
        // Reset for each test case
        for (int j = 1; j <= n; j++) {
            adj[j].clear();
            visited[j] = false;
        }
        // Read the tree edges
        for (int j = 1; j < n; j++) {
            int x, y;
            cin >> x >> y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }

        auto result = dfs(1); // Assuming 1 is the root of the tree
        cout << "Case #" << i << ": " << max(result.first, result.second) << endl;
    }
    return 0;
}
