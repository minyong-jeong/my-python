import re

texts = [
    "ABCD",
    "ABCD.",
    "AB123CD"
]

regex = "^[a-zA-Z0-9][a-zA-Z0-9]{1,5}"

for text in texts:
    match = re.fullmatch(regex, text)
    print(f"pass ==> {text}") if match else print(f"fail ==> {text}")
