friendships = []

n, m = [int(x) for x in input("").split()]

while not (1 <= n <= 10**5) or not (1 <= m <= 10**6):
    print("Beachte: 1 <= n <= 10^5 und 1 <= m <= 10^6")
    n, m = [int(x) for x in input("").split()]

friend_counts = [0] * n

for i in range(0, m):
    i, j = [int(x) for x in input("").split()]
    while not (0 <= i <= n-1) or not (0 <= j <= n-1):
        print("Beachte: 0 <= i, j <= n-1")
        i, j = [int(x) for x in input("").split()]
    friendships.append([i, j])

    friend_counts[i] += 1
    friend_counts[j] += 1

min_friends = min(friend_counts)


users_with_min_friends = []
for i, count in enumerate(friend_counts):
    if count == min_friends:
        users_with_min_friends.append(i)

sorted_users_with_min_friends = sorted(users_with_min_friends)

output_string = " ".join([str(user) for user in sorted_users_with_min_friends])

print(output_string)
