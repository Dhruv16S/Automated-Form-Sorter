import json
import re 
import random
import string
from email.message import EmailMessage
import smtplib


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def input_username():
    emailid = input("Enter Your Email id: ")
    isvalid = check_mail(emailid)
    if isvalid is False:
        print("Not a Valid Email")
        exit()
    return emailid

def check_mail(input_username):
    if(re.search(regex,input_username)):   
        return True   
    else:   
        return False

def input_password():
    password = input("Enter your Password: ")
    return password
 
def password_generator():
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits

    all=lower+upper+num   #+symbols
    temp=random.sample(all,5)
    password="".join(temp)
    return(password)

def email_alert(subject, body, to):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('testproject194@gmail.com', 'testproject!@#$')
    
    msg = EmailMessage()
    msg['From'] = 'testproject194@gmail.co'
    msg['to'] = to
    msg['subject'] = subject
    msg.set_content(body)
    server.send_message(msg)

def listappening(username, password):
    # create a file with the name below and put an empty list in the new file
    # [] 
    f=open("logindetails.json","r+")

    contents = f.read()
    js = json.loads(contents)

    js.append({'username': username, 'password': password})
    f.seek(0)
    f.write(json.dumps(js, indent=2))
    f.truncate()

    f.close()

sec_code=password_generator()

username = input_username()
print(username)
email_alert("Verification Code","Verification Code is "+ sec_code,username)

check_code = input("Enter your Mail Verfication Code: ")

if sec_code == check_code:
    pwd = input("Enter Your Password: ")
    chec_pwd = input("ReType your Password: ")
    if pwd == chec_pwd:
        password=pwd
        listappening(username, password)

    else:
        print("Passwords do Not Match")

else:
    print("Verification Code Does not Match")

