import platform
import os

# Operating System Information
system_info = platform.uname()
print(f"Operating System: {system_info.system} {system_info.release} ({system_info.version})")
print(f"Machine: {system_info.machine}")
print(f"Processor: {system_info.processor}")

# Windows Version
if platform.system() == "Windows":
    windows_version = platform.win32_ver()
    print(f"Windows Version: {windows_version[0]} {windows_version[1]} ({windows_version[2]})")

# Username
username = os.getlogin()
print(f"Username: {username}")

# Current Working Directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")
