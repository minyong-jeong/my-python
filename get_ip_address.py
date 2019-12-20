import os

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    result = str(process.read())
    print(result)

get_ip_address("naver.com")