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
mkdir "$Project_Path/$Project_Name/docs"
mkdir "$Project_Path/$Project_Name/docs/biz\ cards/"
mkdir "$Project_Path/$Project_Name/docs/contract"