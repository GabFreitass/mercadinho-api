from api import server

db = server.db

class Produtos(db.Model):
	CodPro = db.Column(db.Integer, primary_key=True)
	DesPro = db.Column(db.String(121))
	PcoCus = db.Column(db.Numeric)
	PcoVen = db.Column(db.Numeric)

	def __repr__(self):
		return f'Produto({self.CodPro}, {self.DesPro})'
