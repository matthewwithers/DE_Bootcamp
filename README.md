# DE_Bootcamp

--adding docker image for pgsql
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v /Users/matthew.withers/Desktop/DE_Bootcamp/docker/ny_taxi_postgres_data -p 5432:5432 postgres:13

--pgcli -h localhost -p 5432 -u root -d ny_taxi
