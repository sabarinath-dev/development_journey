
shirts = [
  { "id": 1, "title": "Classic White Shirt", "brand": "Allen Solly", "price": 1499, "sizes": ["S", "M", "L", "XL"] },
  { "id": 2, "title": "Slim Fit Denim Shirt", "brand": "Levi's", "price": 2299, "sizes": ["M", "L", "XL"] },
  { "id": 3, "title": "Casual Checked Shirt", "brand": "U.S. Polo Assn.", "price": 1799, "sizes": ["S", "M", "L"] },
  { "id": 4, "title": "Formal Blue Shirt", "brand": "Van Heusen", "price": 1999, "sizes": ["M", "L", "XL", "XXL"] },
  { "id": 5, "title": "Printed Cotton Shirt", "brand": "Flying Machine", "price": 1299, "sizes": ["S", "M", "L"] },
  { "id": 6, "title": "Black Party Shirt", "brand": "Peter England", "price": 1599, "sizes": ["M", "L", "XL"] },
  { "id": 7, "title": "Linen Striped Shirt", "brand": "Raymond", "price": 2499, "sizes": ["S", "M", "L", "XL"] },
  { "id": 8, "title": "Half Sleeve Polo Shirt", "brand": "Tommy Hilfiger", "price": 2699, "sizes": ["M", "L"] },
  { "id": 9, "title": "Checked Flannel Shirt", "brand": "H&M", "price": 1399, "sizes": ["S", "M", "L", "XL"] },
  { "id": 10, "title": "Casual Printed Shirt", "brand": "Zara", "price": 1899, "sizes": ["S", "M", "L", "XL"] }
]

# display all titles of the shirt.
# display all shirt sizes.
# display shirts which the prize are greater than 1500
# display shirts available in size S
# display brands where price greater than 1500 and size not availabe in XL
# display costly shirts
# display size along with count of shirts.


all_shirt_titles = [sh.get("title") for sh in shirts]

all_shirt_sizes = [size for sh in shirts for size in sh.get("sizes")]

size_count = {size : all_shirt_sizes.count(size) for size in all_shirt_sizes}

shirt_1500 = [sh.get("title") for sh in shirts if sh.get("price") >= 1500]

shirts_with_size_s = [sh.get("title") for sh in shirts if "S" in sh.get("sizes")]

shirts_not_xl = [sh.get("title") for sh in shirts if sh.get("price") > 1500 and "XL" not in sh.get("sizes")]

max_shirts = max([sh.get("price") for sh in shirts ])
costly_shirts = [sh.get("title") for sh in shirts if sh.get("price") == max_shirts]



print("All shirt titles:" , all_shirt_titles)
print("All shirt sizes:" , all_shirt_sizes)
print("Size count" , size_count)
print("Shirt with prize greater than 1500:" , shirt_1500)
print("Shirts with size small:" , shirts_with_size_s)
print("Shirts with price greater than 1500 and not having xl:" ,shirts_not_xl)
print("Shirts with costly price:" ,costly_shirts)
