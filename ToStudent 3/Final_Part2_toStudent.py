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

  return user_scores


def recommend_movies(query, users, user_scores):
  # query: a dictionary of watching histories for a specific user
  # users: a dictionary of watching histories for all users
  # user_scores: a dictionary of all user's scores (round 2 decimal points)
  # Return: a list of recommend movies in alphabetically order

  recommend = list()
  
  # fill your code here!
  
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

