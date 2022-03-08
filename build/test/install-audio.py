# /usr/bin/python3
# build/install-audio.py
# -----imports---------------------------
import os
import sys
import codecs
import subprocess
import shutil
from os import system
from datetime import datetime
from pkg_resources import Requirement
from simple_term_menu import TerminalMenu
######## code-start ########



# -----clear screen--------------------------------------------------------------
# subprocess.run('clear')
# -----user name--------------------------------------------------------------
# subprocess.run('whoami')
# -----current date & time--------------------------------------------------------------
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# subprocess.run('date')
# -----current working directory--------------------------------------------------------------
# current_dir = os.getcwd()
# print(os.getcwd())
# subprocess.run('pwd')
# -----list contents of current working directory--------------------------------------------------------------
# subprocess.run('ls')
# -----say-----------------------------------------------------------
# text="Files Made"
# def my_text(text):
#     system("say {}".format(text))
# my_text(text)
# -----copy from file to make folders named after the contents of the file-----------------------------------------------------------------
# python -c 'import sys,os,codecs;[os.mkdir(d) for d in codecs.open(sys.argv[1],"r","utf8")]' list.txt
# -----copy file commands---------------------------
# copyfile() = copies contents of a file
# copy() = + permission mode , destination can be a directory
# copy2() = + copies metadata (file creation time & modification time)
# -----folder---------------------------
Desktop = ('/Users/icepitproductions/Desktop/')
app_folder = ('/Users/icepitproductions/Documents/GitHub/Projects/python/client-project/')
app_folder_build_audio = ("/Users/icepitproductions/Documents/GitHub/Projects/python/client-project/build/audio")

folderA = "Project"
folderB = "Ableton Project Info"
folderC = "Audio Files"
folderD = "Backup"
folderE = "Exports"
folderG = "Stems"
folderF = "Samples"
folderH = "Processed"
folderI = "Consolidate"
folderJ = "Freeze"
folderK = "Recorded"
folderL = "Reverse"

os.chdir(app_folder_build_audio)

os.makedirs(folderA)
os.makedirs(folderA + "/" + folderB)
os.makedirs(folderA + "/" + folderC)
os.makedirs(folderA + "/" + folderD)
os.makedirs(folderA + "/" + folderE)
os.makedirs(folderA + "/" + folderE + "/" + folderG)
os.makedirs(folderA + "/" + folderF)
os.makedirs(folderA + "/" + folderF + "/" + folderH)
os.makedirs(folderA + "/" + folderF + "/" + folderH + "/" + folderI)
os.makedirs(folderA + "/" + folderF + "/" + folderH + "/" + folderJ)
os.makedirs(folderA + "/" + folderF + "/" + folderH + "/" + folderL)
os.makedirs(folderA + "/" + folderF + "/" + folderK)

# # -----file---------------------------
# os.chdir(app_folder_build_audio)
# file1 = ("client_email.csv")
# fil1contents = ("test")
# with open(file1, "w") as f:f.write(fil1contents)

# os.chdir(folderA)
# file2 = ("client_notes.csv")
# fil2contents = ("test")
# with open(file2, "w") as f:f.write(fil2contents)

# file3 = ("changelog.log")
# fil3contents = ("test")
# with open(file3, "w") as f:f.write(fil3contents)

# file4 = ("sample_cue_points.txt")
# fil4contents = ("test")
# with open(file4, "w") as f:f.write(fil4contents)

# os.chdir(app_folder_build_audio)
# file5 = ("README.md")
# fil5contents = ("test")
# with open(file5, "w") as f:f.write(fil5contents)

# file6 = ("index.html")
# fil6contents = ("test")
# with open(file6, "w") as f:f.write(fil6contents)

# # ----------------------------------------------------------------

