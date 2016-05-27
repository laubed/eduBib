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

    def getBookTemplate(self, id_):
        """
        Returns a book template from the database.
        :param id:  int - the book template id
        :return: if found: book template with the specified id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, isbn, name, autor, verlag FROM buecher_template WHERE id = '?';", id_)
 	length = len(cursor)
	if length = 0:
		return None
		
        data = cursor.fetchone()

        bookTemplate = BookTemplate(data[0], data[1], data[2], data[3], data[4])
        cursor.close()
        return bookTemplate

    def getMerchant(self, id_):
        """
        Returns a merchant with given id
        :param id: int - the id to search for
        :return: if found: merchant with specific id, else None
        """
        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, address FROM merchants WHERE id = '?';", id_)
 	length = len(cursor)
	if length = 0:
		return None

        data = cursor.fetchone()

        merchant = Merchant(data[0], data[1], data[2])
        return merchant 

    def getPerson(self, id_):
	cursor = self.connection.cursor()
	cursor.execute("SELECT id, name, klasse FROM persons WHERE id = '?'", id_)
	length = len(cursor)
	if length == 0:
	    return None

        data = cursor.fetchone()
	person = Person(data[0], data[1], data[2])
	return person 
	
	
