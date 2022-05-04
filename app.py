#app.py
from flask import Flask, render_template, request, flash
from web3 import Web3

app = Flask(__name__)
app.secret_key = "madmachine"

@app.route("/")
def index():
  flash("Enter Your Ethereum Address")
  return render_template("index.html")

@app.route("/balance", methods=["POST", "GET"])
def getbalance():  
  ETH_address = request.form['name_input']
  balance_of(ETH_address)
  return render_template("index.html")
# def are_we_connect():
#   print(web3_connection.isConnected())

# def latest_block():
#   print(web3_connection.eth.block_number)

# set up virtual environment, lean on Infura node provider
# build a function, take in eth address
# print to command line, wallet balance

def balance_of(ETH_address):
  node_provider = 'https://mainnet.infura.io/v3/4fc224ff182b4b53964bd6cb4cbc1891'
  web3_connection = Web3(Web3.HTTPProvider(node_provider))
  balance = web3_connection.eth.get_balance(ETH_address)
  balance_ETH = web3_connection.fromWei(balance, 'ether')
  flash("Your balance is " +str(balance_ETH)+" ETH")
  return render_template("index.html")
  

# if __name__ == "__main__":
#   app.run(host="127.0.0.1", port = 8000, debug=True)
