######## code-start ########
""" terminal-menu-version.py
:Run: cd ~/client-project/client-project/scripts/;clear;pwd;ls .;python3 terminal-menu-version.py;
"""

""" :To Do:
- add open app/template commands for each option
- Play Music On Start
- fix from simple_term_menu import TerminalMenu
- fix from pkg_resources import Requirement
"""
'''SETUP'''
import os
import subprocess
from simple_term_menu import TerminalMenu
from pkg_resources import Requirement
subprocess.run('clear')
os.chdir("/Users/icepitproductions/Documents/GitHub/Projects/python/client-project")
current_dir = os.getcwd()
print(os.getcwd())
subprocess.run('ls')
suffix = " Project"
parent_dir = "/Users/icepitproductions/Desktop"
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


'''menu options list'''
main_menu = [
  "[a] audio project",
  "[i] image project",
  "[d] docs project",
  "[v] video project",
  "[w] web project",
  "[q] quit"]
audio_project_menu = [
  "[1] Produce",
  "[2] Record",
  "[3] Mix & Master",
  "[q] Go Back"]
'''show menu options list'''
loop = True
while loop:
    choice = main_menu[
      TerminalMenu(
        main_menu,
        title = "Main menu",
        menu_cursor_style = ("fg_green","bold"),
        menu_highlight_style = ("fg_black", "bg_green"),
        menu_cursor = "~"
        ).show()]
    '''tasks'''
    if choice == "[a] audio project":
        sub_loop = True
        while sub_loop:
            choice = audio_project_menu[
              TerminalMenu(
                audio_project_menu,
                title = "audio project menu",
                menu_cursor_style = ("fg_green", "bold"),
                menu_highlight_style = ("fg_black", "bg_green"),
                menu_cursor = "🔊"
                ).show()]
            if choice == "[1] Produce":
                '''Metadata'''
                producer_name = input("Producer Name  : ")
                # Project_Name = input("Title          : ")
                tempo = input("BPM            : ")
                type = "Beat - " + producer_name + " - "
                
                
                
                '''Path'''
                directory = (type + Project_Name + suffix)
                path = os.path.join(parent_dir, directory)
                print(choice + " % s 'on Desktop' " % directory)
                
                
                
                '''Command'''
                os.makedirs(path)
                
                
                
                '''Exit'''
                sub_loop = False
                loop = False
            elif choice == "[2] Record":
                artist_name = input("Artist         : ")
                Project_Name = input("Title          : ")
                type = "Song - " + artist_name + " - "
                directory = (type + Project_Name + suffix)
                path = os.path.join(parent_dir, directory)
                print(choice + " % s 'on Desktop'" % directory)
                os.makedirs(path)
                sub_loop = False
                loop = False
            elif choice == "[3] Mix & Master":
                sub_loop = False
                loop = False
            elif choice == "[q] Go Back":
                sub_loop = False
    elif choice == "[q] quit":
        loop = False
######## code-end   ########
