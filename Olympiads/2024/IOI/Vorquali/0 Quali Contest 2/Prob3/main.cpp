#include <bits/stdc++.h>

using namespace std;

const long long MAX_TIME = 1e18;

struct TravelNode {
    int location;
    int shipPassesLeft;
    int trainPassesLeft;
    long long totalTime;

    TravelNode(int location, int shipPass, int trainPass, long long totalTime)
        : location(location), shipPassesLeft(shipPass), trainPassesLeft(trainPass), totalTime(totalTime) {}

    bool operator<(const TravelNode& other) const {
        return totalTime > other.totalTime;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int nodes, edges, ships, trains, shipTime, trainTime;
    cin >> nodes >> edges >> ships >> trains >> shipTime >> trainTime;

    vector<vector<pair<int, long long>>> network(nodes + 1);
    int start, end;
    long long duration;

    for (int i = 0; i < edges; ++i) {
        cin >> start >> end >> duration;
        network[start].emplace_back(end, duration);
        network[end].emplace_back(start, duration);
    }

    for (int i = 0; i < ships; ++i) {
        cin >> start >> end >> duration;
        network[start].emplace_back(end, -duration);
        network[end].emplace_back(start, -duration);
    }

    for (int i = 0; i < trains; ++i) {
        cin >> start >> end >> duration;
        network[start].emplace_back(end, -duration - 1000000000LL);
        network[end].emplace_back(start, -duration - 1000000000LL);
    }

    vector<vector<vector<long long>>> travelTime(nodes + 1, vector<vector<long long>>(shipTime + 1, vector<long long>(trainTime + 1, MAX_TIME)));
    priority_queue<TravelNode> travelQueue;
    travelQueue.emplace(1, shipTime, trainTime, 0);
    travelTime[1][shipTime][trainTime] = 0;

    while (!travelQueue.empty()) {
        TravelNode current = travelQueue.top();
        travelQueue.pop();

        if (current.location == nodes) {
            cout << current.totalTime << endl;
            return 0;
        }

        for (auto& route : network[current.location]) {
            int nextLocation = route.first;
            long long routeDuration = route.second;
            int remainingShipPasses = current.shipPassesLeft;
            int remainingTrainPasses = current.trainPassesLeft;
            long long newTime = current.totalTime;

            if (routeDuration < 0) {
                if (routeDuration < -1000000000LL) {
                    routeDuration += 1000000000LL;
                    if (remainingTrainPasses > 0) {
                        remainingTrainPasses--;
                    } else {
                        continue;
                    }
                } else {
                    if (remainingShipPasses > 0) {
                        remainingShipPasses--;
                    } else {
                        continue;
                    }
                }
                routeDuration = -routeDuration;
            }

            newTime += routeDuration;

            if (newTime < travelTime[nextLocation][remainingShipPasses][remainingTrainPasses]) {
                travelTime[nextLocation][remainingShipPasses][remainingTrainPasses] = newTime;
                travelQueue.emplace(nextLocation, remainingShipPasses, remainingTrainPasses, newTime);
            }
        }
    }

    cout << -1 << endl;
    return 0;
}
