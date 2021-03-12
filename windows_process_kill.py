import subprocess


def process_exists(process_name):
    call = 'TASKLIST /FI imagename eq %s' % process_name
    output = subprocess.check_output(call).decode('euc-kr')
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


def process_kill(process_name):
    call = 'TASKKILL /f /im %s' % process_name
    output = subprocess.check_output(call).decode('euc-kr')
    print(output)


if process_exists("Chrome.exe"):
    process_kill("Chrome.exe")
