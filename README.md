# Linux

#Exercice 1 


#question 1
```
[ec2-user@ip-172-31-44-146 ~]$ cd /
```


```
[ec2-user@ip-172-31-44-146 /]$ ls
bin  boot  dev  etc  home  lib  lib64  local  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```


```
[ec2-user@ip-172-31-44-146 /]$ pwd
/
```

```
[ec2-user@ip-172-31-44-146 /]$ mkdir test
mkdir: cannot create directory ‘test’: Permission denied
```


```
[ec2-user@ip-172-31-44-146 /]$ mkdir test
mkdir: cannot create directory ‘test’: Permission denied
```

```
[ec2-user@ip-172-31-44-146 /]$ cd /home
```

```
[ec2-user@ip-172-31-44-146 home]$ cd ~
```

```
[ec2-user@ip-172-31-44-146 ~]$ cd ..
```

```
[ec2-user@ip-172-31-44-146 home]$ cd ..
```

```
[ec2-user@ip-172-31-44-146 /]$ cd ~
```

```
[ec2-user@ip-172-31-44-146 ~]$ mkdir test
```

```
[ec2-user@ip-172-31-44-146 ~]$ cd test
```

```
[ec2-user@ip-172-31-44-146 test]$ pwd 
/home/ec2-user/test
```

#Exo 2 

```
[ec2-user@ip-172-31-44-146 ~]$ touch alexis_bogroff.txt
You have new mail in /var/spool/mail/ec2-user
```

```
[ec2-user@ip-172-31-44-146 ~]$ mv alexis_bogroff.txt notes/
mv: cannot move ‘alexis_bogroff.txt’ to ‘notes/’: Not a directory
```

```
[ec2-user@ip-172-31-44-146 ~]$ mkdir notes
```

```
[ec2-user@ip-172-31-44-146 ~]$ mv alexis_bogroff.txt notes/
```

```
[ec2-user@ip-172-31-44-146 ~]$ mv notes/alexis_bogroff.txt notes/alexis_bogroff_[2023].txt
```

```
[ec2-user@ip-172-31-44-146 ~]$ cp -r notes notes_2022
```

```
[ec2-user@ip-172-31-44-146 ~]$ rm -rv notes
removed ‘notes/alexis_bogroff_[2023].txt’

removed directory: ‘notes’
```

#Exercice 3
#Question1

```
[ec2-user@ip-172-31-44-146 ~]$ touch ~/linux_ex_1/script_1.sh
[ec2-user@ip-172-31-44-146 ~]$ nano ~/linux_ex_1/script_1.sh
[ec2-user@ip-172-31-44-146 ~]$ cat ~/linux_ex_1/script_1.sh
echo "Script running please wait ..."
echo "Done."
```

#Question 2

```
[ec2-user@ip-172-31-44-146 ~]$ chmod +x ~/linux_ex_1/script_1.sh
[ec2-user@ip-172-31-44-146 ~]$ ~/linux_ex_1/script_1.sh
Script running please wait ...
Done.
```


#exo 4.1

```
[ec2-user@ip-172-31-44-146 ~]$ cat ~/linux_ex_1/credentials
hello ^^ 
```

```
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-r--r--r-- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ chmod 444 ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-r--r--r-- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ nano ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ chmod 666 ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rw-rw-rw- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ nano ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ cat ~/linux_ex_1/credentials
hello ^^ 
```

```
[ec2-user@ip-172-31-44-146 ~]$ chmod u+x ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rwxrw-rw- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ chmod o-r ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rwxrw--w- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ chmod 777 ~/linux_ex_1/credentials
```

```
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rwxrwxrwx 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
```


#ex 4.2

```
[ec2-user@ip-172-31-44-146 ~]$ cd /
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo nano .private_file
You have new mail in /var/spool/mail/ec2-user
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo cat .private_file
info bonjour
```

