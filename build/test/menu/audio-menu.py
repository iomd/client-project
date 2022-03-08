import os,subprocess,datetime
from simple_term_menu import TerminalMenu


os.chdir("/Users/icepitproductions/GitHub/Projects/python/client-project/build")
subprocess.run('clear')
current_dir = os.getcwd()
suffix = " Project"
Desktop = ("/Users/icepitproductions/Desktop")

date = datetime.date.today()

main_menu = [
  "[a] audio project",
  "[q] quit"]

audio_project_menu = [
  "[1] Produce",
  "[2] Record",
  "[3] Mix & Master",
  "[q] Go Back"]

loop = True

while loop:
    choice = main_menu[TerminalMenu(main_menu,title = "Enter Project Type?",menu_cursor_style = ("fg_green","bold"),menu_highlight_style = ("fg_black", "bg_green"),menu_cursor = "~").show()]
    if choice == "[a] audio project":
        sub_loop = True
        while sub_loop:
            choice = audio_project_menu[TerminalMenu(audio_project_menu,title = "Audio Project Type?",menu_cursor_style = ("fg_green", "bold"),menu_highlight_style = ("fg_black", "bg_green"),menu_cursor = "🔊").show()]

            if choice == "[1] Produce":

                type = "Beat"
                Producer_Name = input("Enter Producer Name? ")
                Project_Name = input("Enter Project Name ? ")
                Project_Folder_Name = (Producer_Name + "[" + date + "]" + " - " + Project_Name + suffix)
                Project_Path = (Desktop + "/" + Project_Folder_Name)
                
                os.makedirs(Project_Path)
                print()
                print(choice + " % s 'on Desktop' " % type + " by " + Producer_Name)


                sub_loop = False
                loop = False

            elif choice == "[2] Record":

                type = "Song"
                Artist_Name = input ("Enter Artist Name  ? ")
                Project_Name = input("Enter Title Name   ? ")
                Project_Folder_Name = (Artist_Name + " - " + Project_Name + suffix)
                Project_Path = (Desktop + "/" + Project_Folder_Name)
                os.makedirs(Project_Path)
                
                print(date)
                print(choice + " % s 'on Desktop'" % type + " by " + Artist_Name)

                
                sub_loop = False
                loop = False

            elif choice == "[3] Mix & Master":
                sub_loop = False
                loop = False

            elif choice == "[q] Go Back":sub_loop = False

    elif choice == "[q] quit":
        loop = False


# ls Desktop
