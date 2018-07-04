import smtplib
import time
import imaplib
import email

def pullMail(mail):
	
	try:
		results, data = mail.uid('search', None, 'ALL')
		uids = data[0].split()
		result, data = mail.uid('fetch', uids[-1], '(RFC822)')
	except:
		print("no mail")
	#for response_part in data:
	m = email.message_from_string(data[0][1])

	if m.get_content_maintype() == 'multipart': #multipart messages only
	    for part in m.walk():
	        #find the attachment part
	        if part.get_content_maintype() == 'multipart': continue
	        if part.get('Content-Disposition') is None: continue

	        #save the attachment in the program directory
	        filename = part.get_filename()
	        fp = open(filename, 'wb')
        	fp.write(part.get_payload(decode=True))
        	fp.close()
        	print '%s saved!' % filename
        	return filename
        	
	#mail.store(uids[-1], '+FLAGS', '\\Deleted')