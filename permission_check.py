import os

def permission_check(fname):
    read_ok    = "O" if os.access(fname, os.R_OK) else "X"
    write_ok   = "O" if os.access(fname, os.W_OK) else "X"
    execute_ok = "O" if os.access(fname, os.X_OK) else "X"
    print("(r:%s, w:%s, x:%s) %s" % (read_ok, write_ok, execute_ok, fname))

for src_dir, dirs, files in os.walk("/home/jmy/workspace"):
    for fname in files:
        src_file = os.path.join(src_dir, fname)
        permission_check(src_file)
