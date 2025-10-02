

movie = {
    "id" : 1,
    "title" : "KANTHARA",
    "language" : "kannada",
    "runtime" : 120,
    "genre" : "action"
}

for v in movie.values():
    print(v)

print(movie.get("language"))

for k,v in movie.items():
    print(k,v)

# movie["runtime"] = 160
# print(movie)

# movie.update(runtime = 160)
# print(movie)

movie.update(director = "Rishabshetty", runtime = 160)
print(movie)