import smtplib
# from email import mime.text

mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo() 
content = 'hello!\nYou have received a test email using a python script!\nYay!'
mail.starttls()
mail.login('connectnyuad@gmail.com', 'xxxpasswordxxx')
mail.sendmail('navyasuri@nyu.edu', 'aas1066@nyu.edu', content)
mail.close()