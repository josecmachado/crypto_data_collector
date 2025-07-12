from sqlalchemy import Table, Column, String, Integer, Numeric, ForeignKey, MetaData, TIMESTAMP
from db.connection import get_engine

metadata = MetaData()

cryptocurrency = Table(
    "cryptocurrency",
    metadata,
    Column("id", String(50), primary_key=True),
    Column("name", String(255)),
    Column("symbol", String(50)),
    Column("rank", Integer),
)

crypto_market_data = Table(
    "crypto_market_data",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("crypto_id", String(50), ForeignKey("cryptocurrency.id")),
    Column("timestamp", TIMESTAMP),
    Column("price_usd", Numeric),
    Column("market_cap_usd", Numeric),
    Column("volume_usd_24h", Numeric),
    Column("change_pct_24h", Numeric),
)

def create_tables():
    engine = get_engine()
    metadata.create_all(engine)
