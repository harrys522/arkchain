import pickle
import sys, os
from datetime import datetime
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
from src.node import node
from src.data_tree import DataTree
from src.user_graph import *

# Slice 1
node1 = node(1, configpath='conf1.ini')
node2 = node(2, configpath='conf2.ini')
node3 = node(3, configpath='conf3.ini')
#node4 = node.node(configpath='conf4.ini')
slice1 = [node1,node2,node3]

for n in slice1:
    n.local_tree.insert_thread_safe(datetime.now(),n.block)



# Create the user graph
user_graph = create_user_graph(slice1)

### THIS IS JUST EXAMPLE USE CASES OF ADDING PEERS AND BROADCASTING
# Request and add peers for a specific user (In this case node 1)
new_peers = add_peers(node1, user_graph, num_peers_to_add=2)
print(f"New peers for node1: {new_peers}")

# Broadcast information from a specific user (e.g., node1)
broadcast_information(node1, user_graph, information="Sample Information")



# Create datatree
data_tree = DataTree()

# Retrieve sorted elements from the data tree
sorted_elements = data_tree.get_sorted_elements()
