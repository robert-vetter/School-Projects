#include <bits/stdc++.h>

using namespace std;

int N;
string S;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;
    cin >> S;

    bool found = false;
    bool last = false;

    int splits = 0;

    for (int i = 0; i < N; i+=2){
        if (S[i] == S[i+1]){
            continue;
        }
        bool type = false;
        if (S[i] == 'H'){
            type = true;
        }
        if (!found){
            found = true;
            last = type;
        } else {
            if (type != last){
                splits++;
            }
            last = type;
        }
    }

    int ans = splits;

    if (last == false){
        ans++;
    }

    cout << ans << endl;





    return 0;
}
