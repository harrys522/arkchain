from enum import Enum
import pysnark
import datetime
import hashlib

"""
arkchain.py facilitates all chain-related processes which will allow the network to collectively maintain a public ledger.
"""

class verification_record():
    timestamp = datetime.datetime.now()
    dataidentifier = '' # Any identifier, eg. File Hash
    zero_knowledge_proof = '' # Proof of source

class ArkBlock:
    def __init__(self, user):
        self.records = []
        self.origin = user.public_key # How to account for third-party proofs?

    def check_verification_record(self, rec):
        assert type(rec) == type(verification_record)
        assert type(rec[0]) == type(float) # index 0 is timestamp
        assert type(rec[1]) == type(str) # index 1 is identifier
        assert type(rec[2]) == type(str) # index 2 is the Zero-Knowledge Proof

    def add_verification_record(self, rec):
        self.check_verification_record(rec) # Checks correct format of verification_record before adding
        self.records.append(rec) # Append verification_record to the block's record list

    def timestamp(self): # Updates all record timestamp to now
        # Might not be necessary
        pass

class ArkChain:
    def __init__(self) -> None:
        self.chain = []
        self.current_block = None # This is the last finalized block
        self.queue = []

        # ZK-SNARK variables / trusted setup

    


