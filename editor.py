"""
=>simple file editor/creator
=>>creat file with the user input text
=>>edit file : find/change specifique word in the whole file
Author: Safou Abderrahim
"""

from fileHandle import checkFile


def check(file_name):
	file = checkFile(file_name)
	file.handle()
def creat_file(file_name,text):
	with open(file_name ,"w") as f :
		f.write(text)
	print("creating file completed[✓]")

def isthere(file_name , last_word ) :
      	with open(file_name ,"r+") as f:
                last_text_ = f.read()
                if last_word in last_text_ :
                        return True


def edit(file_name , last_word , new_word) :
	last_text_list = []
	if isthere(file_name , last_word):
		with open(file_name ,"r+") as f:
			last_text_ = f.read()
			last_text_list.append(last_text_)

		last_text_str = "".join(map(str,last_text_list))
		edited_text = last_text_str.replace(last_word , new_word)
		with open(file_name ,"w") as file :
			file.write(edited_text)
		print("editing file completed[✓]")
	else :
		print(f"there is'nt this word=>{lt}")


user_choice = input("1)creat ; 2)edit :")

if user_choice == '1' :
	file_name = input("Choose a  file name :")
	user_text = input("Enter the text :")
	creat_file(file_name,user_text)
elif user_choice == '2' :
	file_name = input("Enter file name:")
	check(file_name)
	last_word = input("enter last word:")
	new_word = input("enter new word:")
	edit(file_name ,last_word ,new_word)
else :
	print("[!] wrong choice")
