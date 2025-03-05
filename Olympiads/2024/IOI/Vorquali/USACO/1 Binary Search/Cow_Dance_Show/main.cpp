#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

bool works(int K, const vector<int>& cows, int Tmax) {
    vector<int> stage(K);
    for(int i = 0; i < K; i++) {
        stage[i] = cows[i];
    }
    for(int i = K; i < cows.size(); i++) {
        sort(stage.begin(), stage.end());
        int finish_time = stage[0];
        if(finish_time + cows[i] > Tmax) {
            return false;
        }
        stage[0] = finish_time + cows[i];
    }
    sort(stage.begin(), stage.end());
    return stage[K - 1] <= Tmax;
}

int main() {
    int N, Tmax;
    cin >> N >> Tmax;
    vector<int> cows(N);
    for(int i = 0; i < N; i++) {
        cin >> cows[i];
    }
    int low = 1, high = N, answer = N;
    while(low <= high) {
        int mid = (low + high) / 2;
        if(works(mid, cows, Tmax)) {
            answer = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    cout << answer << '\n';
    return 0;
}

