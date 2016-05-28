# TODO: Ben
# Implement a book class for one instance of a book. Think of all required attributes
class Book(object):
	def __init__(self,id,template, borrowed_by):
		self.id = id
		self.template = template
		self.borrowed_by = borrowed_by
