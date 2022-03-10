import os,subprocess,datetime
date = datetime.date.today()
Desktop = "/Users/icepitproductions/Desktop"
suffix = " Project"

subprocess.run('clear')

print("Date                =",date)
Producer_Name = input("Enter Producer Name = ")
Project_Name = input("Enter Project Name  = ")
# print("Producer_Name       = ",Producer_Name)
# print("Project_Name        = ",Project_Name)


# Project_Folder_Name = Producer_Name + Project_Name + suffix
# Project_Folder_Name = (date,Producer_Name + Project_Name + suffix)
Project_Folder_Name = (date,Producer_Name + Project_Name + suffix)
print("Project_Folder_Name =",Project_Folder_Name)


Project_var_1 = date,Producer_Name,Project_Name
print("Project_var_1       =",Project_var_1)


Project_Path = Desktop + "/", Project_Folder_Name
print("Project_Path        =",Project_Path)




# os.makedirs(Project_Path)
# print(choice + " % s 'on Desktop' " % type + " by " + Producer_Name)

# ----------------------------------------------------------------
# import datetime

# # date = datetime.datetime.now()
# date = datetime.date.today()
# # print(date)

# # date_time = date. strftime("%m/%d/%Y, %H:%M:%S")
# date_time = date. strftime("%m-%d-%Y")
# # print("date and time:",date_time)

# Producer_Name = input("Enter Producer Name? ")
# Project_Name = input("Enter Project Name ? ")
# # print(Producer_Name)
# # print(Project_Name)

# Desktop = ("/Users/icepitproductions/Desktop")
# suffix = " Project"

# Project_Folder_Name = date_time, (Producer_Name + Project_Name + suffix)
# print(Project_Folder_Name)

# ''' Project_Path = Desktop + "/" + Project_Folder_Name
# # Project_Folder_Name = date - Producer_Name - Project_Name + suffix
# # Project_Folder_Name = (Producer_Name + "[" + date + "]" + " - " + Project_Name + suffix)
# # Project_Folder_Name = (Producer_Name + "| " + " |" + " - " + Project_Name + suffix)
# # Project_Folder_Name = (date)|(Producer_Name + "| " + " |" + " - " + Project_Name + suffix)
# # Project_Folder_Name = (date),(Producer_Name + "| " + " |" + " - " + Project_Name + suffix)
# # Project_Folder_Name = date((Producer_Name + "| " + " |" + " - " + Project_Name + suffix))
# # Project_Folder_Name = date + Producer_Name + Project_Name + suffix
# # Project_Folder_Name = Producer_Name + Project_Name + suffix
# # Project_Folder_Name = date + Producer_Name + Project_Name + suffix

# '''

# Project_Path = Desktop + "/", Project_Folder_Name

# print(Project_Path)

# # os.makedirs(Project_Path)
# # print(choice + " % s 'on Desktop' " % type + " by " + Producer_Name)
