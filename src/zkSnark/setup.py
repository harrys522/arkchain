# This module will handle all zk-snark setup code.
# TEMP: For now this is our testing sandbox to develop the first zk-snark system prototype.

import libsnark.alt_bn128 as libsnark
import hashlib

class trusted_setup:
    def __init__(self):
        # Vars
        self.protob = libsnark.ProtoboardPub()
        self.in_v = libsnark.PbVariable()
        self.in_t = libsnark.PbVariable()
        
        # config
        self.in_v.allocate(self.protob)
        self.in_t.allocate(self.protob)

        

    """
    The setup function will take in an input t(x) 
    """
    def setup(self):
        # Builds the SNARK stack
        
        # Flattening + Arithmetic
        # R1CS
        # QAP


        pass

    def define_constraints(self):
        # Define the rank 1 constraint system
        self.protob.add_r1cs_constraint()
        pass

    def generate_secrets(self):
        pass

    

