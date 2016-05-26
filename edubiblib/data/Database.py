import sqlite3
from models import BookTemplate


class Database(object):
    """
    Database Class used to Access Database and get Object Models
    Ensure that this only exists once!
    """
    def __init__(self):
        """
        Constructor, initialize the database connection to a local database
        """
        self.connection = sqlite3.connection("datenbank.sqlite")
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
        res = cursor.execute("SELECT id, isbn, name, autor, verlag FROM buecher_template WHERE id = '?';", id)
        data = cursor.fetchone()

        bookTemplate = BuchTemplate(data[0], data[1], data[2], data[3], data[5])
        cursor.close()
        return bookTemplate
