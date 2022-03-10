!/bin/bash
#The script written below is used to...

echo "input username"
read username
echo "input password"
read password
if [[ ( $username == "main" && $password == "users" ) ]]; then
echo "valid user"
else
echo "invalid user"
fi