## Creating BlockChain
#Step 1 - For Creation first we need to import the Liberaries
import hashlib as hasher    # Hash Liberary
import datetime as date     #Liberary for Date and Time
import pprint               

# Step 2 - Now we need to now Create a Class called Block and define the required Parameters
class Block:
  def __init__( self, index, data, previous_hash ):
    self.index         = index
    self.timestamp     = date.datetime.now()
    self.data          = data
    self.previous_hash = previous_hash
    self.hash          = self.calc_hash()
# The required parameter includes the index, time, Data to store, Unique Hash for current block,
# and the previous block hash.

# Step 3- Now we need to compute the Hash for blocks, to do that we will sum the parameters 

  def calc_hash( self ):
    sha = hasher.sha256()
    sha.update(str(self.index).encode("utf-8") +
               str(self.timestamp).encode("utf-8") +
               str(self.data).encode("utf-8") +
               str(self.previous_hash).encode("utf-8"))
    return sha.hexdigest()

  def __repr__( self ):
        return "Block<\n  index: {},\n  timestamp: {},\n  data: {},\n  previous_hash: {},\n  hash: {}>".format(
          self.index, self.timestamp, self.data, self.previous_hash, self.hash)
# Data

  @staticmethod
  def first( data="Genesis" ):
    return Block( 0, data, "0" )   # Index, Data, Hash for first block

  @staticmethod
  def next( previous, data="Transaction Data..." ):
    return Block( previous.index + 1, data, previous.hash )



#####
## let's get started
##   build a blockchain a block at a time

b0 = Block.first( "Genesis" )
b1 = Block.next( b0, "SKAY" )
b2 = Block.next( b1, "SKAYY" )
b3 = Block.next( b2, "SKAYYY" )


blockchain = [b0, b1, b2, b3]

pprint.pprint( blockchain )
