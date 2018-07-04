import smtplib
import email
import openMailbox as om

def sendMail(body, subject, password, toEmail):
	mail = smtplib.SMTP('smtp.gmail.com', 587)
	mail.starttls()
	mail.login('justinworkoutmailer', password)
	

	msg = "\r\n".join([
	"From: justinworkoutmailer@gmail.com",
	"To: jford@oswego.edu",
	"Subject: " + subject,
	"",
	body
	])
	mail.sendmail("justinworkoutmailer@gmail.com", toEmail, msg)
#	mail.sendmail('justinworkoutmailer@gmail.com', 'jford2@oswego.edu', msg)
