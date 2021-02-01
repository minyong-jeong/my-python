def has_unique_chars(string):
    if string is None:
        return False
    return len(set(string)) == len(string)


print(has_unique_chars("ABCD"))

# print(has_unique_chars("ABCD")) --> True
# print(has_unique_chars("ABCDD")) --> False