```
[ec2-user@ip-172-31-44-146 /]$ ls -la
total 20
dr-xr-xr-x  18 root root  278 Mar 23 21:45 .
dr-xr-xr-x  18 root root  278 Mar 23 21:45 ..
-rw-r--r--   1 root root    0 Mar  9 20:49 .autorelabel
lrwxrwxrwx   1 root root    7 Mar  8 00:46 bin -> usr/bin
dr-xr-xr-x   4 root root 4096 Mar  8 00:47 boot
drwxr-xr-x  15 root root 2900 Mar 23 21:36 dev
drwxr-xr-x  81 root root 8192 Mar  9 20:49 etc
drwxr-xr-x   3 root root   22 Mar  9 20:49 home
lrwxrwxrwx   1 root root    7 Mar  8 00:46 lib -> usr/lib
lrwxrwxrwx   1 root root    9 Mar  8 00:46 lib64 -> usr/lib64
drwxr-xr-x   2 root root    6 Mar  8 00:46 local
drwxr-xr-x   2 root root    6 Apr  9  2019 media
drwxr-xr-x   2 root root    6 Apr  9  2019 mnt
drwxr-xr-x   4 root root   27 Mar  8 00:47 opt
-rw-r--r--   1 root root   13 Mar 23 21:45 .private_file
dr-xr-xr-x 161 root root    0 Mar 23 21:36 proc
dr-xr-x---   3 root root  103 Mar  9 20:49 root
drwxr-xr-x  28 root root  960 Mar 23 21:36 run
lrwxrwxrwx   1 root root    8 Mar  8 00:46 sbin -> usr/sbin
drwxr-xr-x   2 root root    6 Apr  9  2019 srv
dr-xr-xr-x  13 root root    0 Mar 23 21:36 sys
drwxrwxrwt   8 root root  172 Mar 23 21:36 tmp
drwxr-xr-x  13 root root  155 Mar  8 00:46 usr
drwxr-xr-x  19 root root  269 Mar  9 20:49 var
```

```
[ec2-user@ip-172-31-44-146 /]$ nano .private_file
```

```
[ec2-user@ip-172-31-44-146 /]$ cat .private_file
info bonjour
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo chmod 777 .private_file
```

```
[ec2-user@ip-172-31-44-146 /]$ nano .private_file
You have new mail in /var/spool/mail/ec2-user
```

#4.3

```
[ec2-user@ip-172-31-44-146 /]$ chmod a+rw .private_file
chmod: changing permissions of ‘.private_file’: Operation not permitted
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo chown $USER .private_file
```

```
[ec2-user@ip-172-31-44-146 /]$ chmod a+rw .private_file
```


#4.4

```
[ec2-user@ip-172-31-44-146 /]$ sudo apt update
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo apt upgrade
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo apt install cmatrix
```

```
[ec2-user@ip-172-31-44-146 /]$ cmatrix 
CTRL + C
```

```
[ec2-user@ip-172-31-44-146 /]$ sudo apt install tmux
```

```
[ec2-user@ip-172-31-44-146 /]$ tmux
echo "Hello session 0"
```

```
[ec2-user@ip-172-31-44-146 /]$ cmatrix
```

Ctrl + B + D
Ctrl + B + %

#14
```
tmux list-sessions
```

```
tmux attach-session -t session0
```

-20

```
tmux kill-session -a
tmux list-sessions
```

#ex 4.5

```
cmatrix -h
```


cmatrix -C white
cmatrix -s 5
CTRL + C
cmatrix -s 5 -C blue
man cmatrix
tmux -h
man tmux

