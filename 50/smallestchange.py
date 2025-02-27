def change(x):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        count += x // coin
        x %= coin
    return count

# Test cases
print(change(1))  # Output: 1
print(change(3))  # Output: 3
print(change(7))  # Output: 3
print(change(32)) # Output: 4