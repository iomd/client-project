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

from simple_term_menu import TerminalMenu
import os
import subprocess
from pkg_resources import Requirement

suffix = " Project"
parent_dir = "/Users/icepitproductions/Desktop"

# menu options list
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

# show menu options list
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

    # tasks
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
                # Metadata
                producer_name = input("Producer Name  : ")
                project_name = input("Title          : ")
                tempo = input("BPM            : ")
                type = "Beat - " + producer_name + " - "

                # Path
                directory = (type + project_name + suffix)
                path = os.path.join(parent_dir, directory)
                print(choice + " % s 'on Desktop' " % directory)

                # Command
                os.makedirs(path)

                # subprocess.call('Meta.app')
                subprocess.call('/Applications/Meta.app')

                # Exit
                sub_loop = False
                loop = False

            elif choice == "[2] Record":
                artist_name = input("Artist         : ")
                project_name = input("Title          : ")

                type = "Song - " + artist_name + " - "

                directory = (type + project_name + suffix)

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
