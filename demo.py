'''demo.py
this script is to be added to "terminal-menu-version.py"
'''


'''AUDIO PROJECT SETUP'''
import os
import subprocess
subprocess.run('clear')
os.chdir("/Users/icepitproductions/Documents/GitHub/Projects/python/client-project")
current_dir = os.getcwd()
print(os.getcwd())
subprocess.run('ls')


'''User Input'''
Project_Name = input("Enter Project Name?")


'''Root_Folder'''
Project_Path = ("/Users/icepitproductions/Desktop")
directory = (Project_Path + "/" + Project_Name)
Root_Folder = os.path.join(directory)
os.makedirs(Root_Folder)


'''Sub Folders'''
folder_1 = ("/audio")
os.makedirs(Root_Folder + folder_1)
folder_2 = ("/archives")
os.makedirs(Root_Folder + folder_2)
folder_3 = ("/imports")
os.makedirs(Root_Folder + folder_3)
folder_4 = ("/exports")
os.makedirs(Root_Folder + folder_4)
folder_5 = (folder_2 + "/stems")
os.makedirs(Root_Folder + folder_5)
folder_6 = (folder_4 + "/final")
os.makedirs(Root_Folder + folder_6)
folder_7 = (folder_4 + "/unused")
os.makedirs(Root_Folder + folder_7)


'''Files'''
os.chdir(Root_Folder + folder_1)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
os.chdir(Root_Folder + folder_2)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
os.chdir(Root_Folder + folder_3)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
os.chdir(Root_Folder + folder_4)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
os.chdir(Root_Folder + folder_5)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
os.chdir(Root_Folder + folder_6)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
os.chdir(Root_Folder + folder_7)
with open("text.txt", "w") as f:
  f.write("This is a text file.")
