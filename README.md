# Linux

DASHBOARD : http://35.180.111.251:8050/

Le dashboard a ete réalisé en recuperant le prix de la cryptomonnaie Solana depuis le site www.gemini.com.
J'ai recontré avec le choix de l'information dynamique, en effet
j'avais tout d'abord opté pour un indice forex Gbp Usd cependant je me suis rendu compte que les marchés etaient ouverts seulement 5 jours sur 7 donc j'avais 
des resultats constants le week end car le prix ne bougeait pas donc contraignant pour l'etude de mon projet,c'est pourquoi je me suis dirigé vers une info plus dynamique une crypto car il n'y a pas d'interruption.
Un graphique est présent pour montrer l'evolution du prix du solana au cours du temps.Vous pouvez glisser selon l'axe des abscisses pour visualiser les informations anciennes ou recentes à votre guisee
Un tableau recapitulatif de metriques est aussi présent pour indiquer differentes valeurs : 
-le prix minimum, le prix maximum
-le prix d'ouverture, le prix de cloture
-la volatilite et les rendements
Le dashboard recupere le prix du solana toutes les 5 min et affiche en conséquence ses informations relatives continuellement.
Je n'ai pas réussi à actualiser correctement à 20h  le tableau recapitulatif, j'avais tenté une approche en prenant en compte un intervalle entre le jour précedent à 20h01 jusqu au jour d'apres à 19h59 pour afficher une actualisation du tableau mais par par contrainte technique je n'ai pas aboutit à cela mais il s'agissait d'une approche viable je pense.







#Exercice 1 


#question 1
```
[ec2-user@ip-172-31-44-146 ~]$ pwd
```

#question 2

```
[ec2-user@ip-172-31-44-146 ~]$ ls
bin  boot  dev  etc  home  lib  lib64  local  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

#question 3

```
[ec2-user@ip-172-31-44-146 ~]$ pwd
/
```

#question 4

```
[ec2-user@ip-172-31-44-146 ~]$ mkdir test
mkdir: cannot create directory ‘test’: Permission denied
```

#question 4
```
[ec2-user@ip-172-31-44-146 ~]$ mkdir test
mkdir: cannot create directory ‘test’: Permission denied
```

#question 5

```
[ec2-user@ip-172-31-44-146 ~]$ cd ..
```




#question 6

```
[ec2-user@ip-172-31-44-146 ~]$ cd ..
```

#question 7

```
[ec2-user@ip-172-31-44-146 home]$ pwd
```

#question 8

```
[ec2-user@ip-172-31-44-146 /]$ cd ..
```

#question 9

```
[ec2-user@ip-172-31-44-146 ~]$ cd
[ec2-user@ip-172-31-44-146 ~]$ pwd
```

#question 10

```
[ec2-user@ip-172-31-44-146 ~]$ cd test
```

#question 11

```
[ec2-user@ip-172-31-44-146 test]$ pwd 
/home/ec2-user/test
```

#question 11

```
[ec2-user@ip-172-31-44-146 test]$ pwd 
/home/ec2-user/test

```

#Exo 2 

#question 1
```
[ec2-user@ip-172-31-44-146 test]$cd
```

#question 2
```
[ec2-user@ip-172-31-44-146 ~]$cd
/home/ec2-user
```


#question 3
```
[ec2-user@ip-172-31-44-146 ~]$ mkdir linux_ex_1
```

#question 4
```
[ec2-user@ip-172-31-44-146 ~]$ cd linux_ex_1
[ec2-user@ip-172-31-44-146 linux_ex_1]$

```

#question 5

```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ touch syphax_benhamouche.txt
You have new mail in /var/spool/mail/ec2-user
```

#question 6
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ mkdir notes
```

#question 7
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ mv syphax_benhamouche.txt /home/ec2-user/linux_ex_1/notes
```

#question 8
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$cd notes
[ec2-user@ip-172-31-44-146 notes]$mv syphax_benhamouche.txt syphax_benhamouche_2023.txt
```

#question 9
```
[ec2-user@ip-172-31-44-146 notes]$ cd ..
[ec2-user@ip-172-31-44-146 linux_ex_1]$cp -R notes notes_2022
```

#question 10
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ rm -rv notes
removed ‘syphax_benhamouche_2023.txt'
removed directory: ‘notes’
```

#Exercice 3

#Question1
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ nano script_1.sh
echo "Script running please wait ..."
echo "Done."
```

#Question 3
```
Ctrl + x, Y , Enter
```

#Question 4 

```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ cat script_1.sh
```

