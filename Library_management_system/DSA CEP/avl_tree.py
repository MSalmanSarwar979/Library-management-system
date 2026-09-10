
class Book:
    """Book class to store book information"""
    def __init__(self, isbn, title, author, year, category, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.total_copies = total_copies
        self.available_copies = total_copies
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Available: {self.available_copies}/{self.total_copies}"


class AVLNode:
    """Node class for AVL Tree"""
    def __init__(self, isbn, book):
        self.isbn = isbn
        self.book = book
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """AVL Tree implementation for storing books by ISBN"""
    def __init__(self):
        self.root = None
    
    def get_height(self, node):
        """Get height of node"""
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        """Get balance factor of node"""
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        """Update height of node"""
        if not node:
            return
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
    
    def rotate_right(self, y):
        """Right rotation"""
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def rotate_left(self, x):
        """Left rotation"""
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, isbn, book):
        """Insert a book into AVL tree"""
        self.root = self._insert_helper(self.root, isbn, book)
    
    def _insert_helper(self, node, isbn, book):
        """Helper method for insertion"""
        # Standard BST insertion
        if not node:
            return AVLNode(isbn, book)
        
        if isbn < node.isbn:
            node.left = self._insert_helper(node.left, isbn, book)
        elif isbn > node.isbn:
            node.right = self._insert_helper(node.right, isbn, book)
        else:
            # ISBN already exists, update book
            node.book = book
            return node
        
        # Update height
        self.update_height(node)
        
        # Get balance factor
        balance = self.get_balance(node)
        
        # Balance the tree
        # Left Left Case
        if balance > 1 and isbn < node.left.isbn:
            return self.rotate_right(node)
        
        # Right Right Case
        if balance < -1 and isbn > node.right.isbn:
            return self.rotate_left(node)
        
        # Left Right Case
        if balance > 1 and isbn > node.left.isbn:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # Right Left Case
        if balance < -1 and isbn < node.right.isbn:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def search(self, isbn):
        """Search for a book by ISBN"""
        return self._search_helper(self.root, isbn)
    
    def _search_helper(self, node, isbn):
        """Helper method for search"""
        if not node:
            return None
        
        if isbn == node.isbn:
            return node.book
        elif isbn < node.isbn:
            return self._search_helper(node.left, isbn)
        else:
            return self._search_helper(node.right, isbn)
    
    def get_min_value_node(self, node):
        """Get node with minimum value"""
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, isbn):
        """Delete a book from AVL tree"""
        self.root = self._delete_helper(self.root, isbn)
    
    def _delete_helper(self, node, isbn):
        """Helper method for deletion"""
        if not node:
            return node
        
        # Standard BST deletion
        if isbn < node.isbn:
            node.left = self._delete_helper(node.left, isbn)
        elif isbn > node.isbn:
            node.right = self._delete_helper(node.right, isbn)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            temp = self.get_min_value_node(node.right)
            node.isbn = temp.isbn
            node.book = temp.book
            node.right = self._delete_helper(node.right, temp.isbn)
        
        if not node:
            return node
        
        # Update height
        self.update_height(node)
        
        # Get balance factor
        balance = self.get_balance(node)
        
        # Balance the tree
        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def inorder_traversal(self):
        """Return list of books in sorted order by ISBN"""
        result = []
        self._inorder_helper(self.root, result)
        return result
    
    def _inorder_helper(self, node, result):
        """Helper method for inorder traversal"""
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.book)
            self._inorder_helper(node.right, result)