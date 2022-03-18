from flask_restful import Resource
from .. import server
from ..models import Produtos


class Produtos(Resource):

    def get(self):
        produtos = Produtos.query.all()
        result = [
            {
                "CodPro": produto.CodPro,
                "DesPro": produto.DesPro,
                "PcoCus": float(produto.PcoCus),
                "PcoVen": float(produto.PcoVen)
            } for produto in produtos]
        return result


server.api.add_resource(Produtos, "/produtos")
