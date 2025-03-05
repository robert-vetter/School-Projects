#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

int maxDistance = 0;
unordered_map<int, int> nodeFrequency;
vector<vector<int>> maxPaths;

void DFS(vector<int> graph[], int node, int distance, vector<bool>& visited, vector<int>& currentPath, int pathIndex) {
    visited[node] = true;
    currentPath[pathIndex] = node;

    if (distance > maxDistance) {
        maxDistance = distance;
        maxPaths.clear();
        maxPaths.push_back(vector<int>(currentPath.begin(), currentPath.begin() + pathIndex + 1));
    } else if (distance == maxDistance) {
        maxPaths.push_back(vector<int>(currentPath.begin(), currentPath.begin() + pathIndex + 1));
    }

    for (auto neighbor : graph[node]) {
        if (!visited[neighbor]) {
            DFS(graph, neighbor, distance + 1, visited, currentPath, pathIndex + 1);
        }
    }

    visited[node] = false;
}

set<int> findCommonNodes() {
    set<int> commonNodes;
    for (auto& path : maxPaths) {
        for (int node : path) {
            nodeFrequency[node]++;
        }
    }
    for (const auto& [node, count] : nodeFrequency) {
        if (count == maxPaths.size()) {
            commonNodes.insert(node);
        }
    }
    return commonNodes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int n;
    cin >> n;

    vector<int> graph[n + 1];
    vector<bool> visited(n + 1, false);

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> currentPath(n);
    for (int i = 1; i <= n; i++) {
        DFS(graph, i, 0, visited, currentPath, 0);
    }

    cout << maxDistance << endl;

    set<int> commonNodes = findCommonNodes();
    for (int node : commonNodes) {
        cout << node << " ";
    }
    cout << endl;

    return 0;
}
