#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  // Keywords
  vector<int> v1 = {1, 2, 3};
  int frontV = v1.front(); // 1
  int middle = v1[1]; // 2
  int endV = v1.back(); // in diesem Fall 3
  int sizeV = v1.size(); // in diesem Fall 3
  // add element
  v1.push_back(4);
  v1.pop_back(); // returns last element of vector and removes it
  v1.insert(v1.begin(), 5); //inserts 5 at beginning
  v1.insert(v1.begin()+1, 5); //inserts element between elements 1 and 2
  v1.erase(v1.begin()); //löscht erstes Element

  for (int i = 0; i < v1.size(); i++){
    cout << v1[i] << endl;
  }


  // Vector of vectors
  vector<vector<int>> stuff;
  for (int i = 0; i < 3; i++){
    vector<int> temp;
    for (int j = 0; j < 3; j++){
        temp.push_back(i);
    }

    stuff.push_back(temp);
  }

  for (int i = 0; i < stuff.size(); i++){
    for (int j = 0; j < stuff[i].size(); j++){
        cout << stuff[i][j];
    }
    cout << endl;
  }


  return 0;
}
