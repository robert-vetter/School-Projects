#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <string>

using namespace std;

bool compare(const pair<string, pair<int, double>>& a, const pair<string, pair<int, double>>& b) {
    return a.second.second > b.second.second;
}

double max_noms(int n, int m, vector<pair<string, pair<int, double>>> dishes) {
    sort(dishes.begin(), dishes.end(), compare);
    double totalNoms = 0;
    int remainingServings = m;
    for (auto& dish : dishes) {
        int servings = dish.second.first;
        double noms_per_serving = dish.second.second;
        int servings_to_take = min(servings, remainingServings);
        totalNoms += servings_to_take * noms_per_serving;
        remainingServings -= servings_to_take;
        if (remainingServings == 0) {
            break;
        }
    }
    return totalNoms;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<pair<string, pair<int, double>>> dishes;
    for (int i = 0; i < n; ++i) {
        string name;
        int servings;
        double noms;
        cin >> name >> servings >> noms;
        dishes.push_back({name, {servings, noms}});
    }
    cout << fixed << setprecision(6) << max_noms(n, m, dishes) << endl;
    return 0;
}
