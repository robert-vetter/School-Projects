#include <iostream>
using namespace std;

int main() {
    int lo = 0, hi = 1e9;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        cout << "Q " << mid << endl << flush;  // Stellt die Frage "n < mid?"
        char response;
        cin >> response;  // Liest die Antwort ein

        if (response == 'y') {
            // Wenn n < mid, aktualisiere hi
            hi = mid;
        } else {
            // Sonst aktualisiere lo
            lo = mid + 1;
        }
    }

    // Sobald lo == hi, haben wir die Antwort gefunden
    cout << "A " << lo << endl << flush;  // Gibt die gefundene Zahl aus
    return 0;
}
