#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

struct Activity {
    std::string name;
    int fun;
    int len;
};

std::vector<Activity> activities;
std::unordered_map<int, std::unordered_map<int, int>> memo;

int dfs(int index, int remainingTime) {
    if (index == activities.size() || remainingTime == 0) {
        return 0;
    }

    if (memo[index].find(remainingTime) != memo[index].end()) {
        return memo[index][remainingTime];
    }

    // Skip the current activity
    int result = dfs(index + 1, remainingTime);

    // Include the current activity partially or fully
    for (int time = 1; time <= activities[index].len && time <= remainingTime; ++time) {
        result = std::max(result, activities[index].fun * time + dfs(index + 1, remainingTime - time));
    }

    // Save the result in memo
    memo[index][remainingTime] = result;

    return result;
}

int main() {
    int t;
    std::cin >> t;

    std::vector<int> results;

    for (int caseNum = 1; caseNum <= t; ++caseNum) {
        int n, m;
        std::cin >> n >> m;

        activities.resize(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> activities[i].name >> activities[i].fun >> activities[i].len;
        }

        memo.clear();
        results.push_back(dfs(0, m * 60));  // m hours converted to minutes
    }

    for (int caseNum = 1; caseNum <= t; ++caseNum) {
        std::cout << "Case #" << caseNum << ": " << results[caseNum - 1] << std::endl;
    }

    return 0;
}
