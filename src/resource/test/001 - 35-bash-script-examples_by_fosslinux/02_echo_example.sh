#2. Echo commands

#echo commands have numerous options for selection. For instance, there is an addition of a new line by default if you use the ‘echo’ command without any other option. Alternatively, you can use ‘-n’ to print any text without a new line. Make use of the ‘-e’ command to remove backslash characters from the given output. To demonstrate this, create a bash file named ‘echo_example.sh’. After that, add the script below

#!/bin/bash
Echo “printing text with newline”
Echo -n “printing text without newline”
Echo -e “\nRemoving \t backslash \t characters\