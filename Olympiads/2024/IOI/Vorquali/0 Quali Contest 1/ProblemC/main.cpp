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
        // für jede Zeile
        for (int i = 0; i < image.size(); ++i)
        {
            // für jede Spalte
            for (int j = 0; j < image[i].size(); ++j)
            {
                // wenn das Zeichen gefunden wurde
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

tuple<bool, int> checkIfComplete(vector<string> image, tuple<char, int, int, int, int> abmessungen)
{
    char zeichen = get<0>(abmessungen);
    int startZeile = get<1>(abmessungen);
    int endZeile = get<2>(abmessungen);
    int startSpalte = get<3>(abmessungen);
    int endSpalte = get<4>(abmessungen);

    int amountJoker = 0;

    for (int j = startSpalte; j <= endSpalte; ++j)
    {
        if (image[startZeile][j] == '#')
        {
            amountJoker++;
            continue;
        }
        if (image[endZeile][j] == '#')
        {
            amountJoker++;
            continue;
        }
        if (image[startZeile][j] != zeichen)
        {
            return tuple<bool, int>{false, 0};
        }
        if (image[endZeile][j] != zeichen)
        {
            return tuple<bool, int>{false, 0};
        }
    }
    for (int i = startZeile; i <= endZeile; ++i)
    {
        if (image[i][startSpalte] == '#')
        {
            amountJoker++;
            continue;
        }
        if (image[i][endSpalte] == '#')
        {
            amountJoker++;
            continue;
        }
        if (image[i][startSpalte] != zeichen)
        {
            return tuple<bool, int>{false, 0};
        }
        if (image[i][endSpalte] != zeichen)
        {
            return tuple<bool, int>{false, 0};
        }
    }
    return tuple<bool, int>{true, amountJoker};
}

vector<string> removeRahmen(vector<string> image, vector<tuple<char, int, int, int, int>> abmessungen, tuple<char, int, int, int, int> toRemove)
{
    char zeichen = get<0>(toRemove);
    int startZeile = get<1>(toRemove);
    int endZeile = get<2>(toRemove);
    int startSpalte = get<3>(toRemove);
    int endSpalte = get<4>(toRemove);

    for (int j = startSpalte; j <= endSpalte; ++j)
    {
        image[startZeile][j] = '#';
        image[endZeile][j] = '#';
    }
    for (int i = startZeile; i <= endZeile; ++i)
    {
        image[i][startSpalte] = '#';
        image[i][endSpalte] = '#';
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

    int completed;
    int amountJoker;

    while (!abmessungen.empty()) {
        int minJoker = INT_MAX;
        int frameToRemove = -1;

        for (int i = 0; i < abmessungen.size(); ++i) {
            auto checkResult = checkIfComplete(image, abmessungen[i]);
            if (get<0>(checkResult)) {
                int jokerCount = get<1>(checkResult);
                if (jokerCount < minJoker) {
                    minJoker = jokerCount;
                    frameToRemove = i;
                }
            }
        }

        if (frameToRemove == -1) {
            cout << "Error: No removable frame found." << endl;
            break;
        }

        image = removeRahmen(image, abmessungen, abmessungen[frameToRemove]);
        result += get<0>(abmessungen[frameToRemove]);
        abmessungen.erase(abmessungen.begin() + frameToRemove);
    }

    cout << result << "\n";
    return 0;
}
