import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
import src.arkchain as arkchaincore
import src.snark as snark
import hashlib