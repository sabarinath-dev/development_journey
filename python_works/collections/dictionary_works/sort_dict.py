

marks = {"java":75 , "javascript":50 , "asp":80 , "python":60}

# sort this dictionary with respect to value

sorted_list = sorted(marks, key=marks.get , reverse=True)
print(sorted_list)