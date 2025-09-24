#!/bin/bash
containerID=`docker ps | awk -F" " '{Print $1}'`

docker rm -f $containerID

