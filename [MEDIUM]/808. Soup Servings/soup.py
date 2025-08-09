#46 ms Beats 14.19%

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
            
        m = ceil(n / 25)
        dp = [[0.0] * (m + 1) for _ in range(m + 1)]

        dp[0][0] = 0.5
        for j in range(1, m + 1):
            dp[0][j] = 1.0

        for i in range(1, m + 1):
            for j in range(1, m + 1):
                dp[i][j] = 0.25 * (
                    dp[max(i - 4, 0)][j] +
                    dp[max(i - 3, 0)][max(j - 1, 0)] +
                    dp[max(i - 2, 0)][max(j - 2, 0)] +
                    dp[max(i - 1, 0)][max(j - 3, 0)]
                )
        return dp[m][m]