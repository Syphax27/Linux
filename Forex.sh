curl https://www.gemini.com/prices/solana > /home/ec2-user/Project_Linux/forex_cs.txt
prix=$(cat /home/ec2-user/Project_Linux/forex_cs.txt | grep -oP '(?<="sc-1379d271-0 gUFeSW sc-1e2d8969-7 jwmoyb"><span>)[^<]+'| tr -d '$')
echo "$(date),$prix" >> /home/ec2-user/Project_Linux/prix.csv
sudo fuser -k 8050/tcp 
/usr/bin/python3 /home/ec2-user/Project_Linux/syphax_board.py
