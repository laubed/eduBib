class BuchTemplate(object):
	def __init__(self, id, isbn, name, autor, verlag):
		self.id = id
		self.isbn = isbn
		self.name = name
		self.autor = autor
		self.verlag = verlag

class Datenbank(object):
	def __init__(self):
		self.connection = sqlite3.connection("datenbank.sqlite")
	
	def getBuchTemplateFromId(self, id):
		cursor = self.connection.cursor()
		res = cursor.execute("SELECT id, isbn, name, autor, verlag FROM buecher_template WHERE id = '?';", id)
		data = cursor.fetchone()
		
		buchTemplate = BuchTemplate(data[0], data[1], data[2], data[3], data[5])
		cursor.close()
		return buchTemplate
	

datenbank = Datenbank()
buchtemplate = datenbank.getBuchTemplateFromId(2)
