#include <bits/stdc++.h>

using namespace std;

vector<int> adj[100001]; // Increase size by 1 for 1-indexing
vector<int> topo;
bool visited[100001]; // Increase size by 1 for 1-indexing
int ways[100001]; // Change to simple array

void dfs(int u){
    visited[u] = true;
    for (int v : adj[u]){
        if (!visited[v]){
            dfs(v);
        }
    }
    topo.push_back(u);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++){ // Loop m times for edges
        int a, b;
        cin >> a >> b; // Read values of a and b
        adj[a].push_back(b);
    }

    for (int i = 1; i <= n; i++){ // Start from 1
        if(!visited[i]){
            dfs(i);
        }
    }

    reverse(begin(topo), end(topo));

    ways[1] = 1; // Initialize starting level with 1 way

    for (int node : topo){
        for (int neigh : adj[node]){
            ways[neigh] += ways[node];
        }
    }

    cout << ways[n] << endl;

    return 0;
}
