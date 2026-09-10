from avl_tree import AVLTree, Book
from hash_table import HashTable, AuthorHashTable


class Member:
    """Member class to store member information"""
    def __init__(self, member_id, name, member_type="student"):
        self.member_id = member_id
        self.name = name
        self.member_type = member_type
        self.borrowed_books = []  # List of ISBNs
    
    def __str__(self):
        return f"{self.name} ({self.member_id}) - Type: {self.member_type}, Borrowed: {len(self.borrowed_books)} books"


class LibraryManagementSystem:
    """Main Library Management System"""
    def __init__(self):
        self.book_catalog = AVLTree()  #root none
        self.title_index = HashTable()  #100 none bucket
        self.author_index = AuthorHashTable()   
        self.member_database = HashTable()  #100 none bucket
        self.max_books_per_member = 5
     
    def add_book(self, isbn, title, author, year, category, total_copies):
        """Add a book to the library system"""
        # Create book object
        book = Book(isbn, title, author, year, category, total_copies)
        
        # Insert into AVL tree
        self.book_catalog.insert(isbn, book)
        
        # Insert into title index
        self.title_index.insert(title, isbn)
        
        # Insert into author index
        self.author_index.add_isbn_to_author(author, isbn)
        
        print(f"✓ Book added: {title}")
        return True
    
    def delete_book(self, isbn):
        """Delete a book from the library system"""
        # Search for book first
        book = self.book_catalog.search(isbn)
        if not book:
            print(f"✗ Book with ISBN {isbn} not found")
            return False
        
        # Remove from all indices
        self.title_index.delete(book.title)
        self.author_index.remove_isbn_from_author(book.author, isbn)
        self.book_catalog.delete(isbn)
        
        print(f"✓ Book deleted: {book.title}")
        return True
    
    def search_by_isbn(self, isbn):
        """Search for a book by ISBN"""
        book = self.book_catalog.search(isbn)
        if book:
            print(f"\n📖 Found: {book}")
            return book
        else:
            print(f"\n✗ No book found with ISBN: {isbn}")
            return None
    
    def search_by_title(self, title):
        """Search for a book by title"""
        # Step 1: Look up ISBN in title hash table (O(1))
        isbn = self.title_index.search(title)
        
        if not isbn:
            print(f"\n✗ No book found with title: {title}")
            return None
        
        # Step 2: Look up full book details in AVL tree (O(log n))
        book = self.book_catalog.search(isbn)
        if book:
            print(f"\n📖 Found: {book}")
            return book
        return None
    
    def search_by_author(self, author):
        """Search for all books by an author"""
        # Look up list of ISBNs for this author
        isbn_list = self.author_index.search(author)
        
        if not isbn_list:
            print(f"\n✗ No books found by author: {author}")
            return []
        
        # Get full book details for each ISBN
        books = []
        print(f"\n📚 Books by {author}:")
        for isbn in isbn_list:
            book = self.book_catalog.search(isbn)
            if book:
                books.append(book)
                print(f"  • {book}")
        
        return books
    
    def add_member(self, member_id, name, member_type="student"):
        """Add a member to the library system"""
        member = Member(member_id, name, member_type)
        self.member_database.insert(member_id, member)
        print(f"✓ Member added: {name} ({member_id})")
        return True
    
    def borrow_book(self, member_id, isbn):
        """Process book borrowing"""
        # Check if member exists
        member = self.member_database.search(member_id)
        if not member:
            print(f"✗ Member {member_id} not found")
            return False
        
        # Check member's borrowing limit
        if len(member.borrowed_books) >= self.max_books_per_member:
            print(f"✗ {member.name} has reached the borrowing limit ({self.max_books_per_member} books)")
            return False
        
        # Check if book exists
        book = self.book_catalog.search(isbn)
        if not book:
            print(f"✗ Book with ISBN {isbn} not found")
            return False
        
        # Check if book is already borrowed by this member
        if isbn in member.borrowed_books:
            print(f"✗ {member.name} has already borrowed this book")
            return False
        
        # Check book availability
        if book.available_copies <= 0:
            print(f"✗ No copies of '{book.title}' are currently available")
            return False
        
        # Process borrowing
        book.available_copies -= 1
        member.borrowed_books.append(isbn)
        
        print(f"✓ {member.name} borrowed '{book.title}'")
        print(f"  Remaining copies: {book.available_copies}/{book.total_copies}")
        return True
    
    def return_book(self, member_id, isbn):
        """Process book return"""
        # Check if member exists
        member = self.member_database.search(member_id)
        if not member:
            print(f"✗ Member {member_id} not found")
            return False
        
        # Check if member has borrowed this book
        if isbn not in member.borrowed_books:
            print(f"✗ {member.name} has not borrowed this book")
            return False
        
        # Check if book exists
        book = self.book_catalog.search(isbn)
        if not book:
            print(f"✗ Book with ISBN {isbn} not found")
            return False
        
        # Process return
        member.borrowed_books.remove(isbn)
        book.available_copies += 1
        
        print(f"✓ {member.name} returned '{book.title}'")
        print(f"  Available copies: {book.available_copies}/{book.total_copies}")
        return True
    
    def list_member_books(self, member_id):
        """List all books borrowed by a member"""
        member = self.member_database.search(member_id)
        if not member:
            print(f"✗ Member {member_id} not found")
            return []
        
        if not member.borrowed_books:
            print(f"\n{member.name} has no borrowed books")
            return []
        
        print(f"\n📚 Books borrowed by {member.name}:")
        books = []
        for isbn in member.borrowed_books:
            book = self.book_catalog.search(isbn)
            if book:
                books.append(book)
                print(f"  • {book}")
        
        return books
    
    def list_available_books(self):
        """List all books with available copies"""
        all_books = self.book_catalog.inorder_traversal()
        available = []  
        for book in all_books:  
            if book.available_copies > 0: 
                available.append(book)
        
        print(f"\n📚 Available Books ({len(available)}):")
        for book in available:
            print(f"  • {book}")
        
        return available
    
    def list_all_books_sorted(self):
        """List all books sorted by ISBN"""
        all_books = self.book_catalog.inorder_traversal()
        
        print(f"\n📚 All Books (sorted by ISBN) - Total: {len(all_books)}:")
        for book in all_books:
            print(f"  • {book}")
        
        return all_books
    
    def get_member_info(self, member_id):
        """Get member information"""
        member = self.member_database.search(member_id)
        if member:
            print(f"\n👤 {member}")
            return member
        else:
            print(f"\n✗ Member {member_id} not found")
            return None
        
        
