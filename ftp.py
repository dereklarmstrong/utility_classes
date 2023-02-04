import ftplib
import sys
import traceback

class FTP:
    """
    This class provides an implementation of the FTP (File Transfer Protocol)
    for transferring files to and from a remote FTP server.  To use it as SFTP
    change the port to 22.

    Attributes:
        host (str): The hostname or IP address of the FTP server.
        username (str): The username to use for authentication to the FTP server.
        password (str): The password to use for authentication to the FTP server.
        port (int): The port number to use for the FTP connection (default is 21).

    Methods:
        connect: Connect to the FTP server and authenticate with the provided credentials.
        upload_file: Upload a single file to the FTP server.
        download_file: Download a single file from the FTP server.
        get_file_list: List contents of current directory on the FTP server.
        change_directory: Change directory on the FTP server.
        close: Close the FTP connection.
    """
    
    def __init__(self, host, username, password, port=21):
        self.ftp = ftplib.FTP()
        self.ftp.connect(host, port)
        self.ftp.login(username, password)

    def upload_file(self, file_path, destination_path):
        try:
            with open(file_path, 'rb') as file:
                self.ftp.storbinary(f'STOR {destination_path}', file)
        except Exception as e:
            print(f"Error: Failed to upload file - {str(e)}")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print(f"File path: {file_path}, Destination path: {destination_path}")

    def download_file(self, source_path, destination_path):
        try:
            with open(destination_path, 'wb') as file:
                self.ftp.retrbinary(f'RETR {source_path}', file.write)
        except Exception as e:
            print(f"Error: Failed to download file - {str(e)}")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print(f"Source path: {source_path}, Destination path: {destination_path}")

    def get_file_list(self):
        try:
            return self.ftp.nlst()
        except Exception as e:
            print(f"Error: Failed to get file list - {str(e)}")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)

    def change_directory(self, path):
        try:
            self.ftp.cwd(path)
        except Exception as e:
            print(f"Error: Failed to change directory - {str(e)}")
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
            print(f"Directory path: {path}")

    def close(self):
        self.ftp.quit()
