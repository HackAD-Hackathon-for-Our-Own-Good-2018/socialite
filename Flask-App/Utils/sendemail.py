import smtplib
from email.mime.text import MIMEText as text
import emailconfig
def send_email(User1,User2,subject, msg):
	try:
		message = '''Subject: {sub}\nFrom: {fro}\nTo: {u1}, {u2}\n{msg}'''.format(sub = subject, fro = emailconfig.EmailAddress, u1 = User1, u2 = User2, msg = msg)
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login(emailconfig.EmailAddress, 
		emailconfig.Password)
		
		server.sendmail(emailconfig.EmailAddress,[User1,User2],message)
		server.quit()
		print('Email Sent')
	except:
		print('Email failed')


