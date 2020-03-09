import hashlib

HASH_NAME = "md5"

txt = input("Enter the text to convert: ")

text = txt.encode('utf-8')
md5 = hashlib.new(HASH_NAME)
md5.update(text)
result = md5.hexdigest()

print("="*30)
print("TYPE: %s" % HASH_NAME.upper())
print("TEXT: %s" % txt)
print("HASH: %s" % result)
print("="*30)
