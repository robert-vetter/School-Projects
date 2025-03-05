#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n, k;

  cin >> n >> k;

  int times[k];

  for (int i = 0; i < k; i++){
    times[i] = 0;
  }

  vector<pair<long long, long long>> movies(n);

    for (int i = 0; i < n; i++) {
        cin >> movies[i].first >> movies[i].second;
    }

    sort(movies.begin(), movies.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return a.second < b.second;
    });

    set<pair<int, int>> available;

    int totalNumMovies = 0;

    for (int i = 0; i < n; i++){
        if (available.size() == 0){
            available.insert({movies[i].second*-1, i});
        } else {
            auto t = available.lower_bound({movies[i].first*-1, -1});
            if (t != available.end()){
                available.erase(t);
                available.insert({movies[i].second*-1, i});
            } else if (t == available.end() && available.size() < k){
                available.insert({movies[i].second*-1, i});
            } else {
                totalNumMovies++;
            }
        }
    }

    cout << n - totalNumMovies << endl;


  return 0;
}
