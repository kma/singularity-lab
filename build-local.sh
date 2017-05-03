#!/bin/bash

echo "Building local image..."
sudo singularity create -s 1000 mycontainer.img

echo "Bootstraping image..."
sudo singularity bootstrap mycontainer.img Singularity
