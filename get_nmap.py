import os

def get_nmap(options, ip):
    command = "nmap " + options + " " + ip
    process = os.popen(command)
    result = str(process.read())
    return result

print(get_nmap('-F', "127.0.0.1"))