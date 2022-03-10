#!/bin/bash
# SETUP
echo "Enter Project Path?"
read Project_Path
echo "Enter Project Name?"
read Project_Name
echo ""
echo $Project_Path/$Project_Name
echo ""
# CREATE FOLDERS
mkdir "$Project_Path/$Project_Name"
mkdir "$Project_Path/$Project_Name/web/css"
mkdir "$Project_Path/$Project_Name/web/css/scss"
mkdir "$Project_Path/$Project_Name/web/img"
mkdir "$Project_Path/$Project_Name/web/pages"
mkdir "$Project_Path/$Project_Name/web/pages/bookmarks"
mkdir "$Project_Path/$Project_Name/web/scripts"