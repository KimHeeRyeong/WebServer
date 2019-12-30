'''
Created on 2019. 12. 10.

@author: admin
'''
import json
from flask import Flask
import random

app=Flask(__name__)

coin = 100
nowLevel = 1

@app.route("/hello")
def OnHello():
    return "hi"

@app.route("/json/<text>/<int:number>")
def OnJson(text, number):
    ts = dict()
    ts["text"] = text
    ts["number"] = number
    jsonStr = json.dumps(ts)
    return jsonStr
@app.route("/start")
def OnStart():
    global coin
    coin = 100
    global nowLevel
    nowLevel = 1
    
    ts = dict()
    ts["coin"] = coin
    ts["nowLevel"] = nowLevel
    ts["strengthCoin"] = (nowLevel+9)//10
    ts["sellCoin"] = 0
    jsonStr = json.dumps(ts)
    return jsonStr

@app.route("/strength")
def OnStrength():
    global coin
    global nowLevel
    
    strengthCoin = (nowLevel+9)//10
    coin-=strengthCoin
    sellCoin = 0
    
    ts = dict()
    randNum = random.randrange(1,101)
    if randNum<100-nowLevel:
        ts["result"] = True
        nowLevel+=1
        sellCoin=(nowLevel-1)*(((nowLevel+9)//10)+1)
        
    else :
        ts["result"] = False
        nowLevel = 1
        sellCoin = 0
    
    ts["coin"] = coin
    ts["nowLevel"] = nowLevel
    ts["strengthCoin"] = (nowLevel+9)//10
    ts["sellCoin"] = sellCoin
    jsonStr = json.dumps(ts)
    return jsonStr

@app.route("/sell")
def OnSell():
    global coin
    global nowLevel
    
    sellCoin=(nowLevel-1)*(((nowLevel+9)//10)+1)
    coin+=sellCoin
    nowLevel = 1
    
    ts = dict()
    ts["coin"] = coin
    ts["nowLevel"] = nowLevel
    ts["strengthCoin"] = (nowLevel+9)//10
    ts["sellCoin"] = 0
    jsonStr = json.dumps(ts)
    return jsonStr

if __name__=="__main__":
    app.run(host="localhost", port=10000)
