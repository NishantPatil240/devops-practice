# changed this python file
import os
import platform
import sys

apikey = os.environ.get('API_KEY')

if apikey == None:
	print("Error: Key Not Found!!!")
	sys.exit()
else:
	print("COntinue...")

current_os = platform.system()

print(f"Deploying on {current_os}")

os.makedirs("build",exist_ok=True)

file_path = os.path.join("build","status.txt")

with open(file_path, "w") as f:
	f.write("Deployment Active")

print(f"File at {file_path} created successfully!!")

