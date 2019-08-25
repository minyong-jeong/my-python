import os
import hashlib

def calc_md5(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        md5 = hashlib.md5(data).hexdigest()
        return str(md5)

def md5_tree(dir):
    md5_tree = {}
    work_dir = os.path.abspath(dir)
    for (dirpath, dirnames, filenames) in os.walk(work_dir):
        for filename in filenames:
            abs_path = dirpath + "/" + filename
            rel_path = abs_path.split(work_dir)[-1].replace("\\", "/")
            md5 = calc_md5(abs_path)
            md5_tree[rel_path] = md5
    return md5_tree

if __name__ == "__main__":
    print(md5_tree('./'))
