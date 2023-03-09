curl https://www.zonebourse.com/cours/devise/BRITISH-POUND-US-DOLLAR-89717/ > /home/ec2-user/Project_Linux/forex_cs.txt
cat /home/ec2-user/Project_Linux/forex_cs.txt | grep -oP '(?<="4"  >)[^<]+' >> /home/ec2-user/Project_Linux/prix.csv
sudo fuser -k 8050/tcp 
/usr/bin/python3 /home/ec2-user/Project_Linux/syphax_board.py
