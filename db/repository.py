from db.models import cryptocurrency, crypto_market_data
from db.connection import get_engine
from sqlalchemy import select

def insert_or_update_cryptos(cryptos):
    """
    Recebe uma lista de criptomoedas e insere ou atualiza no banco.
    """
    engine = get_engine()

    with engine.connect() as conn:
        for crypto in cryptos:
            # Verifica se a moeda já existe
            stmt = select(cryptocurrency).where(
                cryptocurrency.c.id == crypto["id"]
            )
            result = conn.execute(stmt).fetchone()

            if result:
                # Atualiza dados caso já exista
                update_stmt = cryptocurrency.update().where(
                    cryptocurrency.c.id == crypto["id"]
                ).values(
                    name=crypto["name"],
                    symbol=crypto["symbol"],
                    rank=int(crypto["rank"])
                )
                conn.execute(update_stmt)
            else:
                # Insere nova moeda
                insert_stmt = cryptocurrency.insert().values(
                    id=crypto["id"],
                    name=crypto["name"],
                    symbol=crypto["symbol"],
                    rank=int(crypto["rank"])
                )
                conn.execute(insert_stmt)

            # Insere dados de mercado
            insert_market_data_stmt = crypto_market_data.insert().values(
                crypto_id=crypto["id"],
                timestamp=crypto["timestamp"],
                price_usd=crypto["priceUsd"],
                market_cap_usd=crypto["marketCapUsd"],
                volume_usd_24h=crypto["volumeUsd24Hr"],
                change_pct_24h=crypto["changePercent24Hr"],
            )
            conn.execute(insert_market_data_stmt)

        conn.commit()
