containers=$(docker ps |grep remote_ | awk '{print $1}')
docker container stop $containers
# docker container rm -f $containers
