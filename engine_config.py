import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

class Config:
    """En klass för att hantera konfigurationsinställningar i projektet."""

    # Databasinställningar
    DATABASES = {
        "default": {
            "drivername": "mssql+pyodbc",
            "username": os.getenv("PROJECT_DB_USER"),
            "password": os.getenv("PROJECT_DB_PW"),
            "host": "drorsenprojectserver.database.windows.net",
            "port": 1433,
            "database": "project_db",
            "query": {"driver": "ODBC Driver 17 for SQL Server"}
        },
        # Möjlighet att lägga till fler databaser om det behövs
        # "another_db": {
        #     "drivername": "postgresql",
        #     "username": "user",
        #     "password": "password",
        #     "host": "another-host",
        #     "port": 5432,
        #     "database": "another_db"
        # }
    }

    # Övriga inställningar
    # DEBUG = os.getenv("PROJECT_DEBUG", "False").lower() == "true"
    # LOG_LEVEL = os.getenv("PROJECT_LOG_LEVEL", "INFO")
    # SECRET_KEY = os.getenv("PROJECT_SECRET_KEY", "mysecret")

# Skapa engine baserat på standarddatabasen
DATABASE_URL = URL.create(**Config.DATABASES["default"])
engine = create_engine(DATABASE_URL)