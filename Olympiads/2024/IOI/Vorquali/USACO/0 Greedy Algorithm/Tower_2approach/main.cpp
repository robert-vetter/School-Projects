#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> towerHeights(n);

    for (int i = 0; i < n; i++){
        cin >> towerHeights[i];
    }

    multiset<int> towers; // Speichert die Höhe des obersten Blocks jedes Turms

    for (int i = 0; i < n; i++){
        int currentBlock = towerHeights[i];
        auto it = towers.upper_bound(currentBlock); // Findet den niedrigsten Turm, auf den der aktuelle Block passt

        if (it == towers.end()) { // Wenn kein passender Turm gefunden wurde, erstelle einen neuen Turm
            towers.insert(currentBlock);
        } else { // Wenn ein passender Turm gefunden wurde, aktualisiere die Höhe des obersten Blocks dieses Turms
            towers.erase(it);
            towers.insert(currentBlock);
        }
    }

    cout << towers.size() << endl; // Die Anzahl der Türme ist die Größe des Multisets

    return 0;
}
