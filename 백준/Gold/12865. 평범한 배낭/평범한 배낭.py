N, K = map(int, input().split())
wv = [(0,0)]
for i in range(1, N+1):
    w, v = map(int, input().split())
    wv.append((w,v))

dp = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if wv[i][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], wv[i][1], wv[i][1]+dp[i-1][j-wv[i][0]])

print(dp[N][K])