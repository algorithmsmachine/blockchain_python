import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections
import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:


   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)
        # generation of keys 


   @property
   def identity(self):
      return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
    # public key generation for a particular transaction


class Transaction:


    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = datetime.datetime.now()
    #sender details

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
                                        'sender': identity,
                                        'recipient': self.recipient,
                                        'value': self.value,
                                        'time' : self.time
                                        }
        )
    #reciever details

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')
        #digital signature of each transaction

def display_transaction(transaction):
   #for transaction in transactions:
 
   print ('--------------')
   dict = transaction.to_dict()
   print ("sender: " + dict['sender'])
   print ('-----')
   print ("recipient: " + dict['recipient'])
   print ('-----')
   print ("value: " + str(dict['value']))
   print ('-----')
   print ("time: " + str(dict['time']))
   print ('-----')

transactions=[]

#testing

dinesh=Client()
ramesh=Client()
seema=Client()
vijay=Client()


t1=Transaction(
    dinesh,
    ramesh.identity,
    15.0
)


t1.sign_transaction()
transactions.append(t1)


t2=Transaction(
    dinesh,
    seema.identity,
    6.0
)

t2.sign_transaction()
transactions.append(t2)

t3=Transaction(
    dinesh,
    vijay.identity ,
    3.0
)

t3.sign_transaction()
transactions.append(t3)    


for transaction in transactions:
   display_transaction (transaction)
   print ('--------------')


last_block_hash=" "
# hashing dependency for previous blocks
class Block:
   def __init__(self):
      self.verified_transactions = []
      self.previous_block_hash = ""
      self.Nonce = ""

#block 0 =Gensis block
t0=Transaction(
    "Genesis",
    dinesh.identity,
    500.0
)

block0=Block()

block0.previous_block_hash= None
Nonce =None

block0.verified_transactions.append(t0)

digest = hash (block0)
last_block_hash = digest
#print(last_block_hash)

#Block 1 
t1=Transaction(
    dinesh,
    seema.identity,
    250.0
)

block1=Block()

block1.previous_block_hash=last_block_hash
Nonce =None

block1.verified_transactions.append(t1)

digest = hash (block1)
last_block_hash = digest
#print(last_block_hash)

TPCoins=[]
#definfing a block chain to show all the verified transactions
def dump_blockchain (self):
   print ("Number of blocks in the chain: " + str(len (self)))
   for x in range (len(TPCoins)):
      block_temp = TPCoins[x]
      print ("block # " + str(x))
      for transaction in block_temp.verified_transactions:
         display_transaction (transaction)
         print ('--------------')
      print ('=====================================')

TPCoins.append(block0)

#dump_blockchain(TPCoins)

#TPCoins.append(block1)

#dump_blockchain(TPCoins)
#displaying all the blockchains

def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()


def mine(message, difficulty=1):
   prefix = '1' * difficulty
   for i in range(10000):
      digest = sha256(str(hash(message)) + str(i))
      if digest.startswith(prefix):
            print ("after " + str(i) + " iterations found nonce: "+ digest)
            break
   return digest

#mine("test message",2)


last_transaction_index=0
 # considering we only have one mining server present that means it will run only once , otherwise define the value of last_transaction_index =0 for every it
block = Block()
for i in range(3):
   temp_transaction = transactions[last_transaction_index]
   # validate transaction
   # if valid
   block.verified_transactions.append (temp_transaction)
   last_transaction_index += 1

block.previous_block_hash = last_block_hash
block.Nonce = mine (block, 2)
digest = hash (block)
TPCoins.append (block)
last_block_hash = digest
 

dump_blockchain(TPCoins)
