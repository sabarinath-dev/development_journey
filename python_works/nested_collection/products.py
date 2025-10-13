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




all_sizes=[size for s in shirts for size in s.get("sizes")]


size_count={size:all_sizes.count(size) for size in all_sizes}

print(size_count)