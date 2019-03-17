import os
import hashlib

def get_dir_hash(path):
    if not os.path.isdir(path):
        print("not dir path. plz retry..")
        return {}
    hash_dict = {}
    dir_tour(path, path, hash_dict)
    return hash_dict
    
def dir_tour(ori_path, path, hash_dict):
    for item in os.listdir(path):
        ipath = path+"/"+item
        if os.path.isfile(ipath):
            lpath = ipath.replace(ori_path+"/", "")
            hash_dict[lpath] = get_file_hash(ipath)
        elif os.path.isdir(ipath):
            dir_tour(ori_path, ipath, hash_dict)

def get_file_hash(path):
    f = open(path, 'rb')
    data = f.read()
    hash = hashlib.md5(data).hexdigest()
    return hash

if __name__ == "__main__":
    hash_dict = get_dir_hash("/Users/minyong/Desktop/workspace/minyong-jeong.github.io")
    print(hash_dict)