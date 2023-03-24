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


#Exercice 3

[ec2-user@ip-172-31-44-146 ~]$ touch ~/linux_ex_1/script_1.sh
[ec2-user@ip-172-31-44-146 ~]$ nano ~/linux_ex_1/script_1.sh
[ec2-user@ip-172-31-44-146 ~]$ cat ~/linux_ex_1/script_1.sh
echo "Script running please wait ..."
echo "Done."

[ec2-user@ip-172-31-44-146 ~]$ chmod +x ~/linux_ex_1/script_1.sh
[ec2-user@ip-172-31-44-146 ~]$ ~/linux_ex_1/script_1.sh
Script running please wait ...
Done.



#exo 4.1


[ec2-user@ip-172-31-44-146 ~]$ cat ~/linux_ex_1/credentials
hello ^^ 
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-r--r--r-- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ chmod 444 ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-r--r--r-- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ nano ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ chmod 666 ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rw-rw-rw- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ nano ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ cat ~/linux_ex_1/credentials
hello ^^ 
[ec2-user@ip-172-31-44-146 ~]$ chmod u+x ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rwxrw-rw- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ chmod o-r ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rwxrw--w- 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ chmod 777 ~/linux_ex_1/credentials
[ec2-user@ip-172-31-44-146 ~]$ ls -l ~/linux_ex_1/credentials
-rwxrwxrwx 1 ec2-user ec2-user 10 Mar 23 21:26 /home/ec2-user/linux_ex_1/credentials


#ex 4.2

[ec2-user@ip-172-31-44-146 ~]$ cd /
[ec2-user@ip-172-31-44-146 /]$ sudo nano .private_file
You have new mail in /var/spool/mail/ec2-user
[ec2-user@ip-172-31-44-146 /]$ sudo cat .private_file
info bonjour
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
[ec2-user@ip-172-31-44-146 /]$ nano .private_file
[ec2-user@ip-172-31-44-146 /]$ cat .private_file
info bonjour
[ec2-user@ip-172-31-44-146 /]$ sudo chmod 777 .private_file
[ec2-user@ip-172-31-44-146 /]$ nano .private_file
You have new mail in /var/spool/mail/ec2-user


#4.3

[ec2-user@ip-172-31-44-146 /]$ chmod a+rw .private_file
chmod: changing permissions of ‘.private_file’: Operation not permitted
[ec2-user@ip-172-31-44-146 /]$ sudo chown $USER .private_file
[ec2-user@ip-172-31-44-146 /]$ chmod a+rw .private_file


#4.4

[ec2-user@ip-172-31-44-146 /]$ sudo apt update
[ec2-user@ip-172-31-44-146 /]$ sudo apt upgrade
[ec2-user@ip-172-31-44-146 /]$ sudo apt install cmatrix
[ec2-user@ip-172-31-44-146 /]$ cmatrix 
CTRL + C

[ec2-user@ip-172-31-44-146 /]$ sudo apt install tmux
[ec2-user@ip-172-31-44-146 /]$ tmux

echo "Hello session 0"
[ec2-user@ip-172-31-44-146 /]$ cmatrix
Ctrl + B + D
Ctrl + B + %

#14
tmux list-sessions

tmux attach-session -t session0

-20 
tmux kill-session -a
tmux list-sessions


#ex 4.5

cmatrix -h

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

TD 2

1
sudo apt update && sudo apt upgrade
2
lsb_release -a

top 
htop
nproc
lscpu | grep 'Cache'
df -h
lsblk
lsusb
hostname

#EX 2
1.
x="piri pimpin"
2.
echo $x
3.
x="$x piri pimpin"
4.
mkdir my_programs && cd my_programs
5.
echo "echo pilou pilou" > pilou
6.
bash pilou
7.
chmod +x pilou
8.
./pilou
9.
echo $PATH
10.
export PATH="$PATH:$(pwd)"
11.
export PATH
12.
cd ~
13.
pilou
14.
echo 'export PATH="$PATH:$(pwd)"' >> ~/.profile
15.
bash
pilou

ex3
1.
touch say_hello.sh

date +"%c - Hello" >> hellos.txt
or
echo "$(date) Hello" >> hellos.txt

2.
chmod +x say_hello.sh


Ex4
1.
mkdir hash_checksum

2.
cd hash_checksum 
touch .sensible_addresses .sensible_passwords

3.
ls

4.
echo '#!/bin/bash' > gentle_script.sh
echo 'echo "Have a good day"' >> gentle_script.sh
chmod +x gentle_script.sh

5.
./gentle_script.sh

6.
sha256sum gentle_script.sh > log_sha

7.
echo 'rm -f .sensible*' >> gentle_script.sh
 
8.
sha256sum gentle_script.sh >> log_sha

9.
./gentle_script.sh

10.
ls

11.
cat log_shat

Ex5

1.
sudo apt-get install qpdf

2.
mkdir compress && cd compress

3.
echo "Hello" > hello

4.
zlib-flate -compress -level 1 < hello > hello.deflate && echo "hello $(wc -c < hello.deflate)" >> log_compress

5.
yes Hello | head -1000 > hello_multiple

6.
zlib-flate -compress -level 1 < hello_multiple > hello_multiple.deflate && echo "hello_multiple $(wc -c < hello_multiple.deflate)" >> log_compress

7.
for i in $(seq 1 1000); do echo "Hello $i"; done > hello_multiple_i

8.
zlib-flate -compress -level 1 < hello_multiple_i > hello_multiple_i.deflate && echo "hello_multiple_i $(wc -c < hello_multiple_i.deflate)" >> log_compress

9.
cat log_compress



TD3

eX1
1.
ls -l /

ls -l / | grep bin

ls -l / | grep bin | awk '{print $5}'

ls -l / | grep bin | awk '{print $6, $7, $8}'

ls -l / | grep bin | awk '{print $8"-"$6"-"$7}'

Ex2 
1.
curl https ://en.wikipedia.org/wiki/List_of_cyberattacks > cyberattacks.txt

grep "meta" cyberattacks.txt

cat cyberattacks.txt | grep -oP "meta \w*=\"\w*"

grep -o -E "meta [[:alpha:]]+" cyberattacks.txt | cut -d' ' -f2

cat cyberattacks.txt | grep -P ’A cyberattack is’

cat cyberattacks.txt | grep -o -E "<title>.*</title>" | cut -d'>' -f2 | cut -d'-' -f1
cat cyberattacks.txt | grep -P "(?=title).+(?<=/title)"


TD3 Git

git --version

git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

git config --list


Ex 2

git init

ls -la

git status

echo "# Test repository" > readme.md

git status

git add readme.md

git status

git commit -m "Add readme.md"

git status

git log


Ex3

touch main.py functions.py

git status

git add main.py

git status

git commit -m "Add main.py"

git status

git add functions.py
git commit -m "Add functions.py"

git status

git log


Ex 4


touch requirements.txt .gitignore .private

git status

git add .

git status

git commit -m "Add requirements.txt, .gitignore, and .private"

git status

git log --oneline


Ex5

touch temp.ipynb

git status

echo "temp.ipynb" >> .gitignore

git status

touch temp.aux temp.log

git status

echo "temp.*" > .gitignore

git status

echo ".private/" >> .git/info/exclude

Ex6

echo " test" >> readme.md

git add readme.md

git diff --staged

git commit -m "changee"

git diff

git diff

echo "test 2" > readme.md

git diff

Ex7

rm -rf *

git checkout .

cd ..

