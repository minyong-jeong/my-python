import subprocess

def process_exists_check(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode('euc-kr')
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())

print(process_exists_check("chrome.exe"))
