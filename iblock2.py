import hashlib
import json
import time

reward = 10.0

time_stamp=time.ctime()
genesis_block = {

   'previous_hash': '',

    'time_stamp':time_stamp,

   'index': 0,

   'transaction': [],

   'nonce': 23

}

blockchain = [genesis_block]
open_transactions = []
owner = ''

def hash_block(block):

   return hashlib.sha256(json.dumps(block).encode()).hexdigest()

def valid_proof(transactions, last_hash, nonce):

   guess = (str(transactions) + str(last_hash) + str(nonce)).encode()
   guess_hash = hashlib.sha256(guess).hexdigest()
   print(guess_hash)
   return guess_hash[0:1] == '0' #condition digital signature of the block 

def pow():

   last_block = blockchain[-1]
   last_hash = hash_block(last_block)
   nonce = 0
   while not valid_proof(open_transactions, last_hash, nonce):
       nonce += 1
   return nonce

def get_last_value():

   """ extracting the last element of the blockchain list """

   return(blockchain[-1])


def add_value(recipient, sender=owner, amount=1.0):
   time_stamp=time.ctime()
   transaction = {
        'sender': sender,
        'time_stamp':time_stamp,
        'recipient': recipient,
        'amount': amount
    }
   open_transactions.append(transaction)

def mine_block():

   time_stamp=time.ctime()
   last_block = blockchain[-1]
   hashed_block = hash_block(last_block)
   nonce = pow()
   print(nonce)
   reward_transaction = {

           'sender': 'MINING',
           'time_stamp':time_stamp,
           'recipient': owner,
           'amount': reward

       }

   open_transactions.append(reward_transaction)

   block = {

       'previous_hash': hashed_block,
       'index': len(blockchain),
       'time_stamp':time_stamp,
       'transaction': open_transactions,
       'nonce': nonce
   }

   blockchain.append(block)

def get_transaction_value():

   tx_sender=input('Enter the sender of the transaction: ')

   tx_recipient = input('Enter the recipient of the transaction: ')

   tx_amount = float(input('Enter your transaction amount '))
   return tx_sender,tx_recipient, tx_amount

def get_user_choice():

   user_input = float(input("Please give your choice here: "))
   return user_input

def print_block():    
   for block in blockchain:

       print("Here is your block") 
       print(block[-1])

   
while True:

   print("Choose an option")

   print('Choose 1 for adding a new transaction')

   print('Choose 2 for mining a new block')

   print('Choose 3 for printing the blockchain')

   print('Choose any other number if you want to quit')

   user_choice = get_user_choice()

   if user_choice == 1:

       tx_data = get_transaction_value()

       sender ,recipient, amount = tx_data

       add_value(recipient, sender ,amount=amount)

       print(open_transactions)

   elif user_choice == 2:

       mine_block()

   elif user_choice == 3:
       print_block()

   else:

       break

