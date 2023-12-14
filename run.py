import pickle
import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
import src.arkchain as arkchaincore
import src.snark
import hashlib

def write_chain(chain):
    file = open('chain', 'wb')
    pickle.dump(chain,file)
    file.close()

def load_chain():
    file = open('chain', 'rb')
    chain = pickle.load(file)
    file.close()
    return chain

def file_hash(file_path):
    """
    Imported code that handles data in a safe way to hash large files in a scalable way.
    Credit: https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
    """
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536) # arbitrary number to reduce RAM usage
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def generate_hashlist(num):
    assert num<803

    directory_in_str = './sample_images'
    directory = os.fsencode(directory_in_str)
    
    count = 0
    hashlist = []

    for file in os.listdir(directory):
        if count >= num:
            break
        filename = os.fsdecode(file)
        if filename.endswith(".png"): 
            hash256 = file_hash("./sample_images/"+filename)
            count+=1
            hashlist.append(hash256) 
        else:
            continue

    return hashlist

hlist = generate_hashlist(100)
arkchain = arkchaincore.ArkChain()

