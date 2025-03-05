#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

struct Rahmen
{
    int hoehe, breite;
    char c;
};

vector<tuple<char, int, int, int, int>> findAbmessungen(vector<string> image, set<char> rahmen)
{
    vector<tuple<char, int, int, int, int>> abmessungen;
    for (auto zeichen : rahmen)
    {
        int startZeile = -1;
        int endZeile = -1;
        int startSpalte = -1;
        int endSpalte = -1;
        for (int i = 0; i < image.size(); ++i)
        {
            for (int j = 0; j < image[i].size(); ++j)
            {
                if (image[i][j] == zeichen)
                {
                    if (startZeile == -1)
                    {
                        startZeile = i;
                        endZeile = i;
                        startSpalte = j;
                        endSpalte = j;
                    }
                    else
                    {
                        endZeile = i;
                        endSpalte = j;
                    }
                }
            }
        }
        abmessungen.push_back({zeichen, startZeile, endZeile, startSpalte, endSpalte});
    }
    return abmessungen;
}

// Updated function to check if a frame is completely visible
tuple<bool, int> checkIfComplete(vector<string> image, tuple<char, int, int, int, int> abmessungen)
{
    char zeichen = get<0>(abmessungen);
    int startZeile = get<1>(abmessungen);
    int endZeile = get<2>(abmessungen);
    int startSpalte = get<3>(abmessungen);
    int endSpalte = get<4>(abmessungen);

    int amountJoker = 0;

    for (int i = startZeile; i <= endZeile; ++i) {
        for (int j = startSpalte; j <= endSpalte; ++j) {
            if (image[i][j] != zeichen && image[i][j] != '.') {
                return tuple<bool, int>{false, 0}; // Frame is not completely visible
            }
            if (image[i][j] == '.') {
                amountJoker++;
            }
        }
    }

    return tuple<bool, int>{true, amountJoker};
}

// Updated function to remove a frame from the image
vector<string> removeRahmen(vector<string> image, tuple<char, int, int, int, int> toRemove)
{
    char zeichen = get<0>(toRemove);
    int startZeile = get<1>(toRemove);
    int endZeile = get<2>(toRemove);
    int startSpalte = get<3>(toRemove);
    int endSpalte = get<4>(toRemove);

    for (int i = startZeile; i <= endZeile; ++i) {
        for (int j = startSpalte; j <= endSpalte; ++j) {
            image[i][j] = '.'; // Replace the frame's character with a background
        }
    }
    return image;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    int h, b;
    cin >> h >> b;

    vector<string> image(h);
    for (int i = 0; i < h; ++i)
    {
        cin >> image[i];
    }

    set<char> rahmen;
    for (const auto &row : image)
    {
        for (char c : row)
        {
            if (c != '.')
            {
                rahmen.insert(c);
            }
        }
    }

    vector<tuple<char, int, int, int, int>> abmessungen = findAbmessungen(image, rahmen);
    string result = "";

    while (!abmessungen.empty())
    {
        int completed = -1;
        int amountJoker = 1000000;
        for (int i = 0; i < abmessungen.size(); ++i)
        {
            tuple<bool, int> check = checkIfComplete(image, abmessungen[i]);
            if (get<0>(check) == true)
            {
                if (get<1>(check) < amountJoker)
                {
                    completed = i;
                    amountJoker = get<1>(check);
                }
            }
        }

        if (completed == -1) {
            cerr << "Error: No complete frame found." << endl;
            return 1;
        }

        image = removeRahmen(image, abmessungen[completed]);
        result += get<0>(abmessungen[completed]);
        abmessungen.erase(abmessungen.begin() + completed);
    }
    cout << result << "\n";
}
