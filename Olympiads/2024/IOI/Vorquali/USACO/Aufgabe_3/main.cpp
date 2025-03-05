#include <bits/stdc++.h>
using namespace std;

int main() {
    int M, N, K;
    cin >> M >> N >> K;
    char signal[10][10];
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> signal[i][j];
        }
    }
    for (int i = 0; i < M; i++) {
        for (int r = 0; r < K; r++) {
            for (int j = 0; j < N; j++) {
                for (int c = 0; c < K; c++) {
                    cout << signal[i][j];
                }
            }
            cout << endl;
        }
    }
    return 0;
}
