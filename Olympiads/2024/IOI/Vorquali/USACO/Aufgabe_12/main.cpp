#include <bits/stdc++.h>
using namespace std;

string removeAllSubstrings(string s, string t){
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        result += s[i];
        if (result.size() >= t.size() && result.substr(result.size() - t.size()) == t) {
            result.resize(result.size() - t.size());
        }
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    string s, t;
    cin >> s;
    cin >> t;

    string solution = removeAllSubstrings(s, t);
    cout << solution << endl;

    return 0;
}


