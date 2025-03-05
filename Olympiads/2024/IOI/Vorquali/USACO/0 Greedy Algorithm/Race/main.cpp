#include <bits/stdc++.h>
using namespace std;

int main() {

    int N;
    cin >> N;
    vector<int> positions(N);

    for(int i = 0; i < N; i++) {
        cin >> positions[i];
    }

    sort(positions.begin(), positions.end());

    int max_exploded = 0;
    for(int i = 0; i < N; i++) {
        int leftPointer = i, rightPointer = i, exploded = 0, time = 1;

        while(true) {
            int leftMost = leftPointer, rightMost = rightPointer;

            // Explosion in the left direction
            while(leftPointer > 0 && positions[leftPointer] - positions[leftPointer - 1] <= time) {
                leftPointer--;
            }

            // Explosion in the right direction
            while(rightPointer < N - 1 && positions[rightPointer + 1] - positions[rightPointer] <= time) {
                rightPointer++;
            }

            if(leftPointer == leftMost && rightPointer == rightMost) {
                break;
            }

            time++;
        }
        exploded = rightPointer - leftPointer + 1;
        max_exploded = max(max_exploded, exploded);
    }

    cout << max_exploded << endl;

    return 0;
}

