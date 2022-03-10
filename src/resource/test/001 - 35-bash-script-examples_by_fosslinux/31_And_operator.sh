#31. The AND Operator

#This operator allows the system to check if multiple conditions have been satisfied. This means that all conditions separated by the AND operator must be true for correct execution. Additionally, the ‘&&’ operator is used to denote ‘AND’. To ascertain this, check the example below. First, create a file called ‘And_operator.sh’ then execute it using bash command-line.

#!/bin/bash

echo -n "Input a Number:"
read num
if [[ ( $num -lt 20 ) && ( $num%2 -eq 0 ) ]]; then
echo "It is an Even Number"
else
echo "It is an Odd Number"
fi