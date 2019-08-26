import os
import zipfile

def dir_zip(dir_path, dest_path):
    with zipfile.ZipFile(dest_path, "w") as zf:
        for (path, dir, files) in os.walk(dir_path):
            for file in files:
                fullpath = os.path.join(path, file)
                relpath = os.path.relpath(fullpath, dir_path)
                zf.write(fullpath, relpath, zipfile.ZIP_DEFLATED)
        zf.close()

def extract_zip(zip_path, dest_path):
    with zipfile.ZipFile(zip_path) as zf:
        zf.extractall(dest_path)
        zf.close()

if __name__ == "__main__":
    dir_zip('/path/to/dir', '/path/to/<filename>.zip')
    extract_zip('/path/to/zip_file', '/path/to/dir')
