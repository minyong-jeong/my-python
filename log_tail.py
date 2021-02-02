import os
import re
import sys
import time


class LogTailTool:
    def __init__(self, filename, interval=1, read_from_begin=False, pattern=None):
        self.filename = filename
        self.interval = interval
        self.read_from_begin = read_from_begin
        self.pattern = pattern

        self.openfile()

    def __iter__(self):
        return self

    # Python 3
    def __next__(self):
        return self.next()

    # Python 2
    def next(self):
        return self.read()

    def openfile(self):
        self.fh = open(self.filename, encoding='UTF8')
        self.curino = os.fstat(self.fh.fileno()).st_ino
        if not self.read_from_begin:
            self.fh.seek(0, os.SEEK_END)

    def is_file_rotated(self):
        return os.stat(self.filename).st_ino != self.curino

    def read(self):
        while True:
            curposition = self.fh.tell()
            line = self.fh.readline()
            if line:
                if self.pattern:
                    if re.search(self.pattern, line):
                        return line.strip()
                else:
                    return line.strip()
            else:
                self.fh.seek(curposition)
                if self.is_file_rotated():
                    self.fh.close()
                    self.openfile()
                time.sleep(self.interval)


if __name__ == "__main__":
    lines = LogTailTool("./temp/sample.log")
    for line in lines:
        print(line)
