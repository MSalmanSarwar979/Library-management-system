import customtkinter as ctk
from tkinter import messagebox

from library_system import LibraryManagementSystem


# -----------------------------
# App Configuration
# -----------------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LibraryApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Library Management System")
        self.geometry("1200x700")
        self.minsize(1000, 600)

        # Create backend
        self.library = LibraryManagementSystem()

        # Load books and members
        self.load_sample_data()

        # Create GUI
        self.create_layout()
        self.show_dashboard()

    def load_sample_data(self):

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

        for book in books_data:
            self.library.add_book(*book)

        # -----------------------------
        # Sample Members
        # -----------------------------
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

        for member in members_data:
            self.library.add_member(*member)

    # -----------------------------
    # Main Layout
    # -----------------------------
    def create_layout(self):

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self,
            width=220,
            corner_radius=0
        )
        self.sidebar.pack(
            side="left",
            fill="y"
        )
        self.sidebar.pack_propagate(False)

        # Logo / Title
        title = ctk.CTkLabel(
            self.sidebar,
            text="📚 Library\nManagement",
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )
        title.pack(
            pady=(35, 30)
        )

        # Navigation buttons
        self.create_nav_button(
            "🏠  Dashboard",
            self.show_dashboard
        )

        self.create_nav_button(
            "📚  Books",
            self.show_books
        )

        self.create_nav_button(
            "👤  Members",
            self.show_members
        )

        self.create_nav_button(
            "🔄  Transactions",
            self.show_transactions
        )

        self.create_nav_button(
            "📊  Reports",
            self.show_reports
        )

        # Exit button
        exit_button = ctk.CTkButton(
            self.sidebar,
            text="❌  Exit",
            command=self.destroy,
            fg_color="transparent",
            border_width=1
        )

        exit_button.pack(
            side="bottom",
            padx=20,
            pady=25,
            fill="x"
        )

        # Main content area
        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )
        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

    def create_nav_button(self, text, command):

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            command=command,
            height=45,
            anchor="w",
            fg_color="transparent"
        )

        button.pack(
            padx=15,
            pady=5,
            fill="x"
        )

    # -----------------------------
    # Utility Functions
    # -----------------------------
    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    def create_page_title(self, title, subtitle=""):

        title_label = ctk.CTkLabel(
            self.content,
            text=title,
            font=ctk.CTkFont(
                size=30,
                weight="bold"
            )
        )

        title_label.pack(
            anchor="w",
            padx=30,
            pady=(25, 5)
        )

        if subtitle:

            subtitle_label = ctk.CTkLabel(
                self.content,
                text=subtitle,
                font=ctk.CTkFont(size=14)
            )

            subtitle_label.pack(
                anchor="w",
                padx=30,
                pady=(0, 20)
            )

    # -----------------------------
    # Dashboard
    # -----------------------------
    def show_dashboard(self):

        self.clear_content()

        self.create_page_title(
            "Dashboard",
            "Library Management System"
        )

        books = self.library.book_catalog.inorder_traversal()

        total_books = len(books)

        available_books = sum(
            1 for book in books
            if book.available_copies > 0
        )

        total_copies = sum(
            book.total_copies
            for book in books
        )

        borrowed_copies = total_copies - sum(
            book.available_copies
            for book in books
        )

        # Cards
        cards_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        cards_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        cards_frame.grid_columnconfigure(
            (0, 1, 2, 3),
            weight=1
        )

        self.create_card(
            cards_frame,
            "📚",
            "Books",
            str(total_books),
            0
        )

        self.create_card(
            cards_frame,
            "📖",
            "Available",
            str(available_books),
            1
        )

        self.create_card(
            cards_frame,
            "📦",
            "Borrowed",
            str(borrowed_copies),
            2
        )

        # Member count
        member_count = len(
            self.library.member_database.get_all_keys()
        )

        self.create_card(
            cards_frame,
            "👤",
            "Members",
            str(member_count),
            3
        )

        # Welcome section
        welcome = ctk.CTkFrame(
            self.content
        )

        welcome.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        ctk.CTkLabel(
            welcome,
            text="Welcome to the Library Management System",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        ).pack(pady=(40, 15))

        ctk.CTkLabel(
            welcome,
            text=(
                "Use the navigation menu to manage books, members,\n"
                "borrowing, returns and library reports."
            ),
            font=ctk.CTkFont(size=15),
            justify="center"
        ).pack()

    def create_card(
        self,
        parent,
        icon,
        title,
        value,
        column
    ):

        card = ctk.CTkFrame(
            parent,
            height=130
        )

        card.grid(
            row=0,
            column=column,
            padx=7,
            sticky="nsew"
        )

        ctk.CTkLabel(
            card,
            text=icon,
            font=ctk.CTkFont(size=30)
        ).pack(pady=(15, 2))

        ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(
                size=25,
                weight="bold"
            )
        ).pack()

        ctk.CTkLabel(
            card,
            text=title
        ).pack()

    # -----------------------------
    # Books Page
    # -----------------------------
    def show_books(self):

        self.clear_content()

        self.create_page_title(
            "Books",
            "Manage books in the library"
        )

        button_frame = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        button_frame.pack(
            fill="x",
            padx=30
        )

        ctk.CTkButton(
            button_frame,
            text="➕ Add Book",
            command=self.add_book_window
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="🔍 Search",
            command=self.search_book_window
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            button_frame,
            text="📋 View All Books",
            command=self.view_all_books
        ).pack(
            side="left",
            padx=5
        )

        self.book_display = ctk.CTkTextbox(
            self.content,
            font=ctk.CTkFont(size=14)
        )

        self.book_display.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

    # -----------------------------
    # Add Book
    # -----------------------------
    def add_book_window(self):

        window = ctk.CTkToplevel(self)

        window.title("Add Book")
        window.geometry("500x600")

        window.grab_set()

        fields = [
            ("ISBN", "isbn"),
            ("Title", "title"),
            ("Author", "author"),
            ("Year", "year"),
            ("Category", "category"),
            ("Total Copies", "copies")
        ]

        entries = {}

        for label, key in fields:

            ctk.CTkLabel(
                window,
                text=label
            ).pack(
                anchor="w",
                padx=30,
                pady=(12, 2)
            )

            entry = ctk.CTkEntry(
                window,
                width=400
            )

            entry.pack(
                padx=30
            )

            entries[key] = entry

        def add():

            try:

                isbn = entries["isbn"].get().strip()
                title = entries["title"].get().strip()
                author = entries["author"].get().strip()
                year = int(entries["year"].get())
                category = entries["category"].get().strip()
                copies = int(entries["copies"].get())

                if not all([
                    isbn,
                    title,
                    author,
                    category
                ]):
                    messagebox.showerror(
                        "Error",
                        "Please fill all fields."
                    )
                    return

                if copies <= 0:
                    messagebox.showerror(
                        "Error",
                        "Copies must be greater than 0."
                    )
                    return

                self.library.add_book(
                    isbn,
                    title,
                    author,
                    year,
                    category,
                    copies
                )

                messagebox.showinfo(
                    "Success",
                    f"Book '{title}' added successfully."
                )

                window.destroy()
                self.show_books()

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Year and copies must be numbers."
                )

        ctk.CTkButton(
            window,
            text="Add Book",
            command=add,
            height=40
        ).pack(
            pady=30
        )

    # -----------------------------
    # Search Book
    # -----------------------------
    def search_book_window(self):

        window = ctk.CTkToplevel(self)

        window.title("Search Book")
        window.geometry("500x400")

        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Search Book",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            )
        ).pack(pady=20)

        search_type = ctk.StringVar(
            value="ISBN"
        )

        option = ctk.CTkOptionMenu(
            window,
            values=[
                "ISBN",
                "Title",
                "Author"
            ],
            variable=search_type
        )

        option.pack(pady=10)

        entry = ctk.CTkEntry(
            window,
            width=350,
            placeholder_text="Enter search value"
        )

        entry.pack(pady=10)

        result = ctk.CTkTextbox(
            window,
            width=420,
            height=150
        )

        result.pack(pady=15)

        def search():

            result.delete(
                "1.0",
                "end"
            )

            value = entry.get().strip()

            if not value:
                return

            if search_type.get() == "ISBN":

                book = self.library.search_by_isbn(
                    value
                )

                if book:
                    result.insert(
                        "end",
                        str(book)
                    )
                else:
                    result.insert(
                        "end",
                        "Book not found."
                    )

            elif search_type.get() == "Title":

                book = self.library.search_by_title(
                    value
                )

                if book:
                    result.insert(
                        "end",
                        str(book)
                    )
                else:
                    result.insert(
                        "end",
                        "Book not found."
                    )

            else:

                books = self.library.search_by_author(
                    value
                )

                if books:

                    for book in books:
                        result.insert(
                            "end",
                            str(book) + "\n\n"
                        )
                else:
                    result.insert(
                        "end",
                        "No books found."
                    )

        ctk.CTkButton(
            window,
            text="Search",
            command=search
        ).pack(pady=5)

    # -----------------------------
    # View All Books
    # -----------------------------
    def view_all_books(self):

        books = self.library.list_all_books_sorted()

        self.book_display.delete(
            "1.0",
            "end"
        )

        if not books:

            self.book_display.insert(
                "end",
                "No books in library."
            )

            return

        for i, book in enumerate(books, 1):

            self.book_display.insert(
                "end",
                f"{i}. {book}\n\n"
            )

    # -----------------------------
    # Members
    # -----------------------------
    def show_members(self):

        self.clear_content()

        self.create_page_title(
            "Members",
            "Manage library members"
        )

        ctk.CTkButton(
            self.content,
            text="➕ Add Member",
            command=self.add_member_window
        ).pack(
            anchor="w",
            padx=30
        )

        self.member_display = ctk.CTkTextbox(
            self.content,
            font=ctk.CTkFont(size=14)
        )

        self.member_display.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

        self.show_all_members()

    def show_all_members(self):

        self.member_display.delete(
            "1.0",
            "end"
        )

        member_ids = (
            self.library.member_database
            .get_all_keys()
        )

        if not member_ids:

            self.member_display.insert(
                "end",
                "No members registered."
            )

            return

        for member_id in member_ids:

            member = (
                self.library.member_database
                .search(member_id)
            )

            self.member_display.insert(
                "end",
                str(member) + "\n\n"
            )

    # -----------------------------
    # Add Member
    # -----------------------------
    def add_member_window(self):

        window = ctk.CTkToplevel(self)

        window.title("Add Member")
        window.geometry("450x400")

        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Member ID"
        ).pack(pady=(30, 5))

        member_id = ctk.CTkEntry(
            window,
            width=350
        )

        member_id.pack()

        ctk.CTkLabel(
            window,
            text="Name"
        ).pack(pady=(20, 5))

        name = ctk.CTkEntry(
            window,
            width=350
        )

        name.pack()

        ctk.CTkLabel(
            window,
            text="Member Type"
        ).pack(pady=(20, 5))

        member_type = ctk.CTkOptionMenu(
            window,
            values=[
                "student",
                "faculty"
            ]
        )

        member_type.pack()

        def add():

            mid = member_id.get().strip()
            mname = name.get().strip()
            mtype = member_type.get()

            if not mid or not mname:

                messagebox.showerror(
                    "Error",
                    "Please fill all fields."
                )

                return

            self.library.add_member(
                mid,
                mname,
                mtype
            )

            messagebox.showinfo(
                "Success",
                f"Member '{mname}' added."
            )

            window.destroy()
            self.show_members()

        ctk.CTkButton(
            window,
            text="Add Member",
            command=add
        ).pack(pady=30)

    # -----------------------------
    # Transactions
    # -----------------------------
    def show_transactions(self):

        self.clear_content()

        self.create_page_title(
            "Transactions",
            "Borrow and return books"
        )

        buttons = ctk.CTkFrame(
            self.content,
            fg_color="transparent"
        )

        buttons.pack(
            padx=30,
            pady=20
        )

        ctk.CTkButton(
            buttons,
            text="📖 Borrow Book",
            command=self.borrow_window,
            width=200,
            height=50
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        ctk.CTkButton(
            buttons,
            text="↩ Return Book",
            command=self.return_window,
            width=200,
            height=50
        ).grid(
            row=0,
            column=1,
            padx=10
        )

    # -----------------------------
    # Borrow
    # -----------------------------
    def borrow_window(self):

        window = ctk.CTkToplevel(self)

        window.title("Borrow Book")
        window.geometry("450x350")

        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Member ID"
        ).pack(pady=(30, 5))

        member_id = ctk.CTkEntry(
            window,
            width=350
        )

        member_id.pack()

        ctk.CTkLabel(
            window,
            text="Book ISBN"
        ).pack(pady=(20, 5))

        isbn = ctk.CTkEntry(
            window,
            width=350
        )

        isbn.pack()

        def borrow():

            success = self.library.borrow_book(
                member_id.get().strip(),
                isbn.get().strip()
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Book borrowed successfully."
                )

                window.destroy()

            else:

                messagebox.showerror(
                    "Failed",
                    "Book could not be borrowed.\n"
                    "Check member, ISBN, availability or limit."
                )

        ctk.CTkButton(
            window,
            text="Borrow Book",
            command=borrow
        ).pack(pady=30)

    # -----------------------------
    # Return
    # -----------------------------
    def return_window(self):

        window = ctk.CTkToplevel(self)

        window.title("Return Book")
        window.geometry("450x350")

        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Member ID"
        ).pack(pady=(30, 5))

        member_id = ctk.CTkEntry(
            window,
            width=350
        )

        member_id.pack()

        ctk.CTkLabel(
            window,
            text="Book ISBN"
        ).pack(pady=(20, 5))

        isbn = ctk.CTkEntry(
            window,
            width=350
        )

        isbn.pack()

        def return_book():

            success = self.library.return_book(
                member_id.get().strip(),
                isbn.get().strip()
            )

            if success:

                messagebox.showinfo(
                    "Success",
                    "Book returned successfully."
                )

                window.destroy()

            else:

                messagebox.showerror(
                    "Failed",
                    "Book could not be returned."
                )

        ctk.CTkButton(
            window,
            text="Return Book",
            command=return_book
        ).pack(pady=30)

    # -----------------------------
    # Reports
    # -----------------------------
    def show_reports(self):

        self.clear_content()

        self.create_page_title(
            "Reports",
            "Library information and reports"
        )

        ctk.CTkButton(
            self.content,
            text="📚 Available Books",
            command=self.available_report
        ).pack(
            anchor="w",
            padx=30,
            pady=5
        )

        ctk.CTkButton(
            self.content,
            text="📋 All Books Sorted by ISBN",
            command=self.all_books_report
        ).pack(
            anchor="w",
            padx=30,
            pady=5
        )

        ctk.CTkButton(
            self.content,
            text="👤 Member Information",
            command=self.member_info_window
        ).pack(
            anchor="w",
            padx=30,
            pady=5
        )

        self.report_display = ctk.CTkTextbox(
            self.content,
            font=ctk.CTkFont(size=14)
        )

        self.report_display.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=20
        )

    def available_report(self):

        books = self.library.list_available_books()

        self.report_display.delete(
            "1.0",
            "end"
        )

        for book in books:

            self.report_display.insert(
                "end",
                str(book) + "\n\n"
            )

    def all_books_report(self):

        books = self.library.list_all_books_sorted()

        self.report_display.delete(
            "1.0",
            "end"
        )

        for book in books:

            self.report_display.insert(
                "end",
                str(book) + "\n\n"
            )

    # -----------------------------
    # Member Information
    # -----------------------------
    def member_info_window(self):

        window = ctk.CTkToplevel(self)

        window.title("Member Information")
        window.geometry("500x400")

        window.grab_set()

        ctk.CTkLabel(
            window,
            text="Member ID"
        ).pack(pady=(30, 5))

        entry = ctk.CTkEntry(
            window,
            width=350
        )

        entry.pack()

        result = ctk.CTkTextbox(
            window,
            width=420,
            height=180
        )

        result.pack(pady=20)

        def search():

            result.delete(
                "1.0",
                "end"
            )

            member = self.library.get_member_info(
                entry.get().strip()
            )

            if member:

                result.insert(
                    "end",
                    str(member)
                )

                books = self.library.list_member_books(
                    entry.get().strip()
                )

                if books:

                    result.insert(
                        "end",
                        "\n\nBorrowed Books:\n\n"
                    )

                    for book in books:

                        result.insert(
                            "end",
                            str(book) + "\n\n"
                        )

            else:

                result.insert(
                    "end",
                    "Member not found."
                )

        ctk.CTkButton(
            window,
            text="Search Member",
            command=search
        ).pack()


# -----------------------------
# Run Application
# -----------------------------
if __name__ == "__main__":

    app = LibraryApp()
    app.mainloop()