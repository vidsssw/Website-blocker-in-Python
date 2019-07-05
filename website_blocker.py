import time
from _datetime import datetime as dt

redirect="127.0.0.1"
host_path="C:\Windows\System32\drivers\etc\hosts"
website_list=["www.facebook.com","www.twitter.com"]
while True:
    if dt.now().time().hour >= 8 and dt.now().time().hour <= 16:
        file = open("hosts", "r+")
        content = file.read()
        for w in website_list:
            if w in content:
                pass
            else:
                file.write(redirect + " " + w + "\n")
    else:
        file = open("hosts", "r+")
        content = file.readlines()
        file.seek(0)

        for l in content:
            if not any(website in l for website in website_list):
                file.write(l)

        file.truncate()

    time.sleep(10)




