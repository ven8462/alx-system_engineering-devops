Shell permissions
0. su == creates a script that switches the current user to the user betty.
1. whoami == prints the effective username of the current user.
2. groups == prints all the groups the current user is part of
3. sudo chown betty hello == changes the owner of the file hello to the user betty.
4. touch hello == creates an empty hello file.
5. chmod 744 ./hello == adds execute permission to the owner of the file hello.
6. chmod ug+x , o+r hello == gives multiple permissions to the hello file.
