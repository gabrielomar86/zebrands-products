from src.domain.model.product_model import ProductModel
from src.domain.repositories.product_repository_interface import ProductRepositoryInterface
from src.infrastructure.schema.product_schema import ProductSchema


class ProductRepository(ProductRepositoryInterface):
    def get_all_products(self):
        products = ProductSchema.query.all()
        return [
            ProductModel(product.id, product.sku, product.name, product.price, product.brand) 
            for product in products
        ]
    
    def get_product(self, product_id):
        product = ProductSchema.query.filter_by(id = product_id).first()
        return ProductModel(product.id, product.sku, product.name, product.price, product.brand)
    
    def update_product(self, product_id, product: ProductModel):
        productDb = ProductSchema.query.filter_by(id = product_id).first()
        productDb.sku = product.sku
        productDb.name = product.name
        productDb.price = product.price
        productDb.brand = product.brand
        ProductSchema.query.update(productDb)
        pass
    
    def insert_product(self, product: ProductModel):
        # db.session.add(product)
        # db.session.commit()
        pass
    
    def delete_product(self, product_id):
        # productDb = ProductSchema.query.filter_by(id = product_id).first()
        # db.session.delete(productDb)
        # db.session.commit()
        pass