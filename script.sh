#/bin/bash
docker network create --subnet=172.20.0.0/16 customnetwork
docker run --net customnetwork --ip 172.20.0.5  -v dbdata:/data/db -d mongo
docker build -t myimage .
docker run -it --net customnetwork --env DB_HOST=172.20.0.5 -it  myimage