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
mkdir "$Project_Path/$Project_Name/img"
mkdir "$Project_Path/$Project_Name/img/archives"
mkdir "$Project_Path/$Project_Name/img/imports"
mkdir "$Project_Path/$Project_Name/img/exports"
mkdir "$Project_Path/$Project_Name/img/exports/advertisement"
mkdir "$Project_Path/$Project_Name/img/exports/banner"
mkdir "$Project_Path/$Project_Name/img/exports/cover"
mkdir "$Project_Path/$Project_Name/img/exports/icon"
mkdir "$Project_Path/$Project_Name/img/exports/logo"
