class BookTemplate(object):
    """
    Book template class. Holds all necessary information about a book template.
    """
    def __init__(self, id, isbn, name, autor, verlag):
        self._id = id
        self._isbn = isbn
        self._title = title
        self._author = author
        self._publisher = publisher

    def getID(self):
        """
        Getter for id
        :return: the book template ID
        """
        return self._id

    def getISBN(self):
        """
        Getter for isbn
        :return: the book template isbn
        """
        return self._isbn

    def getTitle(self):
        """
        Getter for title
        :return: the book template title
        """
        return self._title

    def getAuthor(self):
        """
        Getter for author
        :return: the book template author
        """
        return self._author

    def getPublisher(self):
        """
        Getter for publisher
        :return: the book template publisher
        """
        return self._publisher
