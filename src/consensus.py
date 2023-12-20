import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
#import src.fba.fba_server # Needs to be rewritten as object-oriented
#import src.fba.fba_client
# Use these imports to speed up development
# One quorum slice in prototype

class agreement:
    def __init__(self) -> None:
        self.datatree = None
        self.quorum = [] # List of nodes who agree on data consensus

    def initiate(self, datatree):
        self.datatree = datatree
        # Broadcast datatree to peers

    
    def decide_consensus(self):
        # Pass config file
        # Config var: quorum slice address

        # Compare datatree to local datatree
        return False
    
    def generate_multisig(self):
        # Generate multi-signature from the private keys of all nodes in quorum
        pass
    
    

