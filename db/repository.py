from db.connection import get_engine
from db.models import cryptocurrency, crypto_market_data
from sqlalchemy import select
from datetime import datetime

def insert_or_update_crypto(crypto_data):
    engine = get_engine()
    with engine.connect() as conn:
        # Insert or update cryptocurrency table
        for crypto in crypto_data:
            stmt = select(cryptocurrency).where(cryptocurrency.c.id == crypto["id"])
            result = conn.execute(stmt).fetchone()

            if result:
                update_stmt = (
                    cryptocurrency.update()
                    .where(cryptocurrency.c.id == crypto["id"])
                    .values(
                        name=crypto["name"],
                        symbol=crypto["symbol"],
                        rank=int(crypto["rank"])
                    )
                )
                conn.execute(update_stmt)
            else:
                insert_stmt = cryptocurrency.insert().values(
                    id=crypto["id"],
                    name=crypto["name"],
                    symbol=crypto["symbol"],
                    rank=int(crypto["rank"])
                )
                conn.execute(insert_stmt)

            # Insert market data
            insert_market_data_stmt = crypto_market_data.insert().values(
                crypto_id=crypto["id"],
                timestamp=datetime.utcnow(),
                price_usd=float(crypto["priceUsd"]),
                market_cap_usd=float(crypto["marketCapUsd"]),
                volume_usd_24h=float(crypto["volumeUsd24Hr"]),
                change_pct_24h=float(crypto["changePercent24Hr"]),
            )
            conn.execute(insert_market_data_stmt)
        conn.commit()
