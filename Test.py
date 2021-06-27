# import smtplib
# from email.message import EmailMessage
# import imghdr
# with open("Test.docx", "rb") as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
# msg = EmailMessage()
# msg["From"] = "dscuderiaferrari@gmail.com"
# msg["To"] = "dhruv162002@gmail.com"
# msg["Subject"] = "Testing attachments"
# msg.set_content('Please find attached below')
# msg.add_attachment(file_data, maintype = "application", subtype = "octet-stream", filename = f.name)
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login("dscuderiaferrari@gmail.com","ferrarisf21")
#     connection.send_message(msg)

a = ["A","B"]
b = ["A","B","C"]
c = list(set(a).union(set(b)) - set(a).intersection(set(b)))
print(type(b))
print(c)