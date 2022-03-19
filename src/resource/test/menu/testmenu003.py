import os,sys,subprocess,shutil,pyttsx3
from simple_term_menu import TerminalMenu

subprocess.run('clear')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()
print("")
print(" =============================================== Hello World!! ================================================")
print("\n\t 1.BEAT \t 2. \n\t 3. \t 4. \n\t 5.	 \t 6. \n\t 7. \t 8. \n\t 9.	 \t 10. \n\n\t\t	 0. FOR EXIT")
print("\n ============================================ Welcome To My Tools ============================================")
print("")
print("")

while True:
	print("ENTER SELECTION : ", end='')
	p = input()
	p = p.upper()
	print(p)

	if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
		print(".")
		print(".")
		continue

	elif ("BEAT" in p) or ("PRODUCE" in p) or ("1" in p):
		loop = True
		while loop:
			print(".")
			print(".")
		
			producer_name = input("Producer : ");
			project_name = input("Project  : ");
			type = "Beat - " + producer_name + " - ";

			suffix = " Project"
			Project_Path = ("/Users/icepitproductions/Desktop");
			directory = (Project_Path + "/" + producer_name + " - " + project_name + " " + suffix);
			Root_Folder = os.path.join(directory);
			Desktop = "/Users/icepitproductions/Desktop"
			os.chdir("/Users/icepitproductions/bin");
			current_dir = os.getcwd();
			directory = (type + project_name + suffix)
			path = os.path.join(Desktop, directory);

			folder_1 = ("/audio")
			folder_2 = ("/archives")
			folder_3 = ("/imports")
			folder_4 = ("/exports")
			folder_5 = (folder_2 + "/stems")
			folder_6 = (folder_4 + "/final")
			folder_7 = (folder_4 + "/unused")
			os.makedirs(Root_Folder + folder_1)
			os.makedirs(Root_Folder + folder_2)
			os.makedirs(Root_Folder + folder_3)
			os.makedirs(Root_Folder + folder_4)
			os.makedirs(Root_Folder + folder_5)
			os.makedirs(Root_Folder + folder_6)
			os.makedirs(Root_Folder + folder_7)

			os.chdir(Root_Folder);
			shutil.copyfile('/Volumes/CatalogHD/TemplateLibrary/[FLSTUDIO]/basic.nfo',project_name + ".nfo");
			Project_File_1 = shutil.copyfile('/Volumes/CatalogHD/TemplateLibrary/[FLSTUDIO]/basic.flp',project_name + ".flp"); print("FLStudio : " + Project_File_1);

			os.chdir(Root_Folder);
			Project_File_2 = shutil.copyfile('/Volumes/CatalogHD/TemplateLibrary/[ABLETON]/Macros.als',project_name + ".als"); print("Ableton  : " + Project_File_2);

			# # subprocess.run('pwd');
			subprocess.run('ls');
			# os.system("winword")
			os.system("")








			# Exit
			loop = False

	elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
		break

	else:
		print("Is Invalid,Please Try Again")
		print(".")
		print(".")
