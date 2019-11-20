from marshmallow import Schema


class ProductSchema(Schema):

    class Meta:
        fields = ('id_producto','nombre', 'precio', 'stock', 'descripcion')
        ordered = True


products_schema = ProductSchema(many=True)
product_schema = ProductSchema()
