

tamil_movies = {"Thuppakki" , "Theri" , "Thalaiva" , "Leo" , "Bodyguard"}

malayalam_movies = {"premam" , "Drishyam" , "Bodyguard"}

all_movies = tamil_movies.union(malayalam_movies)

tamil_movies.update(malayalam_movies)

print(tamil_movies)