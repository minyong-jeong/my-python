import os
import hashlib

def get_file_hash(path):
    f = open(path, 'rb')
    data = f.read()
    hash = hashlib.md5(data).hexdigest()
    return hash

def is_same_file(file1, file2):
    f1_hash = get_file_hash(file1)
    f2_hash = get_file_hash(file2)
    return f1_hash == f2_hash

if __name__ == "__main__":
    file1_path = './make_dir.py'
    file2_path = './README.md'
    same_file = is_same_file(file1_path, file2_path)
    print(same_file)