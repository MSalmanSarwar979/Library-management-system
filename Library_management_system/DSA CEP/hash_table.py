class Node:
    """Node for linked list (used in chaining)"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Hash Table implementation with chaining for collision resolution"""
    def __init__(self, size=100):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        """Hash function to compute index"""
        hash_value = 0
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size
    
    def normalize_key(self, key):
        """Normalize key (lowercase, remove extra spaces)"""
        if isinstance(key, str):
            return ' '.join(key.lower().split())
        return key
    
    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        key = self.normalize_key(key)
        index = self.hash_function(key)
        
        # If bucket is empty, create new node
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Chain: traverse to end or update existing key
            current = self.table[index]
            while True:
                if current.key == key:
                    # Update existing key
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            # Add new node at end of chain
            current.next = Node(key, value)
    
    def search(self, key):
        """Search for value by key"""
        key = self.normalize_key(key)
        index = self.hash_function(key)
        
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def delete(self, key):
        """Delete key-value pair from hash table"""
        key = self.normalize_key(key)
        index = self.hash_function(key)
        
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev is None:
                    # Delete first node in chain
                    self.table[index] = current.next
                else:
                    # Delete middle or last node
                    prev.next = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def get_all_keys(self):
        """Get all keys in hash table"""
        keys = []
        for bucket in self.table:
            current = bucket
            while current:
                keys.append(current.key)
                current = current.next
        return keys


class AuthorHashTable(HashTable):
    """Specialized hash table for author -> list of ISBNs mapping"""
    
    def add_isbn_to_author(self, author, isbn):
        """Add ISBN to author's list of books"""
        author = self.normalize_key(author)
        isbn_list = self.search(author)
        
        if isbn_list is None:
            # Author doesn't exist, create new list
            self.insert(author, [isbn])
        else:
            # Author exists, add ISBN if not already present
            if isbn not in isbn_list:
                isbn_list.append(isbn)
    
    def remove_isbn_from_author(self, author, isbn):
        """Remove ISBN from author's list of books"""
        author = self.normalize_key(author)
        isbn_list = self.search(author)
        
        if isbn_list and isbn in isbn_list:
            isbn_list.remove(isbn)
            # If list is empty, remove author entry
            if not isbn_list:
                self.delete(author)
            return True
        return False