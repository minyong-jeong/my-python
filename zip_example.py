import os
import zipfile

def dir_zip(dir_path, dest_path):
    try:
        if not os.path.isdir(dir_path):
            raise Exception("No such directory: '%s'" % dir_path)

        with zipfile.ZipFile(dest_path, "w") as zf:
            for (path, dir, files) in os.walk(dir_path):
                for file in files:
                    fullpath = os.path.join(path, file)
                    relpath = os.path.relpath(fullpath, dir_path)
                    zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
            zf.close()
    except Exception as e:
        print("[ERROR] >>> %s" % e)
        return False

    return True

def extract_zip(target_zip, dest_path):
    try:
        with zipfile.ZipFile(target_zip) as zf:
            zf.extractall(dest_path)
            zf.close()
    except Exception as e:
        print("[ERROR] >>> %s" % e)
