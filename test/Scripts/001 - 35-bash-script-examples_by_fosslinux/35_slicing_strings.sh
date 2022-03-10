#35. Slicing strings

#The slicing string refers to the reduction of parts of a string. Unlike many programming languages that offer truncation of strings, bash doesn’t provide this feature. Below is an example to make you get a glimpse of what we are talking about. First, create a file named ‘slicing_strings.sh’. Thereafter, execute the created slicing file using the bash command line.
#The output in the script should be ‘Study Smart commands.’ The expansion in parameter takes the formula {VAR_NAME: S: L). in this formula, S shows the starting position, whereas L denotes the length.

#!/bin/bash

Str="Study smart commands with fosslinux"
subStr=${Str:0:20}
echo $subStr
subStr2=${Str:21:35}
echo $subStr2
