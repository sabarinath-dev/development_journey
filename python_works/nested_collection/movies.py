movies = [
  {"id": 1, "title": "3 Idiots", "runtime": 171, "director": "Rajkumar Hirani", "rating": 8.4, "genre": "Comedy/Drama", "language": "Hindi"},
  {"id": 2, "title": "Dangal", "runtime": 161, "director": "Nitesh Tiwari", "rating": 8.3, "genre": "Biography/Sports", "language": "Hindi"},
  {"id": 3, "title": "Gully Boy", "runtime": 153, "director": "Zoya Akhtar", "rating": 7.9, "genre": "Musical/Drama", "language": "Hindi"},
  {"id": 4, "title": "Piku", "runtime": 123, "director": "Shoojit Sircar", "rating": 7.6, "genre": "Drama/Comedy", "language": "Hindi"},
  {"id": 5, "title": "Andhadhun", "runtime": 139, "director": "Sriram Raghavan", "rating": 8.2, "genre": "Thriller/Crime", "language": "Hindi"},

  {"id": 6, "title": "Baahubali: The Beginning", "runtime": 159, "director": "S. S. Rajamouli", "rating": 8.0, "genre": "Action/Fantasy", "language": "Telugu"},
  {"id": 7, "title": "Arjun Reddy", "runtime": 182, "director": "Sandeep Reddy Vanga", "rating": 8.1, "genre": "Romance/Drama", "language": "Telugu"},
  {"id": 8, "title": "Jersey", "runtime": 160, "director": "Gowtam Tinnanuri", "rating": 8.5, "genre": "Sports/Drama", "language": "Telugu"},
  {"id": 9, "title": "Eega", "runtime": 145, "director": "S. S. Rajamouli", "rating": 7.7, "genre": "Fantasy/Action", "language": "Telugu"},
  {"id": 10, "title": "Rangasthalam", "runtime": 170, "director": "Sukumar", "rating": 8.4, "genre": "Action/Drama", "language": "Telugu"},

  {"id": 11, "title": "Drishyam", "runtime": 160, "director": "Jeethu Joseph", "rating": 8.3, "genre": "Thriller/Crime", "language": "Malayalam"},
  {"id": 12, "title": "Premam", "runtime": 156, "director": "Alphonse Puthren", "rating": 8.3, "genre": "Romance/Drama", "language": "Malayalam"},
  {"id": 13, "title": "Kumbalangi Nights", "runtime": 135, "director": "Madhu C. Narayanan", "rating": 8.6, "genre": "Drama/Comedy", "language": "Malayalam"},
  {"id": 14, "title": "Bangalore Days", "runtime": 171, "director": "Anjali Menon", "rating": 8.3, "genre": "Romance/Drama", "language": "Malayalam"},
  {"id": 15, "title": "Uyare", "runtime": 125, "director": "Manu Ashokan", "rating": 8.0, "genre": "Drama", "language": "Malayalam"},

  {"id": 16, "title": "Super Deluxe", "runtime": 176, "director": "Thiagarajan Kumararaja", "rating": 8.4, "genre": "Thriller/Drama", "language": "Tamil"},
  {"id": 17, "title": "Kaithi", "runtime": 145, "director": "Lokesh Kanagaraj", "rating": 8.5, "genre": "Action/Thriller", "language": "Tamil"},
  {"id": 18, "title": "Pariyerum Perumal", "runtime": 155, "director": "Mari Selvaraj", "rating": 8.8, "genre": "Drama", "language": "Tamil"},
  {"id": 19, "title": "Vikram", "runtime": 173, "director": "Lokesh Kanagaraj", "rating": 8.3, "genre": "Action/Thriller", "language": "Tamil"},
  {"id": 20, "title": "Soorarai Pottru", "runtime": 153, "director": "Sudha Kongara", "rating": 8.7, "genre": "Biography/Drama", "language": "Tamil"}
]





# display all movie names

# all_movie_names=[m.get("title") for m in movies]
# print(all_movie_names)

# display malayalam movie names

malayalam_movie_names=[m.get("title") for m in movies if m.get("language")=="Malayalam" ]
print(len(malayalam_movie_names))
# movie with runtime > 150

# run_time_filter=[m.get("title") for m in movies if m.get("runtime") > 150]
# print(run_time_filter)
# malayalam movie with runtime > 150
# malayalam_movie_runtime_filter=[m.get("title") for m in movies if m.get("runtime") > 150 and m.get("language")=="Malayalam"]
# display movies with rating > 7.5

rating_filter=[m.get("title") for m in movies if m.get("rating")>7.5 and m.get("language")=="Tamil"]
print(rating_filter)
# display tamil movies with rating >8
# number of malayalam movies
