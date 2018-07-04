import smtplib
import time
import imaplib
import email 

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "justinworkoutmailer" + ORG_EMAIL
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
def openMailbox(FROM_PWD):	
	try:
		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(FROM_EMAIL,FROM_PWD)
		mail.select('inbox')
		return mail
	except:
		print('Could not connect to mailbox')
