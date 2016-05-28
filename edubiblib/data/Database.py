import sqlite3
from models.BookTemplate import BookTemplate
from models.Merchant import Merchant


class Database(object):
    """
    Database Class used to Access Database and get Object Models
    Ensure that this only exists once!
    """
    def __init__(self):
        """
        Constructor, initialize the database connection to a local database
        """
        self.connection = sqlite3.connection("eduBib.sqlite")
        self.checkTables()

    def checkTables(self):
        """
        Check all tables. Create them of they dont exist.
        """
        cursor = self.connection.cursor()
        ### Check book_template table
        try:
            cursor.execute("SELECT 1 FROM book_template LIMIT 1");
        except:
            print "book_template does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE book_template (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, isbn STRING, name STRING, author STRING, publisher STRING)")
            self.connection.commit()

        try:
            cursor.execute("SELECT 1 FROM books LIMIT 1");
        except:
            print "books does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, template_id INTEGER, borrowed_by INTEGER)")
            self.connection.commit()

        try:
            cursor.execute("SELECT 1 FROM merchants LIMIT 1")
        except:
            print "merchants does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE merchants (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name STRING, address STRING)")
            self.connection.commit();

        try:
            cursor.execute("SELECT 1 FROM persons LIMIT 1")
        except:
            print "persons does not exist. Create it."
            self.connection.commit()
            cursor.execute("CREATE TABLE persons (id INTEGER PRIMArY KEY AUTOINCREMENT NOT NULL, name STRING, klasse STRING)")
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

        bookTemplate = BuchTemplate(data[0], data[1], data[2], data[3], data[5])
        cursor.close()
        return bookTemplate # TODO: Return None if no book template with given id

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
        return merchant # TODO: Return None if no merchant with given id