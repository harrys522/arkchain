import datetime
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import cryptography

class verification_record():
    timestamp = datetime.datetime.now()
    dataidentifier = '' # Any identifier, eg. File Hash
    proof = '' # Proof of source eg. signature

    def file_hash(self, file_path):
   
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as f:
            while True:
                data = f.read(65536) # arbitrary number to reduce RAM usage
                if not data:
                    break
                sha256.update(data)

        return sha256.hexdigest()
    
    def sign(self, message,private_key):
        #message is "A message I want to sign"
        assert type(message)
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

class ArkBlock:
    def __init__(self, node):
        self.records = []
        self.parent = node
        self.name = '' # Could be expanded in features. ie 'source' object that contains methods for verification from alternate parts of the network. ie ws or https integration

    def check_verification_record(self, rec):
        assert type(rec) == type(verification_record())
        #assert type(rec.timestamp) == type(float())  
        assert type(rec.dataidentifier) == type(str()) 
        assert type(rec.proof) == type(str()) 

    def add_verification_record(self, rec):
        #self.check_verification_record(rec) # Checks correct format of verification_record before adding
        self.records.append(rec) # Append verification_record to the block's record list
        #self.records.sort(key=Arkblock.string_key) # Keep records sorted
    
    def find_record(self, file_hash):
        index = self.__binary_search(0, len(self.records) - 1)
        return self.records[index] if index != -1 else None

    def __binary_search(self, left, right, file_hash):
        low, high = left, right

        while low <= high:
            mid = (low + high) // 2
            mid_val = self.records[mid]

            if mid_val == file_hash:
                return mid  # Target found, return the index
            elif mid_val < file_hash:
                low = mid + 1  # Discard the left half
            else:
                high = mid - 1  # Discard the right half

        return -1  # Target not found in the array

        def string_key(file_hash):
            return str(file_hash)

    def timestamp(self): # Updates all record timestamp to now
        return datetime.datetime.now()
    
    # Path to node's 'data to be verified'