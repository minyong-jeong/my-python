import os

def nslookup(url):
    lines = os.popen('nslookup ' + url).read().split("\n")[:-2]
    print("="*40)
    print('{:^40}'.format(url))
    print("-"*40)
    for line in lines:
        print(line)
    print("="*40 + "\n")

if __name__ == "__main__":
    url_list = [
        'www.google.com'
    ]

    for url in url_list:
        nslookup(url)
