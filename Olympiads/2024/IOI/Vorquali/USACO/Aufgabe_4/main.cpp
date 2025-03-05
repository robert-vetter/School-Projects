#include <bits/stdc++.h>
using namespace std;

const int MAX_LEN = 100;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int N, M;
  cin >> N >> M;

  int speed_limit[MAX_LEN];
  int bessie_speed[MAX_LEN];

  int position = 0;
  for (int i = 0; i < N; i++) {
    int length, limit;
    cin >> length >> limit;
    for (int j = 0; j < length; j++) {
      speed_limit[position] = limit;
      position++;
    }
  }

  position = 0;
  for (int i = 0; i < M; i++) {
    int length, speed;
    cin >> length >> speed;
    for (int j = 0; j < length; j++) {
      bessie_speed[position] = speed;
      position++;
    }
  }

  int max_over = 0;
  for (int i = 0; i < MAX_LEN; i++) {
    int over = bessie_speed[i] - speed_limit[i];
    if (over > max_over) {
      max_over = over;
    }
  }

  cout << max_over << '\n';

  return 0;
}
