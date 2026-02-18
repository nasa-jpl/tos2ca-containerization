#!/bin/bash

# Environmental variavles setup
# $HOME should be your user's home directory on your system
# $REPO_DIR should be the directory where you have cloned this repository

git clone git@github.com:nasa-jpl/tos2ca-containerization.git   $REPO_DIR

# First remove all existing git directories from the directory so we get a clean copy
rm -rf $HOME/docker_executable
mkdir $HOME/docker_executable
mkdir $HOME/docker_executable/code

# Copy over build files
# the containerization repo is the clone of this repository
# this assumes your NASA Earthdata .netrc file is in $HOME
cp -p $REPO_DIR/containerization/tos2ca_*_driver.py   $HOME/docker_executable/
cp -p $REPO_DIR/containerization/Dockerfile*          $HOME/docker_executable/
cp -p $REPO_DIR/containerization/requirements.txt     $HOME/docker_executable/
cp -p $HOME/.netrc                                    $HOME/docker_executable/
chmod a+r $HOME/docker_executable/.netrc

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

## Run Containers Locally
# docker run --rm -it -e JOBID=<jobID> -e CHUNKID=<chunkID> data_driver
## List containers
# docker ps -a
## Removing Containers (if you didn't use --rm above)
# docker rm <container ID>

## You can also run these containers in AWS ECS, which is recommended, but you'll
## need to do some setup on your own for that.

