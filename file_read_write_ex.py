f = open("./test.txt", "w")
f.write("TEST")
f.close()


f = open("./test.txt", "r")
text = f.read()
print(text)
f.close()
