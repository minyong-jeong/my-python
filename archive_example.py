import shutil

def create_archive(filename, archive_format, dir_path):
    shutil.make_archive(filename, archive_format, dir_path)

def extract_archive(filename):
    shutil.unpack_archive(filename)

create_archive("filename", "archive_format", "/path/to/dir")
extract_archive("filename")