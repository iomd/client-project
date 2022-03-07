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
mkdir "$Project_Path/$Project_Name/audio"
mkdir "$Project_Path/$Project_Name/audio/archives"
mkdir "$Project_Path/$Project_Name/audio/archives/stems"
mkdir "$Project_Path/$Project_Name/audio/imports"
mkdir "$Project_Path/$Project_Name/audio/exports"
mkdir "$Project_Path/$Project_Name/audio/exports/final"
mkdir "$Project_Path/$Project_Name/audio/exports/unused"
