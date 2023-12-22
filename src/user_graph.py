# make a connected graph of all users in rundemo.py (start with 4 nodes for now)
# The total number of connections (edges of the graph) are scaled accordingly with the number of users (i.e. scaled dynamically)
# the peers of a user are represented by edges that are connected between them
# make a way for a user to request new peers and then add peers for that particular user (in the form of edges in the graph)
# When broadcasting (sharing information across the network) it should start with one user which is then given to only their peers. 
# Then, the peers of that user will share with their peers and so on until the broadcast is complete.
# Note that information broadcasted cannot go backward to peers to previously sent it to current peers)

import networkx as nx

# Function to create a connected graph of users
def create_user_graph(nodes):
    G = nx.Graph()
    
    # Add nodes to the graph
    for user in nodes:
        G.add_node(user)

    # Add edges to represent peers
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            G.add_edge(nodes[i], nodes[j])

    return G

# Function to request and add peers for a specific user
def add_peers(user, graph:nx.Graph, num_peers_to_add=1):
    neighbors = list(graph.neighbors(user))
    new_peers = []

    for n in range(num_peers_to_add):
        if not neighbors:
            break
        peer = neighbors.pop(0)
        new_peers.append(peer)
        graph.add_edge(user, peer)

    

    return new_peers

# Function for broadcasting information across the network
def broadcast_information(user, graph, information):
    print("Node",user.id,"broadcast a request to the network.")
    assert type(graph) == type(nx.Graph())
    peers = set(graph.neighbors(user))
    for peer in peers:
        #print(f"Broadcasting information from {user.id} to {peer.id}")
        # We need to write what the broadcast information is going to be HERE!!!!!!
        peer.message = information


    for peer in peers:
        verified_peers = []
        if peer.process_broadcast():
            verified_peers.append(peer)

    return verified_peers