[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$
[ec2-user@ip-172-31-44-146 /]$

#TD 2

#1

```
sudo apt update && sudo apt upgrade
```

#2
```
lsb_release -a
```

```
top 
htop
nproc
lscpu | grep 'Cache'
df -h
lsblk
lsusb
hostname
```


#EX 2
#1.
```
x="piri pimpin"
```
#2.
```
echo $x
```
#3.
```
x="$x piri pimpin"
```
#4.
```
mkdir my_programs && cd my_programs
```
#5.
```
echo "echo pilou pilou" > pilou
```
#6.
```
bash pilou
```
#7.
```
chmod +x pilou
```
#8.
```
./pilou
```

#9.
```
echo $PATH
```

#10.
```
export PATH="$PATH:$(pwd)"
```

#11.
```
export PATH
```

#12.
```
cd ~
```

#13.
```
pilou
```

#14.
```
echo 'export PATH="$PATH:$(pwd)"' >> ~/.profile
```

#15.
```
bash
pilou
```

#Ex3

#1.

```
touch say_hello.sh
date +"%c - Hello" >> hellos.txt
```

#2.

```
chmod +x say_hello.sh
```

#Ex4
#1.
```
mkdir hash_checksum
```

#2.

```
cd hash_checksum 
touch .sensible_addresses .sensible_passwords
```

#3.

```
ls
```

#4.

```
echo '#!/bin/bash' > gentle_script.sh
echo 'echo "Have a good day"' >> gentle_script.sh
chmod +x gentle_script.sh
```


#5.

```
./gentle_script.sh
```

#6.

```
sha256sum gentle_script.sh > log_sha
```

#7.

```
echo 'rm -f .sensible*' >> gentle_script.sh
 ```

#8.

```
sha256sum gentle_script.sh >> log_sha
```

#9.

```
./gentle_script.sh
```

#10.

```
ls
```

#11.

```
cat log_shat
```

#Ex5

#1.
```
sudo apt-get install qpdf
```
#2.
```
mkdir compress && cd compress
```

#3.
```
echo "Hello" > hello
```

#4.
```
zlib-flate -compress -level 1 < hello > hello.deflate && echo "hello $(wc -c < hello.deflate)" >> log_compress
```

#5.
```
yes Hello | head -1000 > hello_multiple
```

#6.
```
zlib-flate -compress -level 1 < hello_multiple > hello_multiple.deflate && echo "hello_multiple $(wc -c < hello_multiple.deflate)" >> log_compress
```
#7.

```
for i in $(seq 1 1000); do echo "Hello $i"; done > hello_multiple_i
```

#8.
```
zlib-flate -compress -level 1 < hello_multiple_i > hello_multiple_i.deflate && echo "hello_multiple_i $(wc -c < hello_multiple_i.deflate)" >> log_compress
```
#9.
```
cat log_compress
```


#TD3

#Ex1
#1.
```
ls -l /
```
#2
```
ls -l / | grep bin
```
#3
```
ls -l / | grep bin | awk '{print $5}'
```
#4
```
ls -l / | grep bin | awk '{print $6, $7, $8}'
```
#5
```
ls -l / | grep bin | awk '{print $8"-"$6"-"$7}'
```

#Ex2 
#1.
```
curl https ://en.wikipedia.org/wiki/List_of_cyberattacks > cyberattacks.txt
```
#2
```
grep "meta" cyberattacks.txt
```

#3
```
cat cyberattacks.txt | grep -oP "meta \w*=\"\w*"
```

#4
```
grep -o -E "meta [[:alpha:]]+" cyberattacks.txt | cut -d' ' -f2
```

#5
```
cat cyberattacks.txt | grep -P ’A cyberattack is’
```


#6
```
cat cyberattacks.txt | grep -o -E "<title>.*</title>" | cut -d'>' -f2 | cut -d'-' -f1
cat cyberattacks.txt | grep -P "(?=title).+(?<=/title)"
```

#TD3 Git
#1
```
git --version
```
#2
```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

#3
```
git config --list
```

#Ex 2

#1
```
git init
```
#2
```
ls -la
```

#3
```
git status
```

#4
```
echo "# Test repository" > readme.md
```

#5
```
git status
```
#6
```
git add readme.md
```
#7
```
git status
```
#8
```
git commit -m "Add readme.md"
```
#9
```
git status
```
#10
```
git log
```

#Ex3
#1
```
touch main.py functions.py
```
#2
```
git status
```
#3
```
git add main.py
```
#4
```
git status
```
#5
```
git commit -m "Add main.py"
```
#6
```
git status
```
#7
```
git add functions.py
git commit -m "Add functions.py"
```
#8
```
git status
```
#9
```
git log
```

#Ex 4

#1
```
touch requirements.txt .gitignore .private
```
#2
```
git status
```
#3
```
git add .
```
#4
```
git status
```
#5
```
git commit -m "Add requirements.txt, .gitignore, and .private"
```
#6
```
git status
```
#7
```
git log --oneline
```


#Ex5

#1
```
touch temp.ipynb
```
#2
```
git status
```
#3
```
echo "temp.ipynb" >> .gitignore
```
#4
```
git status
```
#5
```
touch temp.aux temp.log
```
#6
```
git status
```
#7
```
echo "temp.*" > .gitignore
```
#8
```
git status
```
#9
```
echo ".private/" >> .git/info/exclude
```
#Ex6
#1
```
echo " test" >> readme.md
```
#2
```
git add readme.md
```
#3

```
git diff --staged
```
#4
```
git commit -m "changee"
```

#5
```
git diff
```
#6
```
git diff
```
#7
```
echo "test 2" > readme.md
```
#8
```
git diff
```
#Ex7
#1
```
rm -rf *
```
#2
```
git checkout .
```
#3
```
cd ..
cp -R your_project your_project_backup
cd your_project
```




#TD4 LINUX BRANCHES
#exo1
```
git clone <repository URL>                                        
cd <repository name>
``` 
#EX2
```
git checkout -b <your name>                                               
touch <your name>.txt
git add <your name>.txt
git commit -m "Added <your name>.txt file"
git push -u origin <your name>
```

#EX3
```
git checkout master
git merge <your name>
git push origin master
``` 
#EX4
``` 
git checkout <your name>
nano README.md
git add README.md
git commit -m "Edited README.md file"
git checkout master
git pull origin master
git merge <your name>
git add README.md
git commit -m "Resolved merge conflicts"
git push origin master
```
 
#Ex5
``` 
git checkout master
git pull origin master
cat README.md
git checkout <your name>
git merge master
git commit -m "Merged changes from master branch"
git push origin <your name>
```
 
#Ex6
``` 
git branch -d <your name>
git push origin --delete <your name>
```
#EX7
``` 
git checkout master
git pull origin master
git checkout -b <your name>
nano README.md
# Git interactive rebase
## Changing Multiple Commit Messages

To modify a commit that is farther back in your history, you can use interactive rebase. This will allow you to modify any commit message, combine multiple commits into one, or split a commit into multiple commits.

My Name

git add README.md
git commit -m "Clear the whole file, removing all text."
git add README.md
git commit -m "Add a title line 'Git interactive rebase'."
git add README.md
git commit -m "Copy the first paragraph from https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History."
git add README.md
git commit -m "Add the second paragraph from the same page."
git add README.md
git commit -m "Add the first and second paragraphs from the 'Changing Multiple Commit Messages' section in the same page."
git add README.md
git commit -m "Remove the second paragraph from the file."
git add README.md
git commit -m "Add the missing title 'Changing Multiple Commit Messages'."
git add README.md
git commit -m "Add a final line with my name or alias."

git rebase -i HEAD~8

git push -u origin <your name>
``` 
 
#TD Linux API
#Ex1
Exercice 1.1 :
```
curl https://opendomesday.org/api/1.0/county/
curl https://opendomesday.org/api/1.0/place/2346/
curl https://opendomesday.org/api/1.0/manor/181/
```

#Exercice 1.2.
```
curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]'
```
#Exercice 1.3 :
```
derbyshire_place_ids=$(curl -s 'https://opendomesday.org/api/1.0/county/' | jq '.[] | select(.name == "Derbyshire") | .places[]')
for id in $derbyshire_place_ids; do
  curl -s "https://opendomesday.org/api/1.0/place/${id}/" | jq '.manors[]'
done
```
