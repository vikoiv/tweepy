#!/bin/bash

wget https://raw.githubusercontent.com/vikoiv/tweepy/master/conf.json
wget https://raw.githubusercontent.com/vikoiv/tweepy/master/tw.py

echo installing python3-pip
sudo apt install python3-pip

echo installing tweepy 
pip3 install tweepy
