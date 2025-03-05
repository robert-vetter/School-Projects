#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<pair<string, string>> cities(n);

    for (int i = 0; i < n; i++) {
        cin >> cities[i].first >> cities[i].second;
    }

    map<pair<string, string>, int> specialPairs;

    for (int i = 0; i < n; i++) {
        string cityName = cities[i].first;
        string stateCode = cities[i].second;

        string cityLetters = cityName.substr(0, 2);

        if (cityLetters != stateCode) {  // Avoid pairing cities with their own state
            specialPairs[{cityLetters, stateCode}]++;
        }
    }

    int ans = 0;

    for (int i = 0; i < n; i++) {
        string cityName = cities[i].first;
        string stateCode = cities[i].second;

        string cityLetters = cityName.substr(0, 2);

        if (specialPairs.count({stateCode, cityLetters})) {
            ans += specialPairs[{stateCode, cityLetters}];
            if (cityLetters == stateCode) {
                ans -= specialPairs[{cityLetters, stateCode}];
            }
        }
    }

    cout << ans / 2 << endl;

    return 0;

}
