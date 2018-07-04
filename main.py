import read as  pr
import pullEmail as pe
import openMailbox as omail
import sendMail as sm

def main():
	password = ""
	name = "Justin"
	toEmail = ""
	mail = omail.openMailbox(password)
	file = pe.pullMail(mail)
	output = pr.processNumbers(name, file)
	'''outputFile = open("numbers_" + name + ".txt", "w")
	outputFile.write(file + '\n')
	outputFile.write(output)
	outputFile.close()'''
	sm.sendMail(output, file, toEmail)
main()
