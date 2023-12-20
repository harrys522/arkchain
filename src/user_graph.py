

class UserGraph:
    def __init__(self, users: node):
        self.users = users
        # Connect all users
        for u in self.users:
            for peer in self.users:
                if peer != u:
                    u.peers.append(peer)
    
    def add_new_user(self, new_user: node):
        self.users.append(new_user)
        # Connect with all other users
        for u in self.users:
            if (new_user != u):
                new_user.peers.append(u)
                u.peers.append(new_user)