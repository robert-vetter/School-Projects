#include <bits/stdc++.h>

using namespace std;

string reverseString(string s){
    string ans = "";
    for (int i = s.length()-1; i >= 0; i--){
            ans += s[i];

    }
    return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  string s;
  cin >> s;

  string ans = reverseString(s);

  if (s == ans){
    cout << true << endl;
  } else {
    cout << false << endl;
  }



  return 0;
}
