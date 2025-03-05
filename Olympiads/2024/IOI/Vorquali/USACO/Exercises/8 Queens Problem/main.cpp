#include <bits/stdc++.h>

using namespace std;

bool attack(pair<int, int> q1, pair<int, int> q2){
    int x1, y1 = q1.first, q2.second;
    int x2, y2 = q2.fist, q2.second;

    if (abs(x1 - x2) == abs(y1 - y2) || x1 == x2 || y1 == y2){
        return true;
    }
    return false;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);




  return 0;
}
