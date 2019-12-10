# -*- coding: utf-8 -*-
'''
Created on 2019. 12. 10.

@author: admin
'''
'''
장점 : 상시 연결이 아니라서 부하 감소
라이브러리 추가 : install flask
        -> cpu 점유율 낮으며 많은 유저 처리 가능
'''
'''
사용법
@app.route("/hello/<text>/<int:number>",methods=["GET","POST"])
get 방식 : 주소창에 보임
ex)http://127.0.0.1:10000/hello/sekra/123

post 방식 : 주소창에 안보이게 암호화, 일반적인 방법으로 접속 볼가
ex)http://127.0.0.1:10000/
'''
from flask import Flask

app = Flask(__name__)
@app.route("/hello/<text>/<int:number>",methods=["GET","POST"])
def OnHello(text, number):
    return "hi"+text+str(number)

@app.route("/quest/<text>/<int:number>",methods=["GET","POST"])
def OnTest(text, number):
    return "Quest"+text+str(number)

if __name__ == "__main__" : 
    app.run(host="127.0.0.1",port=10000)
