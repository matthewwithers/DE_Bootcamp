# %%
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
from time import time
import argparse
import os


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.tblname
    url = params.url
    file_name = 'yellow_tripdata_2021-01.parquet'

    os.system(f'curl -OL {url}')

    # %%
    # read metadata (download file)
    # pq.read_metadata(file_name)

    # %%
    # Read file, read the table from file and check schema
    file = pq.ParquetFile(file_name)
    table = file.read()
    table.schema

    # %%
    # Convert to pandas and check data
    df = table.to_pandas()
    df.info()

    # %%
    # Create an open SQL database connection object or a SQLAlchemy connectable

    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    # %%
    # Generate CREATE SQL statement from schema for validation
    print(pd.io.sql.get_schema(df, name=table_name, con=engine))

    # Creating just the table in postgres
    df.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    # %%
    # insert values into the table
    t_start = time()
    count = 0
    for batch in file.iter_batches(batch_size=1000000):
        count += 1
        batch_df = batch.to_pandas()
        print(f'inserting batch {count}...')
        b_start = time()

        batch_df.to_sql(name=table_name,
                        con=engine, if_exists='append')
        b_end = time()
        print(f'inserted! time taken {b_end-b_start:10.3f} seconds.\n')

    t_end = time()
    print(
        f'Completed! Total time taken was {t_end-t_start:10.3f} seconds for {count} batches.')

    # %%


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Ingest parquet data to Postgres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host name for postgres')
    parser.add_argument('--port', help='port name for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument(
        '--tblname', help='name of the table we want to write the file results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)
