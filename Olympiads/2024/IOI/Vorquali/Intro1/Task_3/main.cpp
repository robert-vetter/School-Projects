#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Custom comparator function to sort schools based on the new scoring system
bool compareSchools(const vector<int>& a, const vector<int>& b) {
    for (int i = 0; i < 5; ++i) {
        if (a[i] > b[i]) return true;
        if (a[i] < b[i]) return false;
    }
    return false;
}

int main() {
    int t;
    cin >> t;

    for (int testCase = 1; testCase <= t; ++testCase) {
        int n;
        cin >> n;

        vector<vector<int>> schools(n, vector<int>(5));

        // Read skill levels and sort each team
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < 5; ++j) {
                cin >> schools[i][j];
            }
            sort(schools[i].rbegin(), schools[i].rend());
        }

        // Sort schools based on the new scoring system
        sort(schools.begin(), schools.end(), compareSchools);

        // Output the sorted schools
        cout << "Case #" << testCase << ":\n";
        for (const auto& school : schools) {
            for (const auto& skill : school) {
                cout << skill << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}
