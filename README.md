# DE_Bootcamp

--adding docker image for pgsql
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v /Users/matthew.withers/Desktop/DE_Bootcamp/docker/ny_taxi_postgres_data -p 5432:5432 postgres:13

--pgcli -h localhost -p 5432 -u root -d ny_taxi

--docker build -t taxi_ingest:v001 .

URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
python3 ingest_data.py --user=root --password=root --host=localhost --port=5432 --db=ny_taxi --tblname=yellow_taxi_trips --url=${URL}

--create a network for the postgres database to run in
docker create network postgres_backend

docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v /Users/matthew.withers/Desktop/DE_Bootcamp/docker/ny_taxi_postgres_data -p 5432:5432 --network=postgres_backend --name=pg_database postgres:13

--run the image within the newly created docker network
docker run -it --network=postgres_backend taxi_ingest:v001 --user=root --password=root --host=pg_database --port=5432 --db=ny_taxi --tblname=yellow_taxi_trips --url=${URL}
