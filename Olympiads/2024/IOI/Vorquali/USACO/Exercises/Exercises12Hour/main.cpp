#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, s;
    cin >> n;
    vector<int> tower(n, 0);
    for (int i = 0; i < n -1; i++){
        cin >> s;
        if (tower[i] > s){
            tower[i] = s;
        } else {
            tower[i+1] = s;
        }

    }
    int ans = 0;
    for (int i : tower){
        if (i != 0){
            ans += 1;
        }
    }
    cout << ans;




    return 0;
}

