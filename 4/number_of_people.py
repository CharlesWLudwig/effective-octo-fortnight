class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            if i - delay >= 1:
                dp[i] += dp[i - delay]
            if i - forget >= 1:
                dp[i] -= dp[i - forget]
                dp[i] += MOD
                dp[i] %= MOD
            if dp[i] < 0:
                dp[i] += MOD
        
        return sum(dp[-forget:]) % MOD
