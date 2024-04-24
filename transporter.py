import os
import paramiko
import stat

def descarga_rec(remote_path, local_path, sftp):
            files = sftp.listdir_attr(remote_path)
            for file_attr in files:
                file_name = file_attr.filename
                file_mode = file_attr.st_mode
                if stat.S_ISDIR(file_mode):
                    new_remote_path = remote_path + '/' + file_name
                    new_local_path = local_path + '/' + file_name
                    os.makedirs(new_local_path, exist_ok=True)
                    descarga_rec(new_remote_path, new_local_path, sftp=sftp)
                else:
                    remote_file_path = remote_path + '/' + file_name
                    local_file_path = local_path + '/' + file_name
                    sftp.get(remote_file_path, local_file_path)
                    print(f"Downloaded {file_name} successfully.")

def descarga(hostname, username, password, remote_path, local_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, username=username, password=password)        
        sftp = ssh.open_sftp()

        descarga_rec(remote_path, local_path, sftp=sftp)
        
        sftp.close()
        ssh.close()
        
        print("All files downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    server_address = "s-e0b41ca0a90a48059.server.transfer.sa-east-1.amazonaws.com"
    username = "eduardo.gonzales.pisco@entel.pe"
    password = "testing123"
    remote_dir = "/awsfluxus-entel/entel/REPO_CODE"
    local_dir = r"C:\Users\mdrmo\Desktop\entel verano 2024\trabajo\Abril\REPO_CODE"
    
    descarga(server_address, username, password, remote_dir, local_dir)
