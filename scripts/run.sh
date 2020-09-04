#!/bin/bash

docker-compose down

# Remove dangling images (-q=quiet, -f=without prompt)
​docker rmi $(docker images -q -f dangling=true)

# Remove all stopped containers
docker rm -v $(docker ps -a -q -f status=exited)

# Remove dangling volumes
docker volume rm $(docker volume ls -qf dangling=true)

# Spin up the new container
# The if-else and the getopts is to take in the worker argument
if getopts "n:" arg; then
docker-compose -f docker-compose.yml up \
                -d                      \
                --build                  \
                --scale worker=$OPTARG
else
docker-compose -f docker-compose.yml up \
                -d                      \
                --build                  \
                --scale worker=1
fi
