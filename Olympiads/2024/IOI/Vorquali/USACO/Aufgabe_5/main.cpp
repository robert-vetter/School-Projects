#include <bits/stdc++.h>

using namespace std;


bool inBetween(int y, int min, int max){

    if (y >= min && y <= max){
        return true;
    }
    return false;

}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int x, y;

  cin >> x >> y;
  int mult = 1;
  int dist = 0;

  while (true){
    int newPos = x + mult;
    dist += abs(x - newPos);

    if (!inBetween(y, min(x, newPos), max(x, newPos))){
        dist += abs(x - newPos);
        mult *= -2;
    } else {
        dist -= abs(y-newPos);
        break;
    }
  }

  cout << dist;




  return 0;
}
