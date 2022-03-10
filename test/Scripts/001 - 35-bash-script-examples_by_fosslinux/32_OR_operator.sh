#32. The OR Operator

#This is a great bash scripting construct that aids in creating complex logic in scripts. This construct works slightly differently than the ‘AND’ operator because it either returns true whenever the operands outcome is true. On the other hand, the ‘or’ operator only returns false whenever both the operands are false. Check the sample below for more elaboration. To find out about this construct, create a file named ‘OR_operator.sh’ and complete its execution using the command line.

#!/bin/bash

echo -n "Enter any number:"
read n
if [[ ( $n -eq 5 || $n -eq 30 ) ]]
then
echo "You won"
else
echo "You lost!"
fi
