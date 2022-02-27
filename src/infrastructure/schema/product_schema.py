from ..config.database import db

class ProductSchema(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Float(), nullable=False)
    brand = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Product {self.name} --> Brand {self.brand}>'