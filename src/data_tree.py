import threading

class DataNode:
    def __init__(self, key, value):
        """
        All data will be stored in an AVL tree. The key will be the timestamp,
        and the value will be the ArkBlock. 
        """
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class DataTree:
    def __init__(self):
        self.root = None
        self.lock = threading.Lock()

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key, value):
        if not root:
            return DataNode(key, value)

        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            # Duplicate keys are not allowed in AVL tree
            return root

        self.update_height(root)

        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_thread_safe(self, key, value):
        with self.lock:
            self.root = self.insert(self.root, key, value)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self.inorder_traversal(node.right, result)

    def get_sorted_elements(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result

# Example usage:
data_tree = DataTree()

# Insert elements in a thread-safe manner
data_tree.insert_thread_safe(3, 'Three')
data_tree.insert_thread_safe(1, 'One')
data_tree.insert_thread_safe(2, 'Two')
data_tree.insert_thread_safe(4, 'Four')

# Retrieve sorted elements
sorted_elements = data_tree.get_sorted_elements()
#print(sorted_elements)
