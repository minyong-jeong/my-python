import wget
import math

def bar_custom(current, total, width=80):
    width=30
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d / %d]" % (current / total * 100, percent_bar, current, total)
    return progress

def download(url, out_path="."):
    wget.download(url, out=out_path, bar=bar_custom)

if __name__ == "__main__":
    url = "https://github.com/minyong-jeong/minyong-jeong.github.io/raw/master/images/ryan.jpg"
    paths = ["test1.jpg", "test2.jpg", "test3.jpg"]
    for path in paths:
        print("Downloading %s..." % path)
        download(url, path)
        print("")