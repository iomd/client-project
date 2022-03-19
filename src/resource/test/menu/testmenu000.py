#!/usr/local/bin/python3
# python3 ~/bin/terminal-menu-version.py;
from simple_term_menu import TerminalMenu
import os,sys,subprocess,shutil
subprocess.run('clear')
# menu options list
main_menu = [
  "[1] audio project",
  # "[2] image project",
  # "[3] docs project",
  # "[4] video project",
  # "[5] web project",
  "[q] quit"]
audio_project_menu = [
  "[1] Produce",
  # "[2] Record",
  # "[3] Mix & Master",
  "[q] Go Back"]
# show menu options list
loop = True
while loop:
    choice = main_menu[TerminalMenu(main_menu, title = "Main menu", menu_cursor_style = ("fg_green","bold"), menu_highlight_style = ("fg_black", "bg_green"), menu_cursor = "~").show()]
    project_name = input("Project  : ");
    if choice == "[1] audio project":
      sub_loop = True
      while sub_loop:
        choice = audio_project_menu[TerminalMenu(audio_project_menu, title = "audio project menu", menu_cursor_style = ("fg_green", "bold"), menu_highlight_style = ("fg_black", "bg_green"), menu_cursor = "🔊").show()]
        if choice == "[1] Produce":
            # Produce Project Type
            producer_name = input("Producer : ");
            type = "Beat - " + producer_name + " - ";
            # Path
            suffix = " Project"
            Project_Path = ("/Users/icepitproductions/Desktop");
            directory = (Project_Path + "/" + producer_name + " - " + project_name + " " + suffix);
            Root_Folder = os.path.join(directory);
            Desktop = "/Users/icepitproductions/Desktop"
            os.chdir("/Users/icepitproductions/bin");
            current_dir = os.getcwd();
            directory = (type + project_name + suffix)
            path = os.path.join(Desktop, directory);
            # Create Folders
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
            ## Copy flstudio Files
            os.chdir(Root_Folder);
            shutil.copyfile('/Volumes/CatalogHD/TemplateLibrary/[FLSTUDIO]/basic.nfo',project_name + ".nfo");
            Project_File_1 = shutil.copyfile('/Volumes/CatalogHD/TemplateLibrary/[FLSTUDIO]/basic.flp',project_name + ".flp"); print("FLStudio : " + Project_File_1);
            ## Copy ableton Files
            os.chdir(Root_Folder);
            Project_File_2 = shutil.copyfile('/Volumes/CatalogHD/TemplateLibrary/[ABLETON]/Macros.als',project_name + ".als"); print("Ableton  : " + Project_File_2);
            # Open
            # subprocess.run('pwd');
            # subprocess.run('ls');
            
            
            
            # Exit
            sub_loop = False
            loop = False
        # elif choice == "[2] Record":
        #     artist_name = input("Artist         : ")
        #     project_name = input("Title          : ")
        #     type = "Song - " + artist_name + " - "
        #     directory = (type + project_name + suffix)
        #     path = os.path.join(Desktop, directory)
        #     print(choice + " % s 'on Desktop'" % directory)
        #     os.makedirs(path)
        #     sub_loop = False
        #     loop = False
        # elif choice == "[3] Mix & Master":
        #     sub_loop = False
        #     loop = False
        elif choice == "[q] Go Back":
            sub_loop = False
    elif choice == "[q] quit":
        loop = False
