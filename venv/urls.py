from flask import Blueprint
from flask_restful import Api, Resource
from controllers.products import ProductsListController, ProductController
blueprint_urls = Blueprint('url_global', __name__)
api = Api(blueprint_urls, prefix='/api/web')

api.add_resource(ProductsListController, "/products")
api.add_resource(ProductController,"/product/<int:pk>")