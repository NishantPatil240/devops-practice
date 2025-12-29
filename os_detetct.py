import platform
import os

current_os = platform.system()

print(f"System Detected: {current_os}")

if current_os == "Windows":
	print("Hello Windows User! Use BackwardSlash (\\)")
elif current_os == "Linux":
	print("Hello Linux Master! Use Forwardslash (/)")
else:
	print(f"Hello {current_os} User!")

safe_path = os.path.join('logs','error','critical.txt')

print(f"The current machine path is : {safe_path}")

os.mkdir("Name")


