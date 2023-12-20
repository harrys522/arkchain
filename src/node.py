import sys, os
parentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parentdir)
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import hashlib
import arkblock
import consensus
import data_tree
from configparser import ConfigParser
"""
arkchain.py facilitates the network protocol
"""

class node: # A node in ArkChain
    def __init__(self, configpath="./config") -> None:
        self.block = arkblock.ArkBlock(self) 
        #self.blocklist = [] # Blocks aquired externally
        self.local_tree = data_tree.DataTree()
        self.consensus = []
        # Config
        self.config = self.read_config(configpath)

        # Generate a new private key if none is specified
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=4096)
        self.public_key = self.private_key.public_key()
        self.save_key() # Write path to config too.
        self.peers = []

        self.add_data()

    def read_config(self, filepath):
        # parse config to memory. Determines slice, key filepaths etc.
        config = ConfigParser()
        config.read(filepath)
        c = dict()
        # Initialise default values
        c["node_num"] = 0
        c["data_path"] = "./sample_images" # Should be a separate folder so each node has unique data.
        
        for setting, value in config['node'].items():
            c[setting] = value

        return c

    def initiate_consensus(self):
        # Broadcasts current hash of dataTree to the network
        # consensus.initiate()
        new_agreement = consensus.agreement()
        new_agreement.initiate(self.local_tree)
        pass

    def determine_agreement(self, agreement):
        # Configurable rules for agreement
        # if dataTree == myDataTree
        # vote yes
        agreement.decide_consensus()
        pass

    def finalise_consensus(self, agreement):
        # 
        self.consensus.append(agreement)
        pass

    def save_key(self):
        # Write our key to disk for safe keeping

        with open("./keys/privkey"+self.config['node_num']+".pem", "wb") as f:

            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"), # Password to load the node's key.
            ))

    def load_key(self):
        # Load from the disk
        with open("./keys/privkey"+self.config['node_num']+".pem", "wb") as f:

            f.read(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"), # Password to load the node's key.
            ))

    def add_data(self): # Adds data from path specified config
        directory_in_str = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + self.config['data_path'].strip('"')
        print(directory_in_str)
        directory = os.fsencode(directory_in_str)

        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            record = arkblock.verification_record()
            record.dataidentifier = record.file_hash(directory_in_str+filename)
            print(record.dataidentifier)            
            record.proof = record.sign(bytes(record.dataidentifier),self.private_key)
            print(record.dataidentifier, record.proof)
            self.block.add_verification_record(record)
