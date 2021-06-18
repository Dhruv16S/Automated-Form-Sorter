import json
import re 

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def input_username():
    emailid = input("Enter Your Email id: ")
    isvalid = check_mail(emailid);
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
    

username = input_username()
password = input_password()

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