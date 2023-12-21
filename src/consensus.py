import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
#import src.fba.fba_server # Needs to be rewritten as object-oriented
#import src.fba.fba_client
# Use these imports to speed up development
# One quorum slice in prototype



class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.quorum_set = set()
        self.threshold = 2
        self.blocking_set = set()

    def set_quorum_set(self, quorum_set, threshold):
        self.quorum_set = quorum_set
        self.threshold = threshold
        self.update_blocking_set()

    def update_blocking_set(self):
        # Update the blocking set based on quorum set and threshold
        self.blocking_set = {node for node in self.quorum_set if len(self.quorum_set) - len(self.blocking_set) < self.threshold}

# Implement voting logic based on Arkchain
    def vote_ballot(self, ballot_number, value):
        """
        Vote on a ballot based on the node's current state and quorum slices.
        """
        if self.has_voted(ballot_number):
            return

        if self.should_vote_for_ballot(ballot_number, value):
            self.cast_vote(ballot_number, value)
            self.broadcast_vote(ballot_number, value)

    def has_voted(self, ballot_number):
        """
        Check if the node has already voted for the given ballot number.
        """
        return ballot_number in self.voting_history

    def should_vote_for_ballot(self, ballot_number, value):
        """
        Determine if the node should vote for the ballot, based on its quorum slices
        and the state of the network.
        """
        # This is a simplified logic. The actual implementation should consider
        # the node's view of the network state and quorum slice agreements.
        return True

    def cast_vote(self, ballot_number, value):
        """
        Record the node's vote for a particular ballot.
        """
        self.voting_history[ballot_number] = value

    def broadcast_vote(self, ballot_number, value):
        """
        Broadcast the vote to other nodes in the quorum slices.
        """
        for quorum_slice in self.quorum_slices:
            for node_id in quorum_slice:
                # Send the vote to the node. This is a conceptual placeholder.
                # Actual network communication logic is needed here.
                self.send_vote_to_node(node_id, ballot_number, value)

    def receive_vote(self, from_node_id, ballot_number, value):
        """
        Handle an incoming vote from another node.
        """
        if ballot_number not in self.received_votes:
            self.received_votes[ballot_number] = {}
        self.received_votes[ballot_number][from_node_id] = value

        # Process the received vote. This may involve updating the node's state
        # or triggering new actions based on the updated network view.
        self.process_received_vote(ballot_number, value)

    def process_received_vote(self, ballot_number, value):
        """
        Process a received vote for a ballot.
        This method determines if the node should move to the acceptance or confirmation stage.
        """
        # Update the received votes record
        self.update_received_votes(ballot_number, value)

        # Check if the ballot can be accepted
        if self.should_accept_ballot(ballot_number, value):
            self.accept_ballot(ballot_number, value)

        # Check if the ballot can be confirmed
        if self.should_confirm_ballot(ballot_number, value):
            self.confirm_ballot(ballot_number, value)

    def update_received_votes(self, ballot_number, value):
        """
        Update the record of received votes for a ballot.
        """
        if ballot_number not in self.received_votes:
            self.received_votes[ballot_number] = {}

        for quorum_slice in self.quorum_slices:
            for node_id in quorum_slice:
                if node_id in self.received_votes[ballot_number]:
                    self.received_votes[ballot_number][node_id].add(value)
                else:
                    self.received_votes[ballot_number][node_id] = {value}

    def send_vote_to_node(self, node_id, ballot_number, value):
        """
        Send a vote to another node. This is a placeholder for network communication.
        """
        # In a real implementation, this method would handle network communication.
        pass

# Implement acceptance logic based on Arkchain
    def accept_ballot(self, ballot_number, value):
        """
        Accept a ballot based on the received votes and quorum slices.
        """
        if self.has_accepted(ballot_number):
            return  # Avoid re-accepting a ballot

        if self.should_accept_ballot(ballot_number, value):
            self.record_acceptance(ballot_number, value)
            self.broadcast_acceptance(ballot_number, value)

    def has_accepted(self, ballot_number):
        """
        Check if the node has already accepted the given ballot number.
        """
        return ballot_number in self.acceptance_history

    def should_accept_ballot(self, ballot_number, value):
        """
        Determine if the node should accept the ballot, based on its quorum slices
        and the votes received.
        """
        # Check if the quorum slices have enough support for this ballot
        for quorum_slice in self.quorum_slices:
            if self.is_support_from_quorum_slice(quorum_slice, ballot_number, value):
                return True
        return False

    def is_support_from_quorum_slice(self, quorum_slice, ballot_number, value):
        """
        Check if there is enough support for the ballot from a given quorum slice.
        """
        # Count the number of nodes in the quorum slice that have voted for this ballot
        vote_count = sum(1 for node_id in quorum_slice if self.received_votes.get(ballot_number, {}).get(node_id) == value)
        # Check if the vote count meets the threshold for acceptance
        return vote_count >= self.calculate_acceptance_threshold(quorum_slice)

    def calculate_acceptance_threshold(self, quorum_slice):
        """
        Calculate the threshold of votes needed to accept a ballot for a quorum slice.
        """
        # Example: simple majority
        return len(quorum_slice) // 2 + 1

    def record_acceptance(self, ballot_number, value):
        """
        Record the acceptance of a ballot.
        """
        self.acceptance_history[ballot_number] = value

    def broadcast_acceptance(self, ballot_number, value):
        """
        Broadcast the acceptance of a ballot to other nodes.
        """
        for quorum_slice in self.quorum_slices:
            for node_id in quorum_slice:
                self.send_acceptance_to_node(node_id, ballot_number, value)

    def send_acceptance_to_node(self, node_id, ballot_number, value):
        """
        Send an acceptance message to another node. Placeholder for network communication.
        """
        # In a real implementation, this would handle network communication.
        pass

