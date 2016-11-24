#!/bin/bash

# Install Docker
sudo apt-get update
sudo apt-get purge "lxc-docker*"
sudo apt-get purge "docker.io*"
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
sudo echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
yes | sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
sudo apt-get update
yes | sudo apt-get install docker-engine
sudo service docker start

# Install Docker-Compose
sudo apt-get -y install python-pip
sudo pip install docker-compose


#set up docker-compose to run without sudo
#not below is not working - need to log off/on ?
#hence i am still using sudo below for docker-compose
sudo groupadd docker
sudo usermod -aG docker $USER
sudo service docker restart # probably should just start the service here for the first time

# seem git is installed by defualt
#sudo apt-get install git

mkdir ~/git
cd ~/git
sudo git clone https://github.com/SPlanzer/NZGOAL_Decision-Tree.git
cd NZGOAL_Decision-Tree
sudo git checkout docker
sudo docker-compose build
sudo docker-compose up #-d






