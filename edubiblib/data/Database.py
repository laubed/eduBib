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
        # TODO: Implement!
        pass

    def getBookTemplate(self, id):
        """
        Returns a book template from the database.
        :param id:  int - the book template id
        :return: if found: book template with the specified id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, isbn, name, autor, verlag FROM buecher_template WHERE id = '?';", id)
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
        data = cursor.fetchone()

        merchant = Merchant(data[0], data[1], data[2])
        return merchant # TODO: Return None if no merchant with given id