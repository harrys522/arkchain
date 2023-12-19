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
        self.block = arkblock.ArkBlock() 
        #self.blocklist = [] # Blocks aquired externally
        self.local_tree = data_tree.DataTree()
        self.consensus = []
        # Config
        self.config = self.read_config(configpath)

        # Generate a new private key if none is specified
        self.private_key = rsa.generate_private_key(public_exponent=65537,key_size=4096)
        self.save_key() # Write path to config too.

    def read_config(self, filepath):
        # parse config to memory. Determines slice, key filepaths etc.
        c = dict()
        # Initialise default values
        c["nodenum"] = 0
        """        
        bfs["slice_address"] = 2
        bfs[""] = 5
        bfs["bf_step"] = 1
        bfs["max_abs_diff"] = 20
        bfs["min_val"] = 0
        bfs["max_val"] = 100       
        bfs["q"] = 2

        # Find settings in bloomfilter.ini
        if self.config == None:
            self.findConfig()

        # Use custom settings if they exist
        for setting, value in self.config["bloomfilter"].items():
            bfs[setting] = int(value)
        """
        for setting, value in self.config.items():
            self.config[setting] = value

        pass

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

        with open("./keys/key.pem"+self.config_nodenum, "wb") as f:

            f.write(self.private_key.private_bytes(

                encoding=serialization.Encoding.PEM,

                format=serialization.PrivateFormat.TraditionalOpenSSL,

                encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"), # Password to load the node's key.

            ))

    def load_key(self):
        # Load from the disk
        with open("./keys/key.pem"+self.config_nodenum, "wb") as f:

            f.read(self.private_key.private_bytes(

                encoding=serialization.Encoding.PEM,

                format=serialization.PrivateFormat.TraditionalOpenSSL,

                encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"), # Password to load the node's key.

            ))

    

