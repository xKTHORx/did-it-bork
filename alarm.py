#!/usr/bin/env python

token = "xxxxxxxx-xxxxx-xxx-xxxx-xxxxxxxxxxx"
url = "https://xxx.sample.com/xxx/xxx/sms"
import hashlib
import time
import requests

filename = "/home/xxx/xxx/error-log.txt"

md5_hash = hashlib.md5()
with open(filename, "rb") as f:
    # Read and update hash in chunks of 4K
    for byte_block in iter(lambda: f.read(4096), b""):
        md5_hash.update(byte_block)
    log_hash = md5_hash.hexdigest()

new_hash = log_hash
while new_hash == log_hash:
    time.sleep(900)
    md5_hash = hashlib.md5()
    with open(filename, "rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
        new_hash = md5_hash.hexdigest()
    if new_hash != log_hash:
        break

data = {"token":token, "username":"Xsample.userX"}
data["message"] = "XXX FEED DOWN"
res = requests.post(url, data)
