import json

f=open("logindetails.json","r+")

username = input("Enter Email id: ")
password = input("Enter your Password: ")

contents = f.read()
js = json.loads(contents)

email = True

for i in range(len(js)):
    if js[i]['username'] == username:
        if js[i]['password'] == password:
            print("Login Successful")
            email=True
            break
        else:
            #if mail correct and password wrong
            print("Incorrect Password")
            break
    else:
        email = False

    
if email is False:
    #if username does not exit
    print("Email Does not Exit, try to Sign Up")

f.close()