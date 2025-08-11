class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 1000000007
        p = []
        b = 0
        while n > 0:
            if n & 1:
                p.append(1 << b)
            n >>= 1
            b += 1

        pr = []
        run = 1
        for v in p:
            run = (run * v) % MOD
            pr.append(run)
        
        def mod(x: int) -> int:
            return pow(x, MOD - 2, MOD)
        
        ans = []
        for l, r in queries:
            if l == 0:
                ans.append(pr[r])
            else:
                left_prod = pr[l - 1]
                segment = (pr[r] * mod(left_prod)) % MOD
                ans.append(segment)
        return ans