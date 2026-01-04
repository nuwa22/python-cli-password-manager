import random
import string

passwords = {}
print("-" * 20  + " My Password Manager " + "-" * 20)
print("1. Add Password")
print("2. View Password")
print("3. Exit")

def generatePassword(length = 12):
	allCharacters = string.ascii_letters + string.digits + string.punctuation
	password = "".join(random.choices(allCharacters, k = length))
	return password

def addPassword():
	global passwords
	siteName = input("Enter Site Name: ")
	choice = input("Do you want to generate a random password? (Y/N): ")
	if choice == "Y":
		password = generatePassword()

	else:
		password = input("Enter your password: ")

	passwords[siteName] = password
	print(f"Password for {siteName} saved successfully!\n")
		
	try:
		file = open("passwordBook.txt" , "a")
		file.write(f"{siteName} | {password}\n")
		file.close()
	except Exception as e:
		print(f"Error saving to file: {e}")

def viewPasswords():
	global passwords
	searchSite = input("Enter Site Name: ")
	found = False
		
	try:
		file = open("passwordBook.txt", "r")
			
		for line in file:
			data = line.strip().split(" | ")
			if len(data) == 2:
				siteInFile = data[0]
				passwordInFile = data[1]
					
				if siteInFile == searchSite:
					print(f"Password for {searchSite} is {passwordInFile}")
					found = True
					break
		file.close()
		if not found:
			print("Password not found.")

	except FileNotFoundError:
		print("No saved passwords found yet.")

def main(userInput):
	if userInput == 1:
		addPassword()
	elif userInput == 2:
		viewPasswords()
	elif userInput == 3 :
		return "exit"
	
while True :
	userInput = int(input("Enter 1/2/3: "))
	if main(userInput) == "exit" :
		break
				
		