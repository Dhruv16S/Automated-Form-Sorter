import random
import string
def password_generator():
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    num=string.digits
    #symbols=string.punctuation
    all=lower+upper+num   #+symbols
    temp=random.sample(all,5)
    password="".join(temp)
    return(password)
p=input("New User y/n: ")
if(p=='y'):
    user_name=input("Please enter your username: ")
    pwd=password_generator()
    print(f"User name is {user_name},password is {pwd}")
else:
    if(p=='n'):
        user_name=input("Please enter your username: ")
        pwd=input("Please enter your password: ")