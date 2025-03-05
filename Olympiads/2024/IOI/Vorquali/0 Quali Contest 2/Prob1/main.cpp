#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int pathLength, timeLimit, antCount;
    cin >> pathLength >> timeLimit >> antCount;

    vector<pair<int, char>> antDetails(antCount);
    for (int idx = 0; idx < antCount; ++idx) {
        cin >> antDetails[idx].first >> antDetails[idx].second;
    }

    vector<int> finalPositions;
    for (int idx = 0; idx < antCount; ++idx) {
        int currentPosition = antDetails[idx].first;
        int timeRemaining = timeLimit;

        while (timeRemaining > 0) {
            if (antDetails[idx].second == 'R') {
                int distanceToEdge = pathLength - currentPosition;
                if (timeRemaining <= distanceToEdge) {
                    currentPosition += timeRemaining;
                    timeRemaining = 0;
                } else {
                    currentPosition = pathLength;
                    timeRemaining -= distanceToEdge;
                    antDetails[idx].second = 'L';
                }
            } else {
                int startDistance = currentPosition;
                if (timeRemaining <= startDistance) {
                    currentPosition -= timeRemaining;
                    timeRemaining = 0;
                } else {
                    currentPosition = 0;
                    timeRemaining -= startDistance;
                    antDetails[idx].second = 'R';
                }
            }
        }

        finalPositions.push_back(currentPosition);
    }

    sort(finalPositions.begin(), finalPositions.end());

    for (int idx = 0; idx < antCount; ++idx) {
        cout << finalPositions[idx] << " ";
    }
    cout << endl;

    return 0;
}
