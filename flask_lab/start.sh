#! /bin/bash
virtualenv -p python3.5 --no-site-packages flask
cd flask/
source bin/activate #进入环境 
sudo apt-get install pip
pip install -r ../requirements.txt #利用requirement.txt自动配好环境
sudo ln -s ../helloworld.conf /etc/nginx/conf.d/helloworld.conf
sudo rm /etc/nginx/conf.d/default
sudo rm /etc/nginx/sites-enabled/default
sudo nginx
python3 ../run.py&
sleep 3 
python3 ../client.py
sudo nginx -s stop