def test_library_system():
    """Comprehensive test suite for the library management system"""
    
    print("="*80)
    print("LIBRARY MANAGEMENT SYSTEM - TEST SUITE")
    print("="*80)
    
    # Initialize system
    library = LibraryManagementSystem()
    
    # Test 1: Add Books
    print("\n" + "="*80)
    print("TEST 1: ADDING BOOKS")
    print("="*80)
    
    books_data = [
        ("9780134685991", "Effective Python", "Brett Slatkin", 2019, "Programming", 3),
        ("9780132350884", "Clean Code", "Robert Martin", 2008, "Programming", 5),
        ("9780135957059", "The Pragmatic Programmer", "David Thomas", 2019, "Programming", 4),
        ("9780201633610", "Design Patterns", "Gang of Four", 1994, "Software Engineering", 2),
        ("9780596517748", "JavaScript: The Good Parts", "Douglas Crockford", 2008, "Web Development", 3),
        ("9781491950296", "Learning Python", "Mark Lutz", 2013, "Programming", 6),
        ("9780134494166", "Clean Architecture", "Robert Martin", 2017, "Software Engineering", 4),
        ("9781449355739", "Head First Design Patterns", "Eric Freeman", 2004, "Software Engineering", 3),
        ("9780321125215", "Domain-Driven Design", "Eric Evans", 2003, "Software Engineering", 2),
        ("9780596009205", "Head First Java", "Kathy Sierra", 2005, "Programming", 5),
        ("9781617294945", "Grokking Algorithms", "Aditya Bhargava", 2016, "Algorithms", 4),
        ("9780262033848", "Introduction to Algorithms", "Cormen", 2009, "Algorithms", 3),
        ("9780735619678", "Code Complete", "Steve McConnell", 2004, "Programming", 4),
        ("9780596007126", "The Art of Unix Programming", "Eric Raymond", 2003, "Unix", 2),
        ("9781449373320", "Designing Data-Intensive Applications", "Martin Kleppmann", 2017, "Databases", 3),
        ("9780321573513", "Algorithms", "Robert Sedgewick", 2011, "Algorithms", 3),
        ("9781491904244", "Python for Data Analysis", "Wes McKinney", 2017, "Data Science", 4),
        ("9780134757599", "Refactoring", "Martin Fowler", 2018, "Programming", 3),
        ("9780136291558", "Object-Oriented Analysis", "Peter Coad", 1990, "Software Engineering", 2),
        ("9781593279509", "Eloquent JavaScript", "Marijn Haverbeke", 2018, "Web Development", 5),
        ("9780321349606", "Java Concurrency in Practice", "Brian Goetz", 2006, "Programming", 2),
        ("9781449355692", "Learning React", "Alex Banks", 2017, "Web Development", 4),
        ("9780134494272", "Effective Java", "Joshua Bloch", 2018, "Programming", 3),
        ("9780596802189", "Beautiful Code", "Andy Oram", 2007, "Programming", 2),
        ("9781449337711", "Designing Web APIs", "Brenda Jin", 2018, "Web Development", 3),
        ("9780321721334", "Test Driven Development", "Kent Beck", 2002, "Testing", 2),
        ("9781118531648", "Java: The Complete Reference", "Herbert Schildt", 2014, "Programming", 5),
        ("9781492052593", "Building Microservices", "Sam Newman", 2021, "Architecture", 3),
        ("9780134757681", "C Programming Language", "Brian Kernighan", 1988, "Programming", 4),
        ("9781449369415", "RESTful Web APIs", "Leonard Richardson", 2013, "Web Development", 2),
        ("9780201835953", "The Mythical Man-Month", "Frederick Brooks", 1995, "Project Management", 3),
        ("9780135974445", "Agile Software Development", "Robert Martin", 2002, "Agile", 2),
        ("9780596009793", "JavaScript Patterns", "Stoyan Stefanov", 2010, "Web Development", 3),
        ("9781449340377", "High Performance Python", "Micha Gorelick", 2014, "Programming", 2),
        ("9780596516178", "Programming Collective Intelligence", "Toby Segaran", 2007, "AI", 2),
        ("9781617295287", "Deep Learning with Python", "Francois Chollet", 2017, "AI", 4),
        ("9780132778046", "Database Management Systems", "Raghu Ramakrishnan", 2002, "Databases", 3),
        ("9780134494289", "Kotlin in Action", "Dmitry Jemerov", 2017, "Programming", 3),
        ("9781617294945", "Spring in Action", "Craig Walls", 2018, "Frameworks", 2),
        ("9780321573513", "Computer Networks", "Andrew Tanenbaum", 2010, "Networks", 4),
        ("9781449369088", "Learning SQL", "Alan Beaulieu", 2009, "Databases", 3),
        ("9780596527341", "Regular Expressions Cookbook", "Jan Goyvaerts", 2012, "Programming", 2),
        ("9781491946008", "Fluent Python", "Luciano Ramalho", 2015, "Programming", 4),
        ("9780134685991", "Site Reliability Engineering", "Google", 2016, "DevOps", 3),
        ("9781617294136", "Docker in Action", "Jeff Nickoloff", 2016, "DevOps", 2),
        ("9780134494197", "Kubernetes in Action", "Marko Luksa", 2017, "DevOps", 3),
        ("9780135957059", "The DevOps Handbook", "Gene Kim", 2016, "DevOps", 2),
        ("9781449373320", "Continuous Delivery", "Jez Humble", 2010, "DevOps", 3),
        ("9780596517748", "Programming Rust", "Jim Blandy", 2017, "Programming", 2),
        ("9781491950296", "Go in Action", "William Kennedy", 2015, "Programming", 3),
    ]
    
    for isbn, title, author, year, category, copies in books_data[:50]:
        library.add_book(isbn, title, author, year, category, copies)
    
    # Test 2: Add Members
    print("\n" + "="*80)
    print("TEST 2: ADDING MEMBERS")
    print("="*80)
    
    members_data = [
        ("2024-EE-001", "Ali Ahmed", "student"),
        ("2024-EE-002", "Sara Khan", "student"),
        ("2024-CS-015", "Hassan Raza", "student"),
        ("2024-ME-032", "Fatima Malik", "student"),
        ("2024-EE-045", "Usman Ali", "student"),
        ("2024-CS-028", "Ayesha Saeed", "student"),
        ("2024-EE-019", "Ahmed Hassan", "student"),
        ("2024-ME-007", "Zainab Tariq", "student"),
        ("2024-CS-041", "Bilal Aslam", "student"),
        ("2024-EE-033", "Maryam Noor", "student"),
        ("PROF-001", "Dr. Muhammad Saleem", "faculty"),
        ("PROF-002", "Dr. Ayesha Farooq", "faculty"),
        ("2024-EE-067", "Hamza Butt", "student"),
        ("2024-CS-053", "Sana Iqbal", "student"),
        ("2024-ME-021", "Fahad Mahmood", "student"),
        ("2024-EE-012", "Hira Shahid", "student"),
        ("2024-CS-039", "Imran Qureshi", "student"),
        ("2024-EE-055", "Nida Zafar", "student"),
        ("2024-ME-044", "Kamran Siddiqui", "student"),
        ("2024-CS-062", "Rabia Mushtaq", "student"),
    ]
    
    for member_id, name, member_type in members_data:
        library.add_member(member_id, name, member_type)
    
    # Test 3: Search Operations
    print("\n" + "="*80)
    print("TEST 3: SEARCH OPERATIONS")
    print("="*80)
    
    print("\n--- Search by ISBN ---")
    library.search_by_isbn("9780134685991")
    
    print("\n--- Search by Title ---")
    library.search_by_title("Clean Code")
    
    print("\n--- Search by Author ---")
    library.search_by_author("Robert Martin")
    
    # Test 4: Borrowing Books
    print("\n" + "="*80)
    print("TEST 4: BORROWING BOOKS")
    print("="*80)
    
    library.borrow_book("2024-EE-001", "9780134685991")
    library.borrow_book("2024-EE-001", "9780132350884")
    library.borrow_book("2024-EE-002", "9780135957059")
    library.borrow_book("2024-CS-015", "9780134685991")
    
    # Test edge case: Borrowing unavailable book
    print("\n--- Test: Borrowing when no copies available ---")
    library.borrow_book("2024-EE-001", "9780201633610")
    library.borrow_book("2024-EE-002", "9780201633610")
    library.borrow_book("2024-CS-015", "9780201633610")  # Should fail
    
    # Test edge case: Borrowing limit
    print("\n--- Test: Member borrowing limit (max 5 books) ---")
    library.borrow_book("2024-EE-001", "9780596517748")
    library.borrow_book("2024-EE-001", "9781491950296")
    library.borrow_book("2024-EE-001", "9780134494166")  # 5th book
    library.borrow_book("2024-EE-001", "9781449355739")  # Should fail (limit reached)
    
    # Test 5: Return Books
    print("\n" + "="*80)
    print("TEST 5: RETURNING BOOKS")
    print("="*80)
    
    library.return_book("2024-EE-001", "9780134685991")
    library.return_book("2024-EE-002", "9780201633610")
    
    # Test edge case: Returning book not borrowed
    print("\n--- Test: Returning book not borrowed ---")
    library.return_book("2024-EE-001", "9781449355739")  # Should fail
    
    # Test 6: Reporting Functions
    print("\n" + "="*80)
    print("TEST 6: REPORTING FUNCTIONS")
    print("="*80)
    
    print("\n--- Member's Borrowed Books ---")
    library.list_member_books("2024-EE-001")
    
    print("\n--- Available Books ---")
    library.list_available_books()
    
    print("\n--- All Books (Sorted by ISBN) ---")
    library.list_all_books_sorted()
    
    # Test 7: Member Information
    print("\n" + "="*80)
    print("TEST 7: MEMBER INFORMATION")
    print("="*80)
    
    library.get_member_info("2024-EE-001")
    library.get_member_info("PROF-001")
    
    # Test 8: Edge Cases
    print("\n" + "="*80)
    print("TEST 8: EDGE CASES")
    print("="*80)
    
    print("\n--- Search for non-existent book ---")
    library.search_by_isbn("9999999999999")
    
    print("\n--- Search for non-existent author ---")
    library.search_by_author("Unknown Author")
    
    print("\n--- Borrow with invalid member ---")
    library.borrow_book("INVALID-ID", "9780134685991")
    
    print("\n" + "="*80)
    print("ALL TESTS COMPLETED!")
    print("="*80)


if __name__ == "__main__":
    from main import LibraryApp

    app = LibraryApp()
    app.mainloop()