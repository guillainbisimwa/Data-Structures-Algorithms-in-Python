class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.inserting_value(tree.root, new_val)        
    
    def inserting_value(self, start, new_val):

        if start:
            if start.value < new_val:
                if start.left != None:
                    self.inserting_value(start.left, new_val)
                else:
                    start.left = Node(new_val)
            else:
                if start.right != None:
                    self.inserting_value(start.right, new_val)
                else:
                    start.right = Node(new_val)
                    
    def search(self, find_val):
        return self.recursive_search(tree.root, find_val)
    
    def recursive_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.recursive_search(start.left, find_val) or self.recursive_search(start.right, find_val)
        else:
            return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)