#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);


    string crossings;
	cin >> crossings;

	int crossing_pairs = 0;
	// Iterate through all characters of the string
	for (int a = 0; a < crossings.size(); a++) {
		for (int b = a + 1; b < crossings.size(); b++) {
			for (int c = b + 1; c < crossings.size(); c++) {
				for (int d = c + 1; d < crossings.size(); d++) {

					crossing_pairs += (crossings[a] == crossings[c] &&
					                   crossings[b] == crossings[d]);
				}
			}
		}
	}

	cout << crossing_pairs << endl;


  return 0;
}
