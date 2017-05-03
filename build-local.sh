#!/bin/bash

echo "Building local image..."

sudo singularity create -s 1000 mycontainer.img

echo "Bootstraping image..."
sudo sungularity bootstrap Singularity mycontainer.img