#Question 5
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ chmod +x script_1.sh
[ec2-user@ip-172-31-44-146 linux_ex_1]$ ./script_1.sh
Script running please wait ...
Done.
```


#exo 4.1

#Question1
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ nano credentials
"wrote :'hello ^^'" 
```
#b
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ cat credentials
```

#c

```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ ls -l credentials
-rw-rw-r-- 1 ec2-user ec2-user 8 Feb 19 21:26 credentials
```

#Question2a
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ chmod a=r credentials
[ec2-user@ip-172-31-44-146 linux_ex_1]$ ls -l credentials
-r--r--r-- 1 ec2-user ec2-user 8 Feb 19 21:26 credentials
```

#Question2b
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ nano credentials
[ec2-user@ip-172-31-44-146 linux_ex_1]$ cat credentials
hello^^
hello hello^^
```

#Question3a
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ chmod a+rw credentials
[ec2-user@ip-172-31-44-146 linux_ex_1]$ ls -l credentials
-rw-rw-rw- 1 ec2-user ec2-user 8 Feb 19 21:30 credentials
```

#Question3b
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ nano credentials
```


#Question3c
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ cat credentials
```

```
[ec2-user@ip-172-31-44-146 linux_ex_1]$ chmod u+x credentials
[ec2-user@ip-172-31-44-146 linux_ex_1]$ ls -l credentials

```



#Execice 4.2

#question1
```
[ec2-user@ip-172-31-44-146 linux_ex_1]$  cd /
```

#question2a
```
[ec2-user@ip-172-31-44-146 /]$ sudo nano .private_file
You have new mail in /var/spool/mail/ec2-user
```

#question2b
```
[ec2-user@ip-172-31-44-146 /]$ cat .private_file
info bonjour
```

#question2c
```
[ec2-user@ip-172-31-44-146 /]$ ls -la
total 20
```
#question3a nothing 
#question3b nothing

#question 4a
```
[ec2-user@ip-172-31-44-146 /]$ sudo nano .private_file
```

#question4b
```
[ec2-user@ip-172-31-44-146 /]$ cat .private_file
```

#question5a
```
[ec2-user@ip-172-31-44-146 /]$ sudo chmod a+rwx .private_file
```

#question5b
```
[ec2-user@ip-172-31-44-146 /]$ cat .private_file
```

#Exercice 4.3

#question1
```
[ec2-user@ip-172-31-44-146 /]$ chmod 666 .private_file
```

#Question 2
```
[ec2-user@ip-172-31-44-146 /]$ chown $USER .private_file
```



#Exercice 4.4

#question 1
```
[ec2-user@ip-172-31-44-146 /]$ sudo apt update
```

#question 2
```
[ec2-user@ip-172-31-44-146 /]$ sudo apt upgrade
```

#question 3
```
[ec2-user@ip-172-31-44-146 /]$ sudo apt install cmatrix
```

#question 4
```
[ec2-user@ip-172-31-44-146 /]$ cmatrix 
```

#question 5
```
CTRL + C
```

#question 6
```
[ec2-user@ip-172-31-44-146 /]$ sudo apt install tmux
```

#question 7
```
[ec2-user@ip-172-31-44-146 /]$ tmux
```


#question 8
```
echo "Hello session 0"
```



#question 9
```
cmatrix
```

#question 10
```
Ctrl + B + D
```

#question 11
```
Ctrl + B + %
```

#question14
```
tmux list-sessions
```

#question15
```
tmux attach-session -t session0
```

#question20
```
tmux kill-session -a
```

#question20
```
tmux list-sessions
```

#ex 4.5

#question 1
```
cmatrix -h
```


#question 2
```
cmatrix -C white
```
#question 3
```
cmatrix -s 5
```

#question 4

```
CTRL + C
```

#question 5
```
cmatrix -s 5 -C blue
```

#question 6
```
man cmatrix
```

#question 7
```
tmux -h
```

#question 8
```
man tmux
```



####TD 2
#Exercice 1

#question1

```
sudo apt update && sudo apt upgrade
```

#question2
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
#question 1.
```
x="piri pimpin"
```
#question2.
```
echo $x
```
#question3.
```
x="$x piri pimpin"
```
#question4.
```
mkdir my_programs && cd my_programs
```
#question5.
```
echo "echo pilou pilou" > pilou
```
#question6.
```
bash pilou
```
#question7.
```
chmod +x pilou
```
#question8.
```
./pilou
```

#question9.
```
echo $PATH
```

#question10.
```
export PATH="$PATH:$(pwd)"
```

#question11.
```
export PATH
```

#question12.
```
cd ~
```

#question13.
```
pilou
```

#question14.
```
echo 'export PATH="$PATH:$(pwd)"' >> ~/.profile
```

#question15.
```
bash
pilou
```

##Exercice 3

#question1.

```
touch say_hello.sh
date +"%c - Hello" >> hellos.txt
```

#question2.

```
chmod +x say_hello.sh
```

##Exercice4

#question1.
```
mkdir hash_checksum
```

