// Kommentar

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;

    int a[n];
    int differentValues[n];
    fill(differentValues, differentValues + n, 0);

    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    for (int num : a){
        differentValues[num] += 1;
    }
    int res = 0;
    for (int num : differentValues){
        if (num != 0){
            res++;
        }
    }

    cout << res << endl;


}
