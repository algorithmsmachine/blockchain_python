from hashlib import sha256
import time

class block:
	def __init__ (self, timestamp, data, previousHash = ' '	):
		self.timestamp = timestamp
		self.data = data
		self.previousHash = previousHash
		self.hash = self.calculateHash()

	def calculateHash(self):
		return sha256((str(self.timestamp) + str(self.data) + str(self.previousHash)).encode()).hexdigest()



class blockchain:
	def __init__(self):
		self.chain = [self.createGenesis()]
        #creation of gensis block
	def createGenesis(self):
		return block(time.ctime(), "genesisBlock", "00000")
                
	def mineBlock(self, data):
		node = block(time.ctime(), data, self.chain[-1].hash)
		# mining a new block to the blockchain
		self.chain.append(node)

	def printBlockchain(self):
		for i in range(len(self.chain)):
			print("\n-----Block ", i ,"---------\n timestamp = "\
				       , self.chain[i].timestamp,"\n data = ", \
				       		self.chain[i].data, "\n previousHash = ",\
				       		 self.chain[i].previousHash,"\n hash = ", \
				       		    self.chain[i].hash)

kaka = blockchain()

data = input()

x=int(input("enter the number of blocks"))

for i in range(0,x-1):
	print("\n\n ----> Mining New Block -->")
	kaka.mineBlock(data)
	
kaka.printBlockchain()
