#6. For Loop

#Take a look at the following for loop example. After creating a file named ‘for_sample.sh’, add the script using ‘for loop’. This process will re-occur 12 times. After that, it will display the fields in a single line, as shown below;

#!/bin/bash
for (( counter=12; counter>0; counter-- ))
do
echo -n "$counter "
done
printf "\n"