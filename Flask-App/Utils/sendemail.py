import smtplib
from email.mime.text import MIMEText as text
import emailconfig
def send_email(users, subject, msg):
	for i in range(len(users)):
		users[i] = users[i]+"@nyu.edu"

	try:
		message = '''Subject: {sub}\nFrom: {fro}\nTo: {users}\n{msg}'''.format(sub = subject, fro = emailconfig.EmailAddress, users = ", ".join(users), msg = msg)
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login(emailconfig.EmailAddress, 
		emailconfig.Password)
		
		server.sendmail(emailconfig.EmailAddress,users,message)
		server.quit()
		print('Email Sent')
	except (smtplib.SMTPAuthenticationError, smtplib.SMTPHeloError, smtplib.SMTPConnectError, smtplib.SMTPDataError) as e:
		print('Email failed', e)


