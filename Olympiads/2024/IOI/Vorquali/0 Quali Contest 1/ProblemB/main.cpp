#include <iostream>
#include <vector>
#include <map>
using namespace std;

void removeFrame(vector<string>& image, char frame) {
    for (auto &row : image)
        for (auto &ch : row)
            if (ch == frame) ch = '.';
}

bool isTopFrame(const vector<string>& image, char frame) {
    for (int i = 0; i < image.size(); ++i) {
        for (int j = 0; j < image[i].size(); ++j) {
            if (image[i][j] == frame) {
                // Überprüfe die Kanten des Rahmens
                if (i == 0 || i == image.size() - 1 || j == 0 || j == image[0].size() - 1) return true;
                if (image[i-1][j] != frame || image[i+1][j] != frame || image[i][j-1] != frame || image[i][j+1] != frame) return true;
            }
        }
    }
    return false;
}

string findFrameOrder(vector<string>& image, int n) {
    string order;
    while (order.size() < n) {
        for (char frame = 'A'; frame <= 'Z'; ++frame) {
            if (isTopFrame(image, frame)) {
                order += frame;
                removeFrame(image, frame);
                break;
            }
        }
    }
    return order;
}

int main() {
    int h, b;
    cin >> h >> b;
    vector<string> image(h);
    for (int i = 0; i < h; ++i) cin >> image[i];

    string order = findFrameOrder(image, n);
    cout << order << endl;
    return 0;
}
