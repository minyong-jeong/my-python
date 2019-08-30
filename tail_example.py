import subprocess

def tail_example(path):
    f = subprocess.Popen(['tail', "-F", path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        line = f.stdout.readline()
        print(line)

if __name__ == "__main__":
    tail_example("/path/to/file")
