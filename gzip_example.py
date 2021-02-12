import gzip

# compress
with open("./temp/text.txt", "rb") as f_in:
    with gzip.open("./temp/text.txt.gz", "wb") as f_out:
        f_out.writelines(f_in)

# decompress
with gzip.open("./temp/text.txt.gz", "rb") as f:
    content = f.read()
    print(content)
