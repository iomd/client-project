#21. Make Directory

#‘Mkdir’ is a command used to create a new directory. This command means ‘make directory’. Create a file named ‘make_directory.sh’. After that, input a code that will create a new directory. Bash will create a new directory for you.

#!/bin/bash

echo "Input a new directory name"
read newdir
`mkdir $newdir`