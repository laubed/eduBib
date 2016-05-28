# TODO: Ben
# Implement a book class for one instance of a book. Think of all required attributes
class Book(object):
	def __init__(self,id,template, borrowed_by):
		self._id = id
		self._template = template
		self._borrowed_by = borrowed_by

	def getID(self):
		return self._id

	def getTemplate(self):
		return self._template

	def getBorrowedBy(self):
		return self._borrowed_by
