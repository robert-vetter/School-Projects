#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

struct Activity {
    std::string name;
    int fun;
    int len;
};

int maxFun(const std::vector<Activity>& activities, int totalMinutes) {
    std::vector<int> dp(totalMinutes + 1, 0);

    for (const Activity& activity : activities) {
        for (int j = totalMinutes; j >= activity.len; j--) {
            dp[j] = std::max(dp[j], dp[j - activity.len] + activity.fun * activity.len);
        }
    }

    return dp[totalMinutes];
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);
    int t;
    std::cin >> t;

    std::vector<int> results;

    for (int caseNum = 1; caseNum <= t; ++caseNum) {
        int n, m;
        std::cin >> n >> m;

        std::vector<Activity> activities(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> activities[i].name >> activities[i].fun >> activities[i].len;
        }

        results.push_back(maxFun(activities, m * 60));  // m hours converted to minutes
    }

    for (int caseNum = 1; caseNum <= t; ++caseNum) {
        std::cout << "Case #" << caseNum << ": " << results[caseNum - 1] << std::endl;
    }

    return 0;
}


