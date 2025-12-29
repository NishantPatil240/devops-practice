import os

logfile_name = os.environ.get("LOG_FOLDER", "app_logs")

os.makedirs(logfile_name,exist_ok=True)

file_path = os.path.join(logfile_name,"systemcheck.txt")

with open(file_path, "w") as f:
	f.write("ALll System go!!\n")
	print("Log File Created Successfully!!")



