#include <bits/stdc++.h>

using namespace std;

struct Entry {
    int day;
    string name;
    int change;
};

bool compareByDay(const Entry &a, const Entry &b) {
    return a.day < b.day;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<Entry> entries;

    int n;
    cin >> n;

    unordered_map<string, int> scores;
    unordered_map<string, int> index;

    for (int i = 0; i < n; i++) {
        Entry entry;
        cin >> entry.day >> entry.name >> entry.change;
        entries.push_back(entry);

        if (scores.find(entry.name) == scores.end()) {
            scores[entry.name] = 7; // initial score for each cow
            index[entry.name] = index.size();
        }
    }

    vector<int> score_array(scores.size(), 7); // initial score for each cow
    int changeDisplays = 0;

    sort(entries.begin(), entries.end(), compareByDay);

    set<int> formerScoreHolders;
    for (int i = 0; i < score_array.size(); i++) {
        formerScoreHolders.insert(i);
    }

    for (int i = 0; i < n; i++) {
        score_array[index[entries[i].name]] += entries[i].change;

        int maxScore = *max_element(score_array.begin(), score_array.end());

        set<int> currentScoreHolders;
        for (int j = 0; j < score_array.size(); j++) {
            if (score_array[j] == maxScore) {
                currentScoreHolders.insert(j);
            }
        }

        if (currentScoreHolders != formerScoreHolders) {
            changeDisplays++;
            formerScoreHolders = currentScoreHolders;
        }
    }

    cout << changeDisplays << endl;

    return 0;
}

