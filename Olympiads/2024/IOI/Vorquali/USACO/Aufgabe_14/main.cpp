#include <iostream>
#include <vector>
#include <algorithm>

struct Cow {
    char direction;
    int x, y, stop_time = 0;
};

struct Intersection {
    int i, j;
    int time_i, time_j;
    bool active = true;
};

bool find_earliest_intersection(const Intersection &a, const Intersection &b) {
    return a.time_i < b.time_i;
}

int main() {
    int N;
    std::cin >> N;

    std::vector<Cow> cows(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> cows[i].direction >> cows[i].x >> cows[i].y;
    }

    std::vector<Intersection> intersections;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (i == j || cows[i].direction == cows[j].direction) continue;

            int xi = cows[i].x, yi = cows[i].y, xj = cows[j].x, yj = cows[j].y;
            if (cows[i].direction == 'E') {
                std::swap(xi, yi);
                std::swap(xj, yj);
            }

            if (yi > yj || xi < xj || xi >= xj + yj - yi) continue;

            intersections.push_back({i, j, yj - yi, xi - xj});
        }
    }

    while (!intersections.empty()) {
        auto earliest_it = std::min_element(intersections.begin(), intersections.end(), find_earliest_intersection);
        if (!earliest_it->active) break;

        Intersection &intersection = *earliest_it;
        Cow &cow_i = cows[intersection.i], &cow_j = cows[intersection.j];
        if (cow_i.stop_time == 0 && (cow_j.stop_time == 0 || cow_j.stop_time > intersection.time_j)) {
            cow_i.stop_time = intersection.time_i;
        }

        earliest_it->active = false;
        intersections.erase(earliest_it);
    }

    for (const auto &cow : cows) {
        if (cow.stop_time == 0) {
            std::cout << "Infinity" << std::endl;
        } else {
            std::cout << cow.stop_time << std::endl;
        }
    }

    return 0;
}

