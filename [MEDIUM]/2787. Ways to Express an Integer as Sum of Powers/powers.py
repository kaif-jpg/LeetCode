#280 ms Beats 88.37%

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1000000007
        powers = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[ s - p]) % MOD
                
        return dp[n]