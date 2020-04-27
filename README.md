# TutorPlatform

An Online Market place project based on TDD（Test Driven Development)
一个基于TDD(测试驱动开发)的线上交易电商项目 

## Description
## 简介
This project involves DjangoRestFramework, Channels, Redis, and Vue.js, uses Github CI for Continuous Integration.
这个项目使用了 DjangoRestFramework 框架，Channels,Redis, 以及 Vue.js， 并且使用 Github CI 持续集成
## Requirements
## 依赖
### Backend
### 后端
In order to run this project, you need to install all the requirements, you can do this through one line of code.
为了运行这个项目， 你需要安装全部的依赖，你可以通过一下代码实现
```
pip3 install -r requirements.txt
```

Since it is developed in Python3, so it is recommanded to use pip3 to install the requirements.
This project also involves using Channels and Redis to implement the real time chat functionality, if you haven't done so, you need to install [Redis](https://redis.io/)
因为这个项目使用python3 编写，因此推荐使用pip3 安装所有依赖。
这个项目同样使用了Channels 和 Redis 来实现实时聊天功能， 如果你还没有安装， 你需要安装 [Redis](https://redis.io/)
#### If you are using Linux
#### 如果你在使用Linux
```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make
```
#### If you are using Mac, you can install Redis through a package manager called [Homebrew](https://brew.sh/)
#### 如果你在使用Mac OSX， 你可以安装Redis 通过[Homebrew](https://brew.sh/)
```
brew install redis
```
#### If you are using Windows, you can install Redis from [here](https://github.com/dmajkic/redis/downloads)
#### 如果你使用Windows，你可以安装Redis 通过[这里](https://github.com/dmajkic/redis/downloads)
### Frontend
### 前端
For frontend, you need install [node.js](https://nodejs.org/en/) and [npm](https://www.npmjs.com/)
After install node.js, change to Frontend directory, and install all the dependencies
至于前端， 你需要安装[node.js](https://nodejs.org/en/) 和 [npm](https://www.npmjs.com/)
在安装 node.js 之后， 切换至前端文件夹， 并且安装所有依赖
```
cd Frontend
npm install
```

## How to run
## 如何运行
Once you install all the requirements, you are ready to run the servers.
First, start the Redis server by typing the following command 
当你安装完了所有的依赖，你就准备好了运行的所有要求
首先， 通过以下命令启动 Redis 服务器
```
redis-server
```
This command is to start the Redis Server that is needed for websocket real time chat functionality
To run backend tests
这个命令是为了启动 Redis 服务器，Redis服务器是使用实时聊天必须开启的
为了运行后端测试
```
python3 manage.py test
```
After that, to start the backend server
之后， 为了启动服务器
```
python3 manage.py runserver
```
For frontend, you need to change to frontend directory first
至于前端， 你需要现切换至前端文件夹
```
cd Frontend
```
To initialize the payment UI
为了初始化支付界面

```
npm install --save vue-card-payment
```

Then, install dependencies
之后，安装所有依赖
```
npm install
```
start the frontend server
开启前端服务器
```
npm run dev
```
