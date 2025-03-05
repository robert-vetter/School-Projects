#include <bits/stdc++.h>

using namespace std;

bool customComparator(const pair<string, int>& a, const pair<string, int>& b) {
    return a.second < b.second;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<pair<string, int>> cows_and_milk(n);
    vector<pair<string, int>> log(7);
    string cowNames[7] = {"Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"};

    for (int i = 0; i < n; i++) {
        cin >> cows_and_milk[i].first >> cows_and_milk[i].second;
    }

    for (int i = 0; i < 7; i++) {
        log[i].first = cowNames[i];
        log[i].second = 0;
    }

    for (int i = 0; i < n; i++) {
        string cow = cows_and_milk[i].first;
        for (int j = 0; j < 7; j++) {
            if (cow == cowNames[j]) {
                log[j].second += cows_and_milk[i].second;
            }
        }
    }

    sort(log.begin(), log.end(), customComparator);

    int m = log[0].second;
    int idx = 1;
    while (idx < 7 && log[idx].second == m) {
        idx++;
    }

    if (idx >= 7) {
        cout << "Tie" << endl;
        return 0;
    }

    int secondSmallest = log[idx].second;
    int secondSmallestIdx = idx;
    idx++;

    while (idx < 7 && log[idx].second == secondSmallest) {
        idx++;
    }

    if (idx < 7 && log[idx].second == secondSmallest) {
        cout << "Tie" << endl;
    } else {
        cout << log[secondSmallestIdx].first << endl;
    }

    return 0;
}
