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
# display malayalam movie names
# display movies with runtime greater than 150
# malayalam movies with runtime greater than 150
# display movies with rating greater than 7.5
# display tamil movies with rating greater than 8
# number of malayalam movies

all_movies = [mov.get("title") for mov in movies]
all_malayalam_movies = [mov.get("title") for mov in movies if mov.get("language") == "Malayalam"]
movies_runtime = [mov.get("title") for mov in movies if mov.get("runtime") >= 150]
mal_movies_runtime = [mov.get("title") for mov in movies if mov.get("runtime") >= 150 and  mov.get("language") == "Malayalam"]
movies_rating = [mov.get("title") for mov in movies if mov.get("rating") >= 7.5]
tamil_movies_rating = [mov.get("title") for mov in movies if mov.get("rating") >= 8 and  mov.get("language") == "Tamil"]
num_mala_movies = sum(1 for mov in movies if mov.get("language") == "Malayalam")


print("All movie names are:" , all_movies)
print("All malayalam movies:" , all_malayalam_movies)
print("Movies with runtime greater than 150:", movies_runtime)
print("Malayalam Movies with runtime greater than 150:" , mal_movies_runtime)
print("Movies with rating greater than 7.5:", movies_rating)
print("Tamil Movies with rating greater than 7.5:", tamil_movies_rating)
print("Total number of malayalam movies:" , num_mala_movies)

