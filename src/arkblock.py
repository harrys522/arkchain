import datetime
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def sign(message,private_key):
    #message is "A message I want to sign"

    signature = private_key.sign(

        message,

        padding.PSS(

            mgf=padding.MGF1(hashes.SHA256()),

            salt_length=padding.PSS.MAX_LENGTH

        ),

        hashes.SHA256()

    )
    return signature


class verification_record():
    timestamp = datetime.datetime.now()
    dataidentifier = '' # Any identifier, eg. File Hash
    proof = '' # Proof of source

class ArkBlock:
    def __init__(self, node):
        self.records = []
        self.parent = node
        self.source = node.public_key # How to account for third-party proofs? URL-compatible

    def check_verification_record(self, rec):
        assert type(rec) == type(verification_record)
        assert type(rec.timestamp) == type(float)  
        assert type(rec.dataidentifier) == type(str) 
        assert type(rec.proof) == type(str) 

    def add_verification_record(self, rec):
        self.check_verification_record(rec) # Checks correct format of verification_record before adding
        self.records.append(rec) # Append verification_record to the block's record list

    def timestamp(self): # Updates all record timestamp to now
        return datetime.datetime.now()
    
    # Path to node's 'data to be verified'