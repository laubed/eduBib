

class Merchant(object):
    """
    Merchant database model class. Contains all data that belongs to a merchant.
    """
    def __init__(self, id, name, address):
        """
        Constructor prefilling all attributes
        """
        self._id = id
        self._name = name
        self._address = address

    def getID(self):
        """
        Getter for id
        :return: return merchant id
        """
        return self._id

    def getName(self):
        """
        Getter for name
        :return: returns merchant id
        """
        return self._name

    def getAddress(self):
        """
        Getter for address
        :return: returns merchant adress
        """
        return self._address
