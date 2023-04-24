# load users' watching info
users = dict()
users["Pop"] = {"minion", "spiderman"}
users["Tim"] = {"ju-on", "minion"}
users["Pun"] = {"minion"}
users["Puk"] = {"avenger", "batman", "spiderman"}
users["Tan"] = {"spiderman"}


def calculate_user_scores(query, users):
    # query: a dictionary of watching histories for a specific user
    # users: a dictionary of watching histories for all users
    # Return: a dictionary of all user's scores (round 2 decimal points)

    user_scores = dict()

    # fill your code here!
    query = [movie.lower() for movie in query]

    for user in users:
        count = 0
        for movie in query:
            if (movie in users[user]):
                users[user].remove(movie)
                count += 1

        if (users[user]):
            user_scores[user] = round(
                count / (len(users[user]) + len(query)), 2)
        else:
            user_scores[user] = 0.0

    users["Pop"] = {"minion", "spiderman"}
    users["Tim"] = {"ju-on", "minion"}
    users["Pun"] = {"minion"}
    users["Puk"] = {"avenger", "batman", "spiderman"}
    users["Tan"] = {"spiderman"}

    return user_scores


def recommend_movies(query, users, user_scores):
    # query: a dictionary of watching histories for a specific user
    # users: a dictionary of watching histories for all users
    # user_scores: a dictionary of all user's scores (round 2 decimal points)
    # Return: a list of recommend movies in alphabetically order

    recommend = list()

    # fill your code here!
    query = [movie.lower() for movie in query]
    movies = set([item for sublist in [
        list(movie) for movie in users.values()] for item in sublist])

    movie_exist = False

    for query_movie in query:
        if (query_movie in movies):
            movie_exist = True
            break

    if (query and movie_exist):
        max_point = max(user_scores.values())
        for user in user_scores:
            if (user_scores[user] == max_point):
                recommend.extend(users[user])
        recommend = sorted(list(set(recommend) - set(query)))
    else:
        recommend = "No recommendation"

    return recommend


def main():
    n = int(input())
    query = set()
    for i in range(n):
        query.add(input().lower())

    user_scores = calculate_user_scores(query, users)
    print(user_scores)
    recommend = recommend_movies(query, users, user_scores)
    print(recommend)


main()
