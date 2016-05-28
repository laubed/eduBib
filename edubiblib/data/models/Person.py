

class Person(object):
	def __init__(self, id_, name, _class):
		self._id = id_
		self._name = name
		self._class = _class

	def getID(self):
		return self._id

	def getName(self):
		return self._name

	def getClass(self):
		return self._class

