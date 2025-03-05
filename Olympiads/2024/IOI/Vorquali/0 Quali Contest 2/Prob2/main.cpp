#include <bits/stdc++.h>

using namespace std;

bool isReachable(int node, const vector<vector<int>>& network, int nodeCount) {
    vector<bool> checked(nodeCount + 1, false);
    queue<int> nodeQueue;
    nodeQueue.push(node);
    checked[node] = true;
    int visitedNodes = 0;

    while (!nodeQueue.empty()) {
        int currentNode = nodeQueue.front();
        nodeQueue.pop();
        visitedNodes++;

        for (int adjacent : network[currentNode]) {
            if (!checked[adjacent]) {
                checked[adjacent] = true;
                nodeQueue.push(adjacent);
            }
        }
    }

    return visitedNodes == nodeCount;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int nodeCount, edgeCount;
    cin >> nodeCount >> edgeCount;

    vector<vector<int>> network(nodeCount + 1);

    for (int i = 0; i < edgeCount; i++) {
        int fromNode, toNode;
        cin >> fromNode >> toNode;
        network[fromNode].push_back(toNode);
    }

    if (isReachable(1, network, nodeCount)) {
        cout << "1\n";
        return 0;
    }

    for (int i = 2; i <= nodeCount; i++) {
        if (isReachable(i, network, nodeCount)) {
            cout << "-1\n";
            return 0;
        }
    }

    cout << "0\n";
    return 0;
}
