from __future__ import print_function
import docx2txt as d2t
def processNumbers(name):
	output = ""
	txt = d2t.process("squat.docx")
	#name = raw_input("name: ")
	#name = "Justin".encode("utf-8")
	#nameFind = txt.find(name)
	txtSplit = txt.replace("-", " ").split()
	baseNumberInd = 0
	oneRm = 0
	for i,v in enumerate(txtSplit):
		if(v.strip()  == name):
			baseNumberInd = i + 1
			break

	oneRm = (txtSplit[baseNumberInd])
	for i,v in enumerate(txtSplit):
		j=0
		if((v == 'Squat' or v == "Bench" or v == "Deadlift") and i > 100):
			while ":" not in  txtSplit[i+j]:
				output = output + txtSplit[i+j].replace("(", "") + " " 
				j += 1
			output = output + ":\n"
		if("%" in v):
			sets = txtSplit[i+2].replace(",","")
			if(sets.isdigit() and i > 100):
				weight = float(oneRm) * float("." + v.replace("%", ""))
				while weight %  5 != 0:
					weight += 1
				output = output + str(weight) + " " + str(sets) + "\n"
				#print(" " + sets)
	return output
#print(txtSplit)

#print(processNumbers("Justin"))
