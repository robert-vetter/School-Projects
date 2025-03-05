#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> cubes(n);
    for (int i = 0; i < n; ++i) {
        cin >> cubes[i];
    }

    vector<vector<int>> towers;
    int intmax = 100000;

    for (int i = 0; i < n; i++) {
        int idx = -1, min_top = intmax;
        for (int j = 0; j < towers.size(); j++) {
            if (towers[j].back() >= cubes[i] && towers[j].back() < min_top) {
                min_top = towers[j].back();
                idx = j;
            }
        }
        if (idx != -1) {
            towers[idx].push_back(cubes[i]);
        } else {
            towers.push_back({cubes[i]});
        }
    }

    cout << towers.size() << endl;

    return 0;
}