#question2.

```
cd hash_checksum 
touch .sensible_addresses .sensible_passwords
```

#question3.

```
ls
```

#question4.

```
echo '#!/bin/bash' > gentle_script.sh
echo 'echo "Have a good day"' >> gentle_script.sh
chmod +x gentle_script.sh
```


#question5.

```
./gentle_script.sh
```

#question6.

```
sha256sum gentle_script.sh > log_sha
```

#question7.

```
echo 'rm -f .sensible*' >> gentle_script.sh
 ```

#question8.

```
sha256sum gentle_script.sh >> log_sha
```

#question9.

```
./gentle_script.sh
```

#question10.

```
ls
```

#question11.

```
cat log_shat
```

##Exercice 5

#question1.
```
sudo apt-get install qpdf
```
#question2.
```
mkdir compress && cd compress
```

#question3.
```
echo "Hello" > hello
```

#question4.
```
zlib-flate -compress -level 1 < hello > hello.deflate && echo "hello $(wc -c < hello.deflate)" >> log_compress
```

#question5.
```
yes Hello | head -1000 > hello_multiple
```

#question6.
```
zlib-flate -compress -level 1 < hello_multiple > hello_multiple.deflate && echo "hello_multiple $(wc -c < hello_multiple.deflate)" >> log_compress
```
#question7.

```
for i in $(seq 1 1000); do echo "Hello $i"; done > hello_multiple_i
```

#question8.
```
zlib-flate -compress -level 1 < hello_multiple_i > hello_multiple_i.deflate && echo "hello_multiple_i $(wc -c < hello_multiple_i.deflate)" >> log_compress
```
#question9.
```
cat log_compress
```


###TD3

#Ex1
#question1.
```
ls -l /
```
#question2
```
ls -l / | grep bin
```
#question3
```
ls -l / | grep bin | awk '{print $5}'
```
#question4
```
ls -l / | grep bin | awk '{print $6, $7, $8}'
```
#question5
```
ls -l / | grep bin | awk '{print $8"-"$6"-"$7}'
```

#Exercice 2
#question1.
```
curl https ://en.wikipedia.org/wiki/List_of_cyberattacks > cyberattacks.txt
```
#question2
```
grep "meta" cyberattacks.txt
```

#question3
```
cat cyberattacks.txt | grep -oP "meta \w*=\"\w*"
```

#question4
```
grep -o -E "meta [[:alpha:]]+" cyberattacks.txt | cut -d' ' -f2
```

#question5
```
cat cyberattacks.txt | grep -P ’A cyberattack is’
```


#question6
```
cat cyberattacks.txt | grep -o -E "<title>.*</title>" | cut -d'>' -f2 | cut -d'-' -f1
cat cyberattacks.txt | grep -P "(?=title).+(?<=/title)"
```

#TD3 Git
#question1
```
git --version
```
#question2
```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

#question3
```
git config --list
```

#Ex 2

#question1
```
git init
```
#question2
```
ls -la
```

#question3
```
git status
```

#question4
```
echo "# Test repository" > readme.md
```

#question5
```
git status
```
#question6
```
git add readme.md
```
#question7
```
git status
```
#question8
```
git commit -m "Add readme.md"
```
#question9
```
git status
```
#question10
```
git log
```

#Exercice 3
#question1
```
touch main.py functions.py
```
#question2
```
git status
```
#question3
```
git add main.py
```
#question4
```
git status
```
#question5
```
git commit -m "Add main.py"
```
#question6
```
git status
```
#question7
```
git add functions.py
git commit -m "Add functions.py"
```
#question8
```
git status
```
#question9
```
git log
```

#Exercice 4
#question1
```
touch requirements.txt .gitignore .private
```
#question2
```
git status
```
#question3
```
git add .
```
#question4
```
git status
```
#question5
```
git commit -m "Add requirements.txt, .gitignore, and .private"
```
#question6
```
git status
```
#question7
```
git log --oneline
```


#Exercice 5

#question1
```
touch temp.ipynb
```
#question2
```
git status
```
#question3
```
echo "temp.ipynb" >> .gitignore
```
#question4
```
git status
```
#question5
```
touch temp.aux temp.log
```
#question6
```
git status
```
#question7
```
echo "temp.*" > .gitignore
```
#question8
```
git status
```
#question9
```
echo ".private/" >> .git/info/exclude
```
#Exercice6
#question1
```
echo " test" >> readme.md
```
#question2
```
git add readme.md
```
#question3

```
git diff --staged
```
#question4
```
git commit -m "changee"
```

#question5
```
git diff
```
#question6
```
git diff
```
#question7
```
echo "test 2" > readme.md
```
#question8
```
git diff
```
#Exercice 7
#question1
```
rm -rf *
```
#question2
```
git checkout .
```
#question3
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
