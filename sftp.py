import os
import sys
import paramiko
import stat

def remdir(remote_folder, sftp):
        for item in sftp.listdir(remote_folder):
            item_path = os.path.join(remote_folder, item)
            item_attr = sftp.stat(item_path)
            if stat.S_ISDIR(item_attr.st_mode):
                remdir(item_path, sftp)
                try:
                    sftp.remove(item_path)
                except:
                     print(f"no se pudo borrar {item_path}")
                print(f"{item_path} borrado")
            else:
                try:
                    sftp.remove(item_path)
                except:
                     print(f"no se pudo borrar {item_path}")
                print(f"{item_path} borrado")

def upload_repo(source_repo_path, remote_host, remote_port, remote_username, remote_password, remote_folder):
    transport = paramiko.Transport((remote_host, remote_port))
    transport.connect(username=remote_username, password=remote_password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    try:
        sftp.chdir(remote_folder)
    except Exception as e:
        print(f"{str(e)}")
    remdir(remote_folder=remote_folder, sftp=sftp)
                  
    for root, dirs, files in os.walk(source_repo_path):
        for file in files:
            local_path = os.path.join(root, file)
            remote_path = os.path.join(remote_folder, os.path.relpath(local_path, source_repo_path))
            sftp.put(local_path, remote_path)
            print(f"{local_path} movido a {remote_path}")

    sftp.close()
    transport.close()
    print("Upload completo.")

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Uso: python script_name.py source_repo_path remote_host remote_port remote_username remote_password remote_folder")
        sys.exit(1)
        
    source_repo_path = sys.argv[1]
    remote_host = sys.argv[2]
    remote_port = int(sys.argv[3])
    remote_username = sys.argv[4]
    remote_password = sys.argv[5]
    remote_folder = sys.argv[6]
    
    upload_repo(source_repo_path, remote_host, remote_port, remote_username, remote_password, remote_folder)