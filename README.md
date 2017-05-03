# Singularity-lab

Create a reproducible container image to run a simple python program (`data_alaysys.py`).

This code take a csv file and plot results in two separated pdf files.

The csv can be found [[here]](http://info.iut-bm.univ-fcomte.fr/staff/mazouzi/docs/ganglia-metrics.csv)

## Create image container localy
Run `build-local` to create and bootstrap a container (This action needs root access).

```bash
$ sudo singularity create -s 1000 mycontainer.img
$ sudo singularity bootstrap mycontainer.img Singularity
```



## Run python code inside container 

Run `run-me.sh` to execute python code inside the contanier. 

```bash
$ wget http://info.iut-bm.univ-fcomte.fr/staff/mazouzi/docs/ganglia-metrics.csv

$ ./mycontainer data_analaysis

```



## Pull image container from singularity-hub 
If you don't root access, singularity-hub can create images by providing a specification file. See the [[documentation]](https://singularity-hub.org/faq) for more details . The image correspending to the `Singularity` file can be download (pulled) from http://singularity-hub.org server.

