# /usr/bin/python3
# terminal-menu-version.py
# -----imports---------------------------
import os,subprocess
from simple_term_menu import TerminalMenu
""" SETUP
clear;
cd /Users/icepitproductions/GitHub/Projects/python/client-project/build;
pwd;
python3 terminal-menu-version.py;
"""
######## code-start ########
subprocess.run('clear')
Desktop = "~/Desktop"
# print(Desktop)
# print(os.listdir(Desktop))
os.chdir("/Users/icepitproductions/GitHub/Projects/python/client-project/build")
current_dir = os.getcwd()
print(os.getcwd())


'''User Input'''
suffix = " Project"
Project_Name = input("Enter Project Name?")


'''Folders'''
Project_Path = ("/Users/icepitproductions/Desktop")
directory = (Project_Path + "/" + Project_Name)
Root_Folder = os.path.join(directory)
folder_1 = ("/audio")
folder_2 = ("/archives")
folder_3 = ("/imports")
folder_4 = ("/exports")
folder_5 = (folder_2 + "/stems")
folder_6 = (folder_4 + "/final")
folder_7 = (folder_4 + "/unused")




'''file contents'''




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
                type = "Beat - " + producer_name + " - "




                '''Path'''
                directory = (type + Project_Name + suffix)
                path = os.path.join(Desktop, directory)
                print(choice + " % s 'on Desktop' " % directory)




                '''Create Directories & Files'''
                os.makedirs(Root_Folder + folder_1)
                os.makedirs(Root_Folder + folder_2)
                os.makedirs(Root_Folder + folder_3)
                os.makedirs(Root_Folder + folder_4)
                os.makedirs(Root_Folder + folder_5)
                os.makedirs(Root_Folder + folder_6)
                os.makedirs(Root_Folder + folder_7)
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




                '''Exit'''
                sub_loop = False
                loop = False
            elif choice == "[2] Record":
                artist_name = input("Artist         : ")
                Project_Name = input("Title          : ")
                type = "Song - " + artist_name + " - "
                directory = (type + Project_Name + suffix)
                path = os.path.join(Desktop, directory)
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
