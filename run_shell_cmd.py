import subprocess

def run_shell_cmd(cmd):
    cmd_list = cmd.split(' ')
    try:
        sp = subprocess.run(cmd_list, stdout=subprocess.PIPE)
        print(sp.stdout.decode("utf-8"))
        print(sp.returncode)
    except Exception as e:
        print(e)

my_cmd = 'echo shell cmd test!!'
run_shell_cmd(my_cmd)