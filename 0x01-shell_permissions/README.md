Shell permissions
0. su == creates a script that switches the current user to the user betty.
1. whoami == prints the effective username of the current user.
2. groups == prints all the groups the current user is part of
3. sudo chown betty hello == changes the owner of the file hello to the user betty.
4. touch hello == creates an empty hello file.
5. chmod 744 ./hello == adds execute permission to the owner of the file hello.
6. chmod u+x,g+x,0+r hello == gives multiple permissions to the hello file.
7. chmod ugo+x hello ==adds execution permission to the owner, the group owner and the other users, to the file hello.
8. chmod 007 hello ==  sets the permission to the file hello,no permission at all to the owner and group: all permissions to other users.
9. chmod 753 hello == sets the mode of the file hello to -rwxr-x-wx.
10. chmod --reference=olleh hello === sets the mode of the file hello the same as olleh’s mode.
11. chmod -R ugo+X . ===  adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.
12. mkdir -m 751 my_dir === creates a directory called my_dir with permissions 751 in the working directory.
13. chgrp school hello === changes the group owner to school for the file hello.
14. chown -hR vincent:staff . === changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
15. chown -h vincent:staff _hello === changes the owner and the group owner of _hello to vincent and staff respectively.
16. chown --from=guillaume betty hello === changes the owner of the file hello to betty only if it is owned by the user guillaume.
17. telnet towel.blinkenlights.nl ==  plays the StarWars IV episode in the terminal. 
