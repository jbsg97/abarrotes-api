from flask_restful import Resource, request
from models.models import Products
from server import db
from serializers.products import products_schema, product_schema

class ProductsListController(Resource):
    
    def get(self):
        products = Products.query.all()
        return {"data": products_schema.dump(products), "message": "exito"}

    def post(self):
        data = {
            "nombre": request.json['nombre'],
            "precio": request.json['precio'],
            "stock": request.json['stock'],
            "descripcion": request.json['descripcion'],
        }
        new_product = Products(**data)
        db.session.add(new_product)
        db.session.commit()
        return {'data': product_schema.dump(new_product)}

class ProductController(Resource):

    def get(self, pk):
        user = Products.query.get(pk)
        if not user:
            return {"Mensaje":"No se encontro el producto"}, 404
        single_user = []
        single_user.append(user.to_json())
        return {'Producto':product_schema.dump(user)}
        

    def put(self, pk):
        product = Products.query.get(pk)
        if not product:
            return {"mensaje":"No se encontro el producto"}, 404
        data = {
            "nombre": request.json['nombre'],
            "precio": request.json['precio'],
            "stock": request.json['stock'],
            "descripcion": request.json['descripcion'],
        }
        product.nombre = data["nombre"]
        product.precio = data["precio"]
        product.stock = data["stock"]
        product.descripcion = data["descripcion"]


        
        db.session.add(product)
        db.session.commit()
        return {"Producto": product_schema.dump(product),"mensaje":"actualizado"}

    def delete(self,pk):
            product = Products.query.get(pk)
            if not product:
                return {"mensaje":"No se encontro el producto"}
            db.session.delete(product)
            db.session.commit()
            return {"Producto": product_schema.dump(product),"mensaje":"Eliminado"}


