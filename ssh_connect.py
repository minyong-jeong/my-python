import paramiko
from scp import SCPClient

class SSHManager:
    """
    usage:
        >>> import SSHManager
        >>> ssh_manager = SSHManager()
        >>> ssh_manager.create_ssh_client(hostname, username, password)
        >>> ssh_manager.send_command("ls -al")
        >>> ssh_manager.send_file("/path/to/local_file", "/path/to/server_dir")
        >>> ssh_manager.get_file("/path/to/server_file", "/path/to/local_dir")
        ...
        >>> ssh_manager.close_ssh_client()
    """

    def __init__(self):
        pass

    def create_ssh_client(self, hostname, username, password):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname, username=username, password=password)

    def close_ssh_client(self):
        self.ssh_client.close()

    def send_file(self, file_path, server_dir):
        with SCPClient(self.ssh_client.get_transport()) as scp:
            scp.put(file_path, server_dir, preserve_times=True)

    def get_file(self, server_path, local_dir):
        with SCPClient(self.ssh_client.get_transport()) as scp:
            scp.get(server_path, local_dir)

    def send_command(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        exec_out = stdout.readlines()
        print(exec_out)

if __name__ == "__main__":
    ssh_manager = SSHManager()
    ssh_manager.create_ssh_client("hostname", "username", "password")
    ssh_manager.send_file("local_file_path", "server_dir")
    # ssh_manager.get_file('server_file_path', 'lcocal_dir')
    ssh_manager.close_ssh_client()
