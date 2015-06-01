# tornkey

A simple tornado websocket server/listener which sends typed keys back.

## About tornkey

I wanted to do a quick experiment with raw websockets and python keylogging and this is a super simple setup.  I found Tornado web the easier to get running over [Autobahn|Python](https://github.com/tavendo/AutobahnPython).  

If you are looking for a more refined websocket keylogger I would point you to [xss-keylogger](https://github.com/hadynz/xss-keylogger).  I didn't want to depend on socket.io/express/nodejs and I am more comfortable with python.

## Prerequesites

[Tornado web](https://github.com/tornadoweb/tornado)
Python 2.7

## Installation
```bash
git clone https://github.com/binkybear/tornkey.git
cd tornkey
```
Install Tornado web with pip or easy install:
```bash
pip install -r requirements.txt
```
Modify the file static/js/key.js with the port number of the webserver unless you want to leave it default (8888).

## Running
```bash
python server.py [port number]
```

[img]http://i.imgur.com/YSmiLSV.gif[/img]