import time
from datetime import datetime as dt
hosts_path = r"/etc/hosts" #We are using r for raw and string
hosts_temp = "hosts"
redirect =  "127.0.0.1"
web_site_list = ["www.facebook.com", "facebook.com"] #You can choise the website

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,22):
        print("Working hours")
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in  web_site_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        
    else:
        print("Fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0) #Reseting the pointer on the top of the file
            for line in content:
                if not any(website in line for website in web_site_list):
                    file.write(line)

            file.truncate(line) #This line is used to delete the trailing lines
    time.sleep(5)
