#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<pair<char, int>> moves(N);
    for (auto &[direction, steps] : moves) {
        cin >> direction >> steps;
    }

    pair<int, int> position{0, 0};
    map<pair<int, int>, int> visited{{position, 0}};

    int currentTime = 0;
    int maxTime = INT32_MAX;
    for (const auto &[direction, steps] : moves) {
        pair<int, int> delta;
        if (direction == 'N') {
            delta = {0, 1};
        } else if (direction == 'W') {
            delta = {-1, 0};
        } else if (direction == 'E') {
            delta = {1, 0};
        } else if (direction == 'S') {
            delta = {0, -1};
        }

        for (int i = 0; i < steps; i++) {
            position.first += delta.first;
            position.second += delta.second;
            currentTime++;

            if (visited.find(position) != visited.end()) {
                maxTime = min(maxTime, currentTime - visited[position]);
            }
            visited[position] = currentTime;
        }
    }

    cout << (maxTime == INT32_MAX ? -1 : maxTime) << '\n';
    return 0;
}
