from collections import Counter                   # not loaded by default
from collections import defaultdict

def number_of_friends(user): return len(friendships[user["id"]])

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]     # For each of my friends,
        for foaf_id in friendships[friend_id]     # find their friends
        if foaf_id != user_id                     # who aren't me
        and foaf_id not in friendships[user_id]   # and aren't my friends.
    )
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]
friendships = {user["id"]: [] for user in users}
# print(friendships)

user_ids_by_interest = defaultdict(list)
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

for a, b in user_ids_by_interest.items():
    print(a, b)
for a, b in interests_by_user_id.items():
    print(a, b)
# for interest in interests_by_user_id[0]:
#     print(interest)


# print(user_ids_by_interest)
# print(interests_by_user_id)

# for a, b in friendships.items():
#     print(a, b)
total_connections = sum(number_of_friends(user)
                        for user in users)  
# print(total_connections)
num_users = len(users)
avg_connections = total_connections / num_users
# print(avg_connections)

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# print(num_friends_by_id)

num_friends_by_id.sort(key=lambda a: a[1], reverse= True)
# print(num_friends_by_id)

# print(friends_of_friends(users[3])) 
print(most_common_interests_with(users[3])) 