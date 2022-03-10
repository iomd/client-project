#!/bin/bash
#The script written below is used to create a client root directory
echo "Enter Artist Name?";read Artist_Name
echo "Enter Project Name?";read Project_Name
echo $Artist_Name/$Project_Name
mkdir -p $Artist_Name/$Project_Name
