#include <iostream>
#include <algorithm>

const int MAXN = 2005;
const long long INF = 1e18;

long long dp[MAXN];

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int n, C;
    scanf("%d %d", &n, &C);

    std::fill(dp, dp + MAXN, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        int a, b, p;
        scanf("%d %d %d", &a, &b, &p);

        for (int j = 1; j <= b; ++j) {
            int max_k_updated = 0;
            for (int k = C; k >= a; --k) {
                if (dp[k] > dp[k - a] + p) {
                    dp[k] = dp[k - a] + p;
                    max_k_updated = k;
                }
            }
            // If no updates in this iteration, break
            if (max_k_updated == 0) break;
        }
    }

    if (dp[C] == INF) {
        printf("-1\n");
    } else {
        printf("%lld\n", dp[C]);
    }

    return 0;
}
