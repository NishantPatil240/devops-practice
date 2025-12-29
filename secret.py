import os

secret = os.environ.get("DB_PASSWD", "Access Denied: Password Not Found!")

print(f"Secret Password : {secret}")
