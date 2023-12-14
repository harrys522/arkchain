from enum import Enum
import pysnark
import datetime
import hashlib

"""
arkchain.py facilitates all chain-related processes which will allow the network to collectively maintain a public ledger.
"""

class zkp_record():
    timestamp = datetime.datetime.now()
    dataidentifier = '' # Any identifier, eg. File Hash
    zero_knowledge_proof = '' # Proof of source
    # public_key = '' # Optional public key allows automatic source identification, reduces privacy but may be necessary.

class ArkBlock:
    def __init__(self):
        self.blockhash = ''
        self.prevblockhash = ''
        self.records = []

    def check_zkp_record(self, rec):
        assert type(rec) == type(zkp_record)
        assert type(rec[0]) == type(float) # index 0 is timestamp
        assert type(rec[1]) == type(str) # index 1 is identifier
        assert type(rec[2]) == type(str) # index 2 is the Zero-Knowledge Proof

    def add_zkp_record(self, rec):
        self.check_zkp_record(rec) # Checks correct format of zkp_record before adding
        self.records.append(rec) # Append zkp_record to the block's record list

    def set_blockhash(self):
        self.blockhash = hashlib.sha256(self) # Buffer API required? 

    def timestamp(self): # Updates all record timestamp to now
        # Might not be necessary
        pass
        


class ArkChain:
    def __init__(self) -> None:
        self.chain = []
        self.current_block = None # This is the last finalized block
        self.init_block() # Move this to change the startup process
        self.queue = []

        # ZK-SNARK variables / trusted setup



    def get_chainlength(self):
        assert self.chain != None
        return len(self.chain)
    
    def get_block(self,blocknumber): # Get block based on block number index.
        return self.chain[blocknumber-1]
    
    def get_previousblock(self): # Find the most recent block
        return self.get_block(self.get_chainlength())

    def init_block(self): # Initialise a new block to add, puts into state where records can be added
        new_block = ArkBlock()
        if self.current_block != None:
            new_block.prevblockhash = self.find_prevhash() # Put previous block hash

        self.nextblock = new_block
        
    def find_prevhash(self): # Returns the hash of the latest block
        chainlen = self.get_chainlength()
        if chainlen < 1 or self.current_block == None:
            return None
        elif chainlen >= 1:
            prevblock = self.get_previousblock()
            return prevblock.blockhash
        else:
            print("Unable to find a valid previous block")
            return "Error"

    def process_block(self):
        if self.nextblock == None:
            self.init_block()

        queue = self.queue.copy()

        count = 0 # Only do 50 records off the queue per process
        for i in queue:
            self.nextblock.records.append(i)
            self.queue.remove(i)
            count+=1
            if count >= 50:
                break
            
        self.finalise_block()

    def finalise_block(self): #
        #print(self.nextblock)
        assert isinstance(self.nextblock, ArkBlock)

        if self.current_block != None:
            print(len(self.nextblock.records))
            #self.nextblock.set_blockhash() # Generate blockhash

        self.chain.append(self.nextblock) # Add to chain[]
        self.update_currentblock() # Update current_block 
        self.nextblock = None

        print("Added %d records to the chain" % len(self.current_block.records))

    def update_currentblock(self):
        self.current_block = self.get_previousblock()

    def run(self): # Deprecated to ../run.py
        self.init_block()
        self.add_to_queue()
        self.process_block()

    def add_to_queue(self): # Test function to simulate zkp records being added.
        for i in range(0,5):
            newrec = zkp_record()
            newrec.dataidentifier = i
            newrec.zero_knowledge_proof = i
            self.queue.append(newrec)
