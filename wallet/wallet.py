#import relevant files or libraries
import os
from constants import *
import subprocess
from dotenv import load_dotenv
import bit
import web3
from bit import Key
from web3 import Web3
from eth_account import Account
from pathlib import Path
from getpass import getpass
import json
#set for local network
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

#import mnemnic from environmental variables
load_dotenv()
mnemonic = os.getenv("MNEMONIC", "insert mnemonic here")

#make a list of the constants associated with string values
#for ethereum ('eth'), bitcoin ('btc'), bitcoin test ('btc-test')
coin_list=[BTCTEST,ETH]


#derive hd wallet address using hd-wallet-drive subprocess
def derive_wallets(mnemonic,coin_list):
    #define a wallet key dictionary to be filled
    coin_wallet_dict={}
    #loop through the coins that are int he object-list called coins
    #get wallet keys for various coin types
    for coin_name in coin_list:
        #use hd-wallet-derive ./derive subprocess
        #need to make subprocess command and get output
        #use mneumonic phrase, coin name, number of wallets desired, and json format
    
        #run the subprocess
        process=subprocess.Popen(f"./derive -g --mnemonic='{mnemonic}' --coin={coin_name} --numdrive=3 --format=json"
        , stdout=subprocess.PIPE, shell=True)
        (output,err)=process.communicate()
        p_status=process.wait()

        #set wallet key to subprocess command output
        wallet_key=output
        wallet_str=wallet_key.decode("UTF-8")


        #append the wallet key list to the walley key dictionary 
        #for the key corresponding to the coin name
        coin_wallet_dict.update({coin_name:wallet_key})
    return coin_wallet_dict

#run the function on mneumonic and coins list defined
output=derive_wallets(mnemonic, coin_list)
#output_json=json.dumps(output)
#wallets=json.loads(output_json)
print(type(output))
#print(output)
#btc-test private key
btc_priv_key=output['btc-test'][2]
btc_test_address=os.getenv("BTC_ADRESS", "insert address here")

#eth address 
eth_address=os.getenv("ETH_ADRESS", "insert address here")



#read the output in json format
#result=json.dumps(output)
#show=json.loads(result)
#print(output)


#function for priv_key_to_account
#convert privkey string to account object
def priv_key_to_account(coin,priv_key):
    if coin=='eth':
        account = web3.Account.from_key(priv_key)
        return account
    elif coin=='btc-test':
        account = bit.PrivateKeyTestnet(priv_key)
        return account



#function to create raw transaction with all metadata to transact
def create_tx(coin,account,to,amount):
    if coin=='eth':
        gasEstimate=w3.eth.estimateGas({
            "from":account.address,
            "to":recipient,
            "value":amount
        })
        
        eth_info={
            "from":account.address,
            "to":recipient,
            "value":amount,
            "gas": gasEstimate,
            "gasPrice":w3.eth.gasPrice,
            "nonce":w3.eth.getTransactionCount(account.address)
        }
        return eth_info
    elif coin=='btc-test':
        return bit.PrivateKeyTestnet.prepare_transaction(account.address,[(to,amount,BTC)])

#function to sign the transaction and send on designated network
def send_tx(coin,account,to,amount):
    if coin=='eth':
        #get raw transaction data
        raw_tx=create_tx(coin,account,to,amount)
        #sign the transaction
        signed_tx=w3.eth.account.sign_transaction(raw_tx)
        #send the transaction
        return w3.eth.sendRawTransactions(signed_tx.rawTransaction)
    elif coin=='btc-test':
        #get raw transaction data
        raw_tx=create_tx(coin,account,to,amount)
        #sign the transaction
        signed=bit.multisig1.sign_transaction(raw_tx)
        #send the transaction
        return bit.NetworkAPI.broadcast_tx_testnet(signed)


