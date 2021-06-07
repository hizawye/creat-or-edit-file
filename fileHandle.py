from sys import exit
class checkFile:
	def __init__(self,filename):
		self.file = filename
	def handle(self):
		try :
			with open(self.file) as f :
				pass
		except :
			print(f"[!] somthing happend ,can't open the file '{self.file}'")
			exit()
		finally :
			pass


