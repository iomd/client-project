#4. Multiline comment

#In bash, the multiline comment is applicable in different ways. To prove this, create a new bash named, ‘multiline-comment example.sh’, after that, add ‘:’ and “ ’ ” scripts symbols to add a multi-line comment in the script. The following example will execute the square of 2.

#!/bin/bash
: ‘The script written below is used to calculate the square of 2
‘
((area=2*2))
echo $area