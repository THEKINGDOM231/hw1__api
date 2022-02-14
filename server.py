from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

firstnumber=10
secondnumber=30
outcome=0
calculate = []

@app.route('/calculator/firstnumber',methods = ['GET'])
def getfirstnumber():
   return jsonify({"firstnumber":firstnumber});

@app.route('/calculator/secondnumber',methods = ['GET'])
def getfirstnumber():
   return jsonify({"secondnumber":secondnumber});

@app.route('/calculator/calculate',methods = ['GET'])
def getHistory():
   return jsonify(calculate);

@app.route('/calculator/add',methods = ['POST'])
def deposit():
   global firstnumber
   global secondnumber
   global outcome
   calculate = request.get_json()
   calculate["type"] = "add"
   calculate["time"] = datetime.now()
   outcome = firstnumber + secondnumber
   calculate.append(calculate)
   return jsonify({"outcome":outcome});

@app.route('/calculator/minus',methods = ['POST'])
def withdraw():
   global firstnumber
   global secondnumber
   global outcome
   calculate = request.get_json()
   calculate["type"] = "minus"
   calculate["time"] = datetime.now()
   outcome = firstnumber - secondnumber
   calculate.append(calculate)
   return jsonify({"outcome":outcome});

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=8030, debug = True)
