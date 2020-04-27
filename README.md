# TutorPlatform

Course Project for COMP307 -- Principles of Web Development

| Names | Student ID  |
|:----------------:|:---:|
| Hengxian Jiang   | 260830557 |
| Yizhong Ding    | 260829197 |  
| Junjie Yang       | 260829732  | 

## Description
This project involves Django Rest Framework, Channels, Redis, and Vue.js, uses Github CI for Continuous Integration.

## Requirements
### Backend
In order to run this project, you need to install all the requirements, you can do this through one line of code.
```
pip3 install -r requirements.txt
```

Since it is developed in Python3, so it is recommanded to use pip3 to install the requirements.
This project also involves using Channels and Redis to implement the real time chat functionality, if you haven't done so, you need to install [Redis](https://redis.io/)
#### If you are using Linux
```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```
#### If you are using Mac, you can install Redis through a package manager called [Homebrew](https://brew.sh/)
```
brew install redis
```
#### If you are using Windows, you can install Redis from [here](https://github.com/dmajkic/redis/downloads)

### Frontend
For frontend, you need install [node.js](https://nodejs.org/en/) and [npm](https://www.npmjs.com/)
After install node.js, change to Frontend directory, and install all the dependencies
```
cd Frontend
npm install
```

## How to run
Once you install all the requirements, you are ready to run the servers.
First, start the Redis server by typing the following command 
```
redis-server
```
This command is to start the Redis Server that is needed for websocket real time chat functionality

To run backend tests
```
python3 manage.py test
```
After that, to start the backend server
```
python3 manage.py runserver
```
For frontend, you need to change to frontend directory first
```
cd Frontend
```
Then, start the frontend server
```
npm start
```
To initialize the payment UI
```npm install --save vue-card-payment```
