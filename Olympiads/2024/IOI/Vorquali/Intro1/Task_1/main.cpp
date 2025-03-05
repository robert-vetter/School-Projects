#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int l, r;
    cin >> l >> r;

    if (l == 0 && r == 0) {
        cout << "Not a moose" << endl;
        return 0;
    }

    if (l == r) {
        cout << "Even " << 2 * l << endl;
    } else {
        int maxTines = max(l, r);
        cout << "Odd " << 2 * maxTines << endl;
    }

    return 0;
}
