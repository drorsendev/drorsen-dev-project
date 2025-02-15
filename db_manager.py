import argparse
from sqlalchemy.orm import sessionmaker
from db_table_schemas import Base, Product, Category
from engine_config import engine

# Skapa en session factory
SessionLocal = sessionmaker(bind=engine)

def create_tables():
    """Skapar alla tabeller i databasen om de inte redan finns."""
    print("Skapar tabeller...")
    Base.metadata.create_all(engine)
    print("Tabeller skapade!")

def drop_all_tables():
    """Raderar alla tabeller i databasen."""
    print("Droppar alla tabeller...")
    Base.metadata.drop_all(engine)
    print("Alla tabeller har raderats!")

def reset_database():
    """Raderar och återskapar databasen."""
    drop_all_tables()
    create_tables()
    add_initial_data()
    print("Databasen har återställts!")

def add_initial_data():
    """Lägger till startdata i databasen om den är tom."""
    with SessionLocal() as session:
        # Kontrollera om det redan finns data
        if session.query(Product).count() > 0:
            print("Startdata finns redan, ingen åtgärd.")
            return

        print("Lägger till startdata...")

        # Skapa kategorier
        category1 = Category(name="Kontorsmaterial")
        category2 = Category(name="Elektronik")

        session.add_all([category1, category2])
        session.commit()

        # Lägga till produkter kopplade till kategorierna
        products = [
            Product(name="Pärm", price=99.99, category_id=category1.id),
            Product(name="Bok", price=150.00, category_id=category1.id),
            Product(name="Dator", price=7999.00, category_id=category2.id),
        ]

        session.add_all(products)
        session.commit()
        
        print("Startdata har lagts till!")

def main():
    """Hanterar kommandoradsargument för att styra databasoperationer."""
    parser = argparse.ArgumentParser(description="Hantera databasoperationer.")
    parser.add_argument("--action", choices=["create", "drop", "reset", "seed"], required=True,
                        help="Välj en åtgärd: create, drop, reset eller seed.")

    args = parser.parse_args()

    if args.action == "create":
        create_tables()
    elif args.action == "drop":
        drop_all_tables()
    elif args.action == "reset":
        reset_database()
    elif args.action == "seed":
        add_initial_data()
    else:
        print("Ogiltigt val. Använd --action create, drop, reset eller seed.")

if __name__ == "__main__":
    main()