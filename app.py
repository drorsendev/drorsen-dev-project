from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from engine_config import engine
from db_table_schemas import Product, Category

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # Fixar så att svenska tecken visas korrekt

# Skapa en session factory
SessionLocal = sessionmaker(bind=engine)

@app.route("/products", methods=["GET"])
def get_products():
    """Hämta alla produkter från databasen utan att hårdkoda kolumner."""
    with SessionLocal() as session:
        products = session.query(Product).all()

        # Dynamiskt hämta alla kolumner i Product-tabellen
        data = [
            {column.name: getattr(p, column.name) for column in Product.__table__.columns}
            for p in products
        ]

        # Lägg till kategorinamn om en kategori finns
        for item, product in zip(data, products):
            item["category"] = product.category.name if product.category else None

    return jsonify(data)  # Returnerar JSON med alla produkter

if __name__ == "__main__":
    app.run(debug=True)
