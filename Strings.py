text = "\"Data Structuring\" is Very Important\n" \
       " for any Programmer who wants to become\n" \
       "a \"Professional\" in the field"

#Lower , Upper Strings
lower_text = text.lower()
upper_text = text.upper()
print(upper_text)
print(lower_text.islower())
print(text.isupper())

# Index Strings
index_text = text[16]
print(index_text)
print(text.index("Programmer"))

# Replace Strings
replace_text = text.replace("Data Structuring", "Problem Solving")
print(replace_text)

# len Strings
print(len(text))
