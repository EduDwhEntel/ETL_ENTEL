import os
import sys
import paramiko

def move_repository_to_sftp(source_repo_path, remote_host, remote_port, remote_username, remote_password, remote_folder):
    transport = paramiko.Transport((remote_host, remote_port))
    transport.connect(username=remote_username, password=remote_password)
    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.chdir(remote_folder)
    for root, dirs, files in os.walk(source_repo_path):
        for file in files:
            local_path = os.path.join(root, file)
            remote_path = os.path.join(remote_folder, os.path.relpath(local_path, source_repo_path))
            sftp.put(local_path, remote_path)
            print(f"Uploaded {local_path} to {remote_path}")

    sftp.close()
    transport.close()
    print("Repository moved successfully to remote folder.")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python script_name.py source_repo_path remote_host remote_port remote_username remote_password remote_folder")
        sys.exit(1)
        
    source_repo_path = sys.argv[1]
    remote_host = sys.argv[2]
    remote_port = int(sys.argv[3])
    remote_username = sys.argv[4]
    remote_password = sys.argv[5]
    remote_folder = sys.argv[6]
    
    move_repository_to_sftp(source_repo_path, remote_host, remote_port, remote_username, remote_password, remote_folder)

    #jejejeje