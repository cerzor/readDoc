import read as  pr
def main():
	name = "Justin"
	output = pr.processNumbers(name)
	outputFile = open("numbers_" + name + ".txt", "w")
	outputFile.write(output)
	outputFile.close()
main()
