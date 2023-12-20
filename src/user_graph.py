# make a connected graph of all users in rundemo.py (start with 4 nodes for now)
# The total number of connections (edges of the graph) are scaled accordingly with the number of users (i.e. scaled dynamically)
# the peers of a user are represented by edges that are connected between them
# make a way for a user to request new peers and then add peers for that particular user (in the form of edges in the graph)
# When broadcasting (sharing information across the network) it should start with one user which is then given to only their peers. 
# Then, the peers of that user will share with their peers and so on until the broadcast is complete.
# Note that information broadcasted cannot go backward to peers to previously sent it to current peers)

import pickle
import sys
import os
import networkx as nx
from node import node
from data_tree import DataTree

# Function to create a connected graph of users
def create_user_graph(nodes):
    G = nx.Graph()

    # Add nodes to the graph
    for user in nodes:
        G.add_node(user.id)

    # Add edges to represent peers
    ### this is adding edges of all nodes to other nodes (not really efficient, ask Harry)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            G.add_edge(nodes[i].id, nodes[j].id)

    return G

# Function to request and add peers for a specific user
def add_peers(user, graph, num_peers_to_add=1):
    neighbors = list(graph.neighbors(user.id))
    new_peers = []

    for _ in range(num_peers_to_add):
        if not neighbors:
            break
        peer = neighbors.pop(0)
        new_peers.append(peer)
        graph.add_edge(user.id, peer)

    return new_peers

# Function for broadcasting information across the network
def broadcast_information(user, graph, information):
    visited = set()
    queue = [user.id]

    while queue:
        current_user = queue.pop(0)
        visited.add(current_user)

        # Broadcast information to the peers of the current user
        peers = set(graph.neighbors(current_user)) - visited
        for peer in peers:
            print(f"Broadcasting information from {current_user} to {peer}")
            # We need to write what the broadcast information is going to be HERE!!!!!!

        # Add unvisited peers to the queue for further broadcasting
        queue.extend(peers - set(queue))





