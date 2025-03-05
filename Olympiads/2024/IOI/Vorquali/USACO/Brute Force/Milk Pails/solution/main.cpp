#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int x, y, m;

  cin >> x >> y >> m;

  int firstBound = m / x;
  int secondBound = m / y;

  int maxRes = 0;

  for (int i = 0; i <= firstBound; i++){
    for (int j = 0; j <= secondBound; j++){
        int currRes = i * x + j * y;
        if (currRes <= m){
            if (currRes > maxRes){
                maxRes = currRes;
            }
        }

    }
  }

  cout << maxRes << endl;





  return 0;
}
