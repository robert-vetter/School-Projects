#include <bits/stdc++.h>

using namespace std;

// keine Referenz, String wird kopiert und weiterverarbeitet
void rev(string s){
    reverse(s.begin(), s.end());
}

//mit Referenz (Zeiger auf Speicherort), verändert String auch außerhalb dieser Funktion
void rev(string& s){
    reverse(s.begin(), s.end());
}


int main() {
  // Ergebnis erst in Buffer schreiben, am Ende wird geflusht (Laufzeitreduzierung)
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  // bei Gleitkommazahlen "double" verwenden
  double pi = 3.1415;
  cout << setprecision(6) << fixed << pi;






  return 0;
}


