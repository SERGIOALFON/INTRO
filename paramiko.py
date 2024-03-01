import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='18.220.165.113', username='kali', password='kali', port=22)
ssh.connect(hostname='18.220.165.113', username='kali'
            , key_filename='C:\Users\Usuario\PycharmBasic\pythonProject\prueba.txt', port=22)

sftp_client = ssh.open_sftp()
print(sftp_client.getcwd())
sftp_client.chdir("/home/kali")
print(sftp_client.getcwd())
sftp_client.put('upload_prueba.txt','/home/kali/upload_prueba.txt')
sftp_client.close()
ssh.close()
