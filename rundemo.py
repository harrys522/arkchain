import pickle
import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
import src.node as node
from src.arkblock import ArkBlock, verification_record
from src.data_tree import DataTree



node1 = node.node(configpath='conf1.ini')
node2 = node.node(configpath='conf2.ini')
node3 = node.node(configpath='conf3.ini')




# get ArkBlock into sorted data tree 

def upload_arkblock(data_tree, ark_block):
    # Extract timestamp from the first verification record in the ArkBlock
    timestamp = ark_block.records[0].timestamp

    # Insert the ArkBlock into the data tree in a thread-safe manner
    data_tree.insert_thread_safe(timestamp, ark_block)

# Create an instance of DataTree
data_tree = DataTree()

# Create an instance of ArkBlock
ark_block = ArkBlock(node=None)

# Add some verification records to the ArkBlock 
verification_record_1 = verification_record()
verification_record_2 = verification_record()
ark_block.add_verification_record(verification_record_1)
ark_block.add_verification_record(verification_record_2)

# Upload the ArkBlock to the sorted data tree
upload_arkblock(data_tree, ark_block)

# Retrieve sorted elements from the data tree
sorted_elements = data_tree.get_sorted_elements()
