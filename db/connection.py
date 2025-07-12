from sqlalchemy import create_engine
from config.settings import DB_SETTINGS

def get_engine():
    """
    Cria e retorna a conexão com o banco de dados PostgreSQL
    usando SQLAlchemy. O pool_pre_ping evita problemas com conexões inativas.
    """
    conn_str = (
        f"postgresql+psycopg2://{DB_SETTINGS['user']}:"
        f"{DB_SETTINGS['password']}@{DB_SETTINGS['host']}:"
        f"{DB_SETTINGS['port']}/{DB_SETTINGS['database']}"
    )
    return create_engine(conn_str, echo=True, pool_pre_ping=True)
