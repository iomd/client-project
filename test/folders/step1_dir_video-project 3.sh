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
mkdir "$Project_Path/$Project_Name/videos"
mkdir "$Project_Path/$Project_Name/videos/archives"
mkdir "$Project_Path/$Project_Name/videos/imports"
mkdir "$Project_Path/$Project_Name/videos/exports"
mkdir "$Project_Path/$Project_Name/videos/exports/advertisement"
mkdir "$Project_Path/$Project_Name/videos/exports/banner"
mkdir "$Project_Path/$Project_Name/videos/exports/trailer"
mkdir "$Project_Path/$Project_Name/videos/exports/music\ video/"
