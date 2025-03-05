#include <iostream>
#include <map>
#include <string>
using namespace std;

const string zodiac[] = {"Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"};

int get_year_index(const string& year) {
    for (int i = 0; i < 12; ++i) {
        if (zodiac[i] == year) {
            return i;
        }
    }
    return -1;
}

int main() {
    int N;
    cin >> N;
    map<string, int> cows;
    cows["Bessie"] = 0;
    for (int i = 0; i < N; ++i) {
        string cow1, born, in, relation, animal, year, from, cow2;
        cin >> cow1 >> born >> in >> relation >> animal >> year >> from >> cow2;
        int index = get_year_index(animal);
        int offset = (relation == "previous" ? -1 : 1);
        while (true) {
            if ((cows[cow2] + index) % 12 == 0) {
                cows[cow1] = cows[cow2] + index;
                break;
            }
            index += offset * 12;
        }
    }
    cout << abs(cows["Elsie"] - cows["Bessie"]) << endl;
    return 0;
}
