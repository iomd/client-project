#!/usr/bin/python3
# -*- coding: utf8 -*-
# :Author: Chris Shanklin <ice.fetty@gmail.com>
# :Copyright: © 2022 Icepit Productions.
# :License:
#
# :Revision: v0.01
# :Date: $Date: 2022-03-04 00:19:43 -0500 $

"""comments
new_client_project.py
======

:Requirements: pip3 install simple_term_menu;
:Usage: python3 new_client_project.py
"""

######## code-start ########

import os
from simple_term_menu import TerminalMenu
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
image_project_menu = [
  "[a] sub_option1",
  "[b] sub_option2",
  "[q] Go Back"]
docs_project_menu = [
  "[a] sub_option1",
  "[b] sub_option2",
  "[q] Go Back"]
video_project_menu = [
  "[a] sub_option1",
  "[b] sub_option2",
  "[q] Go Back"]
web_project_menu = [
  "[a] sub_option1",
  "[b] sub_option2",
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
                producer_name = input("Producer Name  : ")
                project_name = input("Title          : ")
                tempo = input("BPM            : ")

                type = "Beat - " + producer_name + " - "

                directory = (type + project_name + suffix)

                path = os.path.join(parent_dir, directory)
                print(choice + " % s 'on Desktop' " % directory)

                os.makedirs(path)

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

    elif choice == "[i] image project":
        sub_loop = True
        while sub_loop:
            choice = image_project_menu[
              TerminalMenu(
                image_project_menu,
                title = "image project menu",
                menu_cursor_style = ("fg_green", "bold"),
                menu_highlight_style = ("fg_black", "bg_green"),
                menu_cursor = "~"
                ).show()]

            if choice == "[a] sub_option1":
                print (choice)

            elif choice == "[b] sub_option2":
                print (choice)

            elif choice == "[q] Go Back":
                sub_loop = False

    elif choice == "[d] docs project":
        sub_loop = True
        while sub_loop:
            choice = docs_project_menu[
              TerminalMenu(
                docs_project_menu,
                title = "docs project menu",
                menu_cursor_style = ("fg_green", "bold"),
                menu_highlight_style = ("fg_black", "bg_green"),
                menu_cursor = "~"
                ).show()]

            if choice == "[a] sub_option1":
                print (choice)

            elif choice == "[b] sub_option2":
                print (choice)

            elif choice == "[q] Go Back":
                sub_loop = False

    elif choice == "[v] video project":
        sub_loop = True
        while sub_loop:
            choice = video_project_menu[
              TerminalMenu(
                video_project_menu,
                title = "video project menu",
                menu_cursor_style = ("fg_green", "bold"),
                menu_highlight_style = ("fg_black", "bg_green"),
                menu_cursor = "~"
                ).show()]

            if choice == "[a] sub_option1":
                print (choice)

            elif choice == "[b] sub_option2":
                print (choice)

            elif choice == "[q] Go Back":
                sub_loop = False

    elif choice == "[w] web project":
        sub_loop = True
        while sub_loop:
            choice = web_project_menu[
              TerminalMenu(
                web_project_menu,
                title = "web project menu",
                menu_cursor_style = ("fg_green", "bold"),
                menu_highlight_style = ("fg_black", "bg_green"),
                menu_cursor = "~"
                ).show()]

            if choice == "[a] sub_option1":
                print (choice)

            elif choice == "[b] sub_option2":
                print (choice)

            elif choice == "[q] Go Back":
                sub_loop = False

    elif choice == "[q] quit":
        loop = False

######## code-end   ########
