import sqlite3
from models.BookTemplate import BookTemplate
from models.Merchant import Merchant
from models.Person import Person
from models.Book import Book

class Database(object):
    """
    Database Class used to Access Database and get Object Models
    Ensure that this only exists once!
    """
    def __init__(self):
        """
        Constructor, initialize the database connection to a local database
        """
        self.connection = sqlite3.connect("eduBib.sqlite")
        self.checkTables()

    def checkTables(self):
        """
        Check all tables. Create them of they dont exist.
        """
        cursor = self.connection.cursor()
        ### Check book_template table
        try:
            print "Checking book_template table..."
            cursor.execute("SELECT 1 FROM book_template LIMIT 1");
            print "found."
        except:
            print "book_template does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE book_template (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, isbn STRING, name STRING, author STRING, publisher STRING)")
            self.connection.commit()

        ### Check books table
        try:
            print "Checking books table..."
            cursor.execute("SELECT 1 FROM books LIMIT 1");
            print "found."
        except:
            print "books does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, template_id INTEGER, borrowed_by INTEGER)")
            self.connection.commit()

        ### Check merchants table
        try:
            print "Checking merchants table..."
            cursor.execute("SELECT 1 FROM merchants LIMIT 1")
            print "found."
        except:
            print "merchants does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE merchants (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name STRING, address STRING)")
            self.connection.commit();

        ### Check persons table
        try:
            print "Checking persons table..."
            cursor.execute("SELECT 1 FROM persons LIMIT 1")
            print "found."
        except:
            print "persons does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE persons (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name STRING, class STRING)")
            self.connection.commit()
        # TODO: Do the other tables

    def getBookTemplate(self, id):
        """
        Returns a book template from the database.
        :param id:  int - the book template id
        :return: if found: book template with the specified id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, isbn, name, author, publisher FROM book_template WHERE id = '?';", id)
        length = len(cursor)
        if length == 0:
            return None

        data = cursor.fetchone()

        bookTemplate = BookTemplate(data[0], data[1], data[2], data[3], data[5])
        cursor.close()
        return bookTemplate

    def getMerchant(self, id):
        """
        Returns a merchant with given id
        :param id: int - the id to search for
        :return: if found: merchant with specific id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, address FROM merchants WHERE id = '?';", id)
        length = len(cursor)
        if length == 0:
            return None

        data = cursor.fetchone()

        merchant = Merchant(data[0], data[1], data[2])
        return merchant

    def getPerson(self, id):
        """
        Returns a person with given id
        :param id: int - the id to search for
        :return: if found: person with specific id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, class FROM persons WHERE id = '?'", id)
        length = len(cursor)
        if length == 0:
            return None

        data = cursor.fetchone()
        person = Person(data[0], data[1], data[2])
        return person

    def getBook(self, id):
        """
        Returns a book with given id
        :param id: int the id to search for
        :return: if found: book with given id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, template_id, borrowed_by FROM books WHERE id = '?'", id)
        length = len(cursor)
        if length == 0:
            return None

        data = cursor.fetchone()
        template = self.getBookTemplate(data[1])
        if template == None:
            print "book with none existing book_template in database..."
            return None
        borrowed_by = data[2]
        if borrowed_by != None:
            borrowed_by = self.getPerson(borrowed_by)

        book = Book(data[0], template, borrowed_by)
        return book


database = Database()
