# !/usr/bin/python3
import time,sys,subprocess,os
os.system('clear')
os.system('pwd')
os.system('ls')
# ----------------------------------------------------------------
# exec(open('client_root.sh').read())

# Artist_Name = input()
# Project_Name = input()
# subprocess.call("client_root.sh")
# root = open("client_root.sh")

# ----------------------------------------------------------------

def project_type():
    time.sleep(1)
    os.system('clear')
    print("******* Main Menu ********")
    choice = input(
"""
[1] audio
[2] image
[3] video
[4] web
[0] quit

Please Select a Type:"""
    )
    if choice == "1" or choice == "audio" or choice == "Audio" or choice == "AUDIO":
      audio_project()
    elif choice == "2" or choice == "image" or choice == "Image" or choice == "IMAGE":
      image_project()
    elif choice == "3" or choice == "video" or choice == "Video" or choice == "VIDEO":
      video_project()
    elif choice == "4" or choice == "web" or choice == "Web" or choice == "WEB":
      web_project()
    else:
      # print("""*** Invalid Selection ****""")
      # print("* Make Another Selection *")
      # time.sleep(2)
      # project_type()
      quit()
def audio_project():
    # time.sleep(1)
    os.system('clear')
    print("******* Audio Menu *******")
    audio_type = input(
"""
[1] produce
[2] record
[3] mix
[0] quit

Please Make a Selection:"""
    )
    if audio_type == "1" or audio_type == "produce" or audio_type == "Produce" or audio_type == "PRODUCE":
      print(Artist_Name)
      print(Project_Name)
      print("AudioType: Produce")
      print(Artist_Name/Project_Name, "AudioType: Produce")
      print()
    elif audio_type == "2" or audio_type == "record" or audio_type == "Record" or audio_type == "RECORD":
      print("AudioType: Record")
      print()
    elif audio_type == "3" or audio_type == "mix" or audio_type == "Mix" or audio_type == "MIX":
      print("AudioType: Mix")
      print()
    else:
      quit()
def image_project():
    # time.sleep(1)
    os.system('clear')
    print("******* Graphic Menu *******")
    image_project = input(
"""
[1] cover
[2] logo
[3] icon
[0] quit

Please Make a Selection:"""
    )
    if image_project == "1" or image_project == "cover" or image_project == "Cover" or image_project == "COVER":
      print("GraphicType: Cover")
      print()
    elif image_project == "2" or image_project == "logo" or image_project == "Logo" or image_project == "LOGO":
      print("GraphicType: Logo")
      print()
    elif image_project == "3" or image_project == "icon" or image_project == "Icon" or image_project == "ICON":
      print("GraphicType: Icon")
      print()
    else:
      quit()
def video_project():
    # time.sleep(1)
    os.system('clear')
    print("******* Video Menu *******")
    video_project = input(
"""
[1] Social Media
[2] option2
[0] quit

Please Make a Selection:"""
    )
    if video_project == "1" or video_project == "social" or video_project == "Social" or video_project == "SOCIAL":
      print("VideoType: Social")
      print()
    elif video_project == "2" or video_project == "2" or video_project == "2" or video_project == "2":
      print("VideoType: option2")
      print()
    else:
      quit()
def web_project():
    # time.sleep(1)
    os.system('clear')
    print("******* Web Menu *******")
    web_project = input(
"""
[1] HTML
[2] option2
[0] quit

Please Make a Selection:"""
    )
    if web_project == "1" or web_project == "html" or web_project == "HTML":
      print("WebType: HTML")
      print()
    elif web_project == "2" or web_project == "2" or web_project == "2" or web_project == "2":
      print("WebType: option2")
      print()
    else:
      quit()
def quit():
    print("Quiting Current Program")
    time.sleep(.5)
    print("Goodbye")
    time.sleep(.5)
    sys.exit()
project_type()
