#!/bin/bash

echo "Building local image..."

sudo singularity create -s 1000 mycontaner.img

echo "Bootstraping image..."
sudo sungularity bootstrap Singularity mycontaner.img
