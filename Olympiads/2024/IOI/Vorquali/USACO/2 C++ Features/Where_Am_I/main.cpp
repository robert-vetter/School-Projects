#include <bits/stdc++.h>

using namespace std;

bool appearsMoreThanOnce(string uniqueSequence, string mailboxSequence){
    int occurrences = 0;
    std::string::size_type pos = 0;

    while ((pos = mailboxSequence.find(uniqueSequence, pos )) != std::string::npos) {
        occurrences++;
        pos += 1;  // Aktualisierung der Position um 1, nicht um die Länge der Unterzeichenfolge
    }

    if (occurrences > 1){
        return true;
    } else {
        return false;
    }

}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);

  int n;
  string mailboxSequence;

  cin >> n;
  cin >> mailboxSequence;

  for (int length = 1; length <= n; length++){
    bool unique = true;  // Annahme, dass die aktuelle Länge eindeutig ist

    for (int i = 0; i + length <= n; i++){
        string sub = mailboxSequence.substr(i, length);
        if (appearsMoreThanOnce(sub, mailboxSequence)){
            unique = false;  // Die aktuelle Länge ist nicht eindeutig
            break;
        }
    }

    if (unique){  // Wenn die aktuelle Länge eindeutig ist, geben Sie die Antwort aus und beenden Sie das Programm
        cout << length << endl;
        break;
    }
  }

  return 0;
}

