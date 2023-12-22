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
node4 = node(4, configpath='conf4.ini')
slice1 = [node1,node2,node3,node4]

for n in slice1:
    n.local_tree.insert_thread_safe(datetime.now(),n.block)

# Create the user graph
user_graph = create_user_graph(slice1)

### THIS IS JUST EXAMPLE USE CASES OF ADDING PEERS AND BROADCASTING
# Request and add peers for a specific user (In this case node 1)
node1.peers = add_peers(node1, user_graph, num_peers_to_add=3)
node2.peers = add_peers(node2, user_graph, num_peers_to_add=3)
node3.peers = add_peers(node3, user_graph, num_peers_to_add=3)
node4.peers = add_peers(node4, user_graph, num_peers_to_add=3)

newpeerids = []
for n in node1.peers:
    newpeerids.append(n.id)
print(f"New peers for node1: {newpeerids}")

"""
# Broadcast information from a specific user (e.g., node1 and their request hash to peers)
broadcast_information(node2, user_graph, information="REQ cb51dad7a814614594a76d242592129bb9883a9ab7ad03348c14750bb4354907")

# Create datatree
data_tree = DataTree()

# Retrieve sorted elements from the data tree
sorted_elements = data_tree.get_sorted_elements()
"""
node1.verify("/sample_images/pikachu.png", user_graph)
node2.verify("/sample_images/charizard.png", user_graph)
node3.verify("/sample_images/psyduck.png", user_graph)
#node4.verify("/sample_images/charmander.png", user_graph)
