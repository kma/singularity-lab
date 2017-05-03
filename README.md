# Singularity use case

Create a reproducible container image to run a simple python program (`data_alaysys.py`).

This code takes a csv file and plots results in two separated pdf files.

The csv can be found [[here]](http://info.iut-bm.univ-fcomte.fr/staff/mazouzi/docs/ganglia-metrics.csv)

## Create image container localy
Run `build-local` to create and bootstrap a container (This action needs root access).

```bash
$ sudo singularity create -s 1000 mycontainer.img
$ sudo singularity bootstrap mycontainer.img Singularity
```



## Run python code inside container 

Run `run-local.sh` to execute python code inside the contanier. 

```bash
$ wget http://info.iut-bm.univ-fcomte.fr/staff/mazouzi/docs/ganglia-metrics.csv

$ ./mycontainer data_analaysis

```

## Pull image container from singularity-hub 

If you don't root access, singularity-hub can create images by providing a specification file. See the [[documentation]](https://singularity-hub.org/faq) for more details . The image correspending to the `Singularity` file can be pulled from https://singularity-hub.org/containers/842/.

Pull image:
```bash
$ singularity pull shub://842
Or
$ singularity pull shub://kma/singularity-lab:master 
```

Run python code using:
```bash
$ singularity exec kma-singularity-lab-master.img python data_analysis.py
```
Or 
```bash
$ ./kma-singularity-lab-master.img data_analysis.py
```


