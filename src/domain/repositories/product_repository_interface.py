from src.domain.model.product_model import ProductModel

class ProductRepositoryInterface():
    def get_all_products(self):
        pass
    
    def get_product(self, product_id):
        pass
    
    def update_product(self, product_id, product: ProductModel):
        pass
    
    def insert_product(self, product: ProductModel):
        pass
    
    def delete_product(self, product_id):
        pass