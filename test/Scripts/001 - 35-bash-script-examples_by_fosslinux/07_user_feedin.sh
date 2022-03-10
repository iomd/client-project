#7. Get User Input

To get user input from bash, we will use the ‘read’ command. Follow the simple steps below to achieve the expected results. First, create a file named ‘user_feedin.sh’ and include the script below to get the user input. One value will be taken and displayed by combining other string values. As indicated below,

#!/bin/bash
echo "Enter Your Name"
read name
echo "Welcome $name to FossLinux"
