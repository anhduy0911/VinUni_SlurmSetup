# Slurm setup for VinUni-SHC Server
`Dockerfile_*`: all the dockerfiles for building the images of worker nodes, jupyter (sandbox) and master node.

`docker-compose.yml`: the docker-compose file for running the cluster.

`slurm.conf`: the slurm configuration file.

`gres`: the gres configuration file.

**Note**: Remember to create the docker volume named `shared-vol` before running the cluster with compose.