#29. The Wait command

#Linux OS has a built-in command feature that awaits to complete any running process by using a peculiar id to finish that particular assigned task. Therefore, when there is no job id, the wait command will wait for all secondary cycles to complete before returning exiting. Create a file named ‘wait_example.sh’ and add the script below for execution.

#!/bin/bash

echo "Waiting command" &
process_id=$!
wait $process_id
echo "Exited with status $?"
