import os,sys,subprocess,shutil,pyttsx3
from simple_term_menu import TerminalMenu

subprocess.run('clear')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
print("")
print(" =============================================== Hello World!! ================================================")
print("")
print("\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 5.VLC PLAYER	 \t 6.ADOBE ILLUSTRATOR \n\t 7.ADOBE PHOTOSHOP \t 8.MICROSOFT EDGE \n\t 9.NOTEPAD	 \t 10.TELEGRAM \n\n\t\t	 0. FOR EXIT")
print("\n	 (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")
print("\n ============================================ Welcome To My Tools ============================================")
print("")
print("")

while True:
	print(" CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
	p = input()
	p = p.upper()
	print(p)

	if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
		print(".")
		print(".")
		continue

	elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
		print(".")
		print(".")
		os.system("chrome")

	elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("8" in p):
		print(".")
		print(".")
		os.system("msedge")

	elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
		print(".")
		print(".")
		os.system("Notepad")

	elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("5" in p):
		print(".")
		print(".")
		os.system("VLC")

	elif ("ILLUSTRATOR" in p) or ("AI" in p) or ("6" in p):
		print(".")
		print(".")
		os.system("illustrator")

	elif ("PHOTOSHOP" in p) or ("PS" in p) or ("PHOTOSHOP CC" in p) or ("7" in p):
		print(".")
		print(".")
		os.system("photoshop")

	elif ("TELEGRAM" in p) or ("TG" in p) or ("10" in p):
		print(".")
		print(".")
		os.system("telegram")

	elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
		print(".")
		print(".")
		os.system("excel")

	elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
		print(".")
		print(".")
		os.system("powerpnt")

	elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
		print(".")
		print(".")
		os.system("winword")

	elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
		break

	else:
		print("Is Invalid,Please Try Again")
		print(".")
		print(".")
