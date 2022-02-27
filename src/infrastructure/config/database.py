from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import src.infrastructure.schema.user_schema
import src.infrastructure.schema.product_schema
