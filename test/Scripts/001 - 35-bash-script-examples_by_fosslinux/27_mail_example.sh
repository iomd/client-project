#27. Send Email

#The ‘mail’ or ‘sendmail’ commands in a bash script are used to send emails. These commands will work efficiently after installing all the necessary packages. For demonstration purposes, create a file named ‘mail_example.sh’.  Use the codes highlighted below to send the intended email.

#!/bin/bash

Recipient=”fosslinux@example.com”
Subject=”inquiries”
Message=”Need anything from fosslinux blogsite?”
`mail -s $Subject $Recipient <<< $Message`