#!/bin/bash
# The script written below is used to create a new directory
# project_type_selection.sh
# ----------------------------------------------------------
# client root directory
echo "Enter Artist Name?";read Artist_Name
echo "Enter Project Name?";read Project_Name
echo $Artist_Name/$Project_Name
# mkdir -p $Artist_Name/$Project_Name
clear
echo "Project Types List:"
echo "audio
image
video
web
Enter Project Type:"
read Project_Type
# ----------------------------------------------------------
#if audio project
if [ "$Project_Type" = "audio" ];then
        echo "$Project_Type"
        mkdir -p $Artist_Name/$Project_Name/{archives/exports/{final,stems,unused},Project/{Samples/{Recorded,Processed/{Consolidate,Freeze,Reverse}},{Backup,"Ableton Project Info","Audio Files"}}}
#if image project
elif [ "$Project_Type" = "image" ];then
        echo "$Project_Type"
        mkdir -p $Artist_Name/$Project_Name/{archives,exports/{advertisement,banner,cover,icon},assets/{docs/{bizcards,contract},img/{icon,logo,unsorted}}}
#if video project
elif [ "$Project_Type" = "video" ];then
        echo "$Project_Type"
        mkdir -p $Artist_Name/$Project_Name/{archives,contracts,imports,exports/{advertisment,banner}}
#if web project
elif [ "$Project_Type" = "web" ];then
        echo "$Project_Type"
        mkdir -p $Artist_Name/$Project_Name/web/{pages/bookmarks,assets/{docs/{bizcards,contract},scripts,css/scss,img/{icon,logo,unsorted},video/{advertisment,banner,"music video",unsorted}}}
else
        echo "UNKNOWN SELECTION"
fi
#----------------------------------------------------------
