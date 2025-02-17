def knapsack(items, maxWeight):
    n = len(items)
    dp = [[0 for _ in range(maxWeight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(1, maxWeight + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][maxWeight]

# Example usage
items = [(1, 6), (2, 10), (3, 12)]
maxWeight = 5
print(knapsack(items, maxWeight))  # Output: 22