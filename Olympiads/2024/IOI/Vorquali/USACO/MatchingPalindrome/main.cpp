#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {

    int N;
    cin >> N;

    vector<int> heights(N), sorted_heights(N);
    for (int i = 0; i < N; i++) {
        cin >> heights[i];
        sorted_heights[i] = heights[i];
    }

    // Sort the sorted_heights array
    sort(sorted_heights.begin(), sorted_heights.end());

    // Find the interval where the cows are out of order
    int start = -1, end = -1;
    for (int i = 0; i < N; i++) {
        if (heights[i] != sorted_heights[i]) {
            start = i;
            break;
        }
    }

    for (int i = N - 1; i >= 0; i--) {
        if (heights[i] != sorted_heights[i]) {
            end = i;
            break;
        }
    }

    // Count the number of unique cows between start and end
    int swaps = 0;
    for (int i = start; i <= end; i++) {
        if (heights[i] != heights[i+1] && i != end) {
            swaps++;
        }
    }

    cout << swaps << endl;

    return 0;
}


