import os

def make_dir(path):
    try:
        os.makedirs(path)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    make_dir("./temp")