# Implement confirmation logic based on Arkchain

    def confirm_ballot(self, ballot_number, value):
        """
        Confirm a ballot based on the acceptances received from quorum slices.
        """
        if self.has_confirmed(ballot_number):
            return  # Avoid re-confirming a ballot

        if self.should_confirm_ballot(ballot_number, value):
            self.record_confirmation(ballot_number, value)
            self.broadcast_confirmation(ballot_number, value)

    def has_confirmed(self, ballot_number):
        """
        Check if the node has already confirmed the given ballot number.
        """
        return ballot_number in self.confirmation_history

    def should_confirm_ballot(self, ballot_number, value):
        """
        Determine if the node should confirm the ballot, based on its quorum slices
        and the acceptances received.
        """
        # Check if the quorum slices have enough acceptances for this ballot
        for quorum_slice in self.quorum_slices:
            if self.is_acceptance_from_quorum_slice(quorum_slice, ballot_number, value):
                return True
        return False

    def is_acceptance_from_quorum_slice(self, quorum_slice, ballot_number, value):
        """
        Check if there is enough acceptance for the ballot from a given quorum slice.
        """
        # Count the number of nodes in the quorum slice that have accepted this ballot
        acceptance_count = sum(1 for node_id in quorum_slice if self.received_acceptances.get(ballot_number, {}).get(node_id) == value)
        # Check if the acceptance count meets the threshold for confirmation
        return acceptance_count >= self.calculate_confirmation_threshold(quorum_slice)

    def calculate_confirmation_threshold(self, quorum_slice):
        """
        Calculate the threshold of acceptances needed to confirm a ballot for a quorum slice.
        """
        # Example: simple majority
        return len(quorum_slice) // 2 + 1

    def record_confirmation(self, ballot_number, value):
        """
        Record the confirmation of a ballot.
        """
        self.confirmation_history[ballot_number] = value

    def broadcast_confirmation(self, ballot_number, value):
        """
        Broadcast the confirmation of a ballot to other nodes.
        """
        for quorum_slice in self.quorum_slices:
            for node_id in quorum_slice:
                self.send_confirmation_to_node(node_id, ballot_number, value)

    def send_confirmation_to_node(self, node_id, ballot_number, value):
        """
        Send a confirmation message to another node. Placeholder for network communication.
        """
        # In a real implementation, this would handle network communication.
        pass

class Statement:
    def __init__(self, statement_id, content):
        self.statement_id = statement_id
        self.content = content

class ArkchainNetwork:
    def __init__(self):
        self.nodes = {}
        self.statements = {}

    def add_node(self, node_id):
        node = Node(node_id)
        self.nodes[node_id] = node
        return node

    def set_quorum_set_for_node(self, node_id, quorum_set, threshold):
        self.nodes[node_id].set_quorum_set(quorum_set, threshold)

    def add_statement(self, statement_id, content):
        statement = Statement(statement_id, content)
        self.statements[statement_id] = statement

    def federated_voting(self, statement_id):
        statement = self.statements[statement_id]
        for node in self.nodes.values():
            node.vote(statement)
            node.accept(statement)
            node.confirm(statement)

# Example usage
arkchain_network = ArkchainNetwork()
node1 = arkchain_network.add_node("node1")
node2 = arkchain_network.add_node("node2")
node3 = arkchain_network.add_node("node3")

arkchain_network.set_quorum_set_for_node("node1", {"node2", "node3"}, 2)
arkchain_network.set_quorum_set_for_node("node2", {"node1", "node3"}, 2)
arkchain_network.set_quorum_set_for_node("node3", {"node1", "node2"}, 2)

arkchain_network.add_statement("stmt1", "Proposed transaction set for ledger 800")

# Run federated voting
arkchain_network.federated_voting("stmt1")
