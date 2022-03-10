#34. Concatenating strings

#With its advanced comfort-ability, bash allows easy implementation of concatenating string. This has been simplified by the example below. For demonstration purposes, create a file named ‘concatenating_strings.sh’ and run the file in the bash command line. You will get an output similar to the one below.

#!/bin/bash

string1="FossLinux"
string2="Blogsite"
string=$string1$string2
echo "$string is a great resource for Linux users to find relevant tutorials."
