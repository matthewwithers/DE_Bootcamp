# DE_Bootcamp

--adding docker image for pgsql
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v /Users/matthew.withers/Desktop/DE_Bootcamp/docker/ny_taxi_postgres_data -p 5432:5432 postgres:13

--docker build -t taxi_ingest:v001 .

URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
--run the image within the newly created docker network
docker run -it --network=de_bootcamp_default taxi_ingest:v001 --user=root --password=root --host=pgdatabase --port=5432 --db=ny_taxi --tblname=yellow_taxi_trips --url=${URL}

> > docker-compose up
> > docker-compose down

specifying the the docker configuration for postgres and pgadmin allows those two services to be created within the same docker network. Becuase a custom network name was not given, it was autogenerated based on the project directory name de_bootcamp_default.

> > docker network ls

ingesting files from the internet
os.system('curl -L -o top-popular-anime.zip\
 https://www.kaggle.com/api/v1/datasets/download/tanishksharma9905/top-popular-anime && unzip top-popular-anime.zip')
