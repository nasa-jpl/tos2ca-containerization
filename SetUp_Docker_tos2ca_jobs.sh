#!/bin/bash

# First remove all existing git directories from the directory so we get a clean copy
rm -rf $HOME/docker_executable
mkdir $HOME/docker_executable
mkdir $HOME/docker_executable/code

# Copy over build files
# the containerization repo is the clone of this repository
# this assumes your NASA Earthdata .netrc file is in $HOME
cp -p $HOME/containerization/tos2ca_*_driver.py   $HOME/docker_executable/
cp -p $HOME/containerization/Dockerfile*          $HOME/docker_executable/
cp -p $HOME/containerization/requirements.txt     $HOME/docker_executable/
cp -p $HOME/.netrc                                $HOME/docker_executable/
chmod a+r $HOME/docker_executable/.netrc

# Grab copies of the necessary repos; you can grab a specific branch with the '-b' option if needed
git clone git@github.com:nasa-jpl/tos2ca-anomaly-detection.git                    $HOME/docker_executable/code/anomaly-detection
git clone git@github.com:nasa-jpl/tos2ca-data-dictionaries.git                    $HOME/docker_executable/code/data-dictionaries
git clone git@github.fortracc-module:TOS2CA/fortracc-module.git                   $HOME/docker_executable/code/fortracc-module                       

### Here's some suggested ways to build the Docker image and push them to an AWS ECR
## Building Images
# docker build -t data_driver . -f Dockerfile_tos2ca_data_driver
## Listing Images
# docker image ls
## Removing Images
# docker rmi <name>

## Tag to Image
# docker tag <image ID> <AWS URI>/<repo name>:<tag>
## Push to AWS ECR
# aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <AWS URI>
# docker push <AWS URI>/<repo name>:<tag>

## Run Containers 
# docker run --rm -it -e JOBID=<jobID> -e CHUNKID=<chunkID> data_driver
## List containers
# docker ps -a
## Removing Containers (if you didn't use --rm above)
# docker rm <container ID>

