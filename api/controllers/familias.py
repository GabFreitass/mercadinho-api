from flask_restful import Resource
from .. import server
from ..models import Produtos


class Familias(Resource):

	def get(self):
		produtos = Produtos.query.all()
		result = [
			{
				"CodPro": produto.CodPro,
				"DesPro": produto.DesPro, 
				"PcoVen": float(produto.PcoVen)
			} for produto in produtos]
		return result

server.api.add_resource(Familias, "/familias")
