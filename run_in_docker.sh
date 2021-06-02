#!/bin/bash

set -u
set -e

echo This script is not working yet as expected!


IP=127.0.0.1
echo IP: $IP

IP_FOR_DOCKER=host.docker.internal

DISPLAY_NO=0

#open -a XQuartz

xhost + $IP

# https://hub.docker.com/r/osrf/ros/
image_name=osrf/ros:melodic-desktop-full

docker pull ${image_name}
docker run -it --rm \
    --user=root \
    -e HOME=/home/$USER \
    -e USER \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v /etc/group:/etc/group:ro \
    -v /etc/passwd:/etc/passwd:ro \
    -v /etc/sudoers.d:/etc/sudoers.d:ro \
    -v $HOME:/home/$USER \
    -v /tmp/ros/:/var/root/.ros \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e DISPLAY=$IP_FOR_DOCKER:$DISPLAY_NO \
    -e "QT_X11_NO_MITSHM=1" \
    ${image_name} $@
