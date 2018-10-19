# DRoVirt
Disaster Recovery / Replication for oVirt/RHV

DRoVirt project has been created to address the need of Disaster-Recovery process of oVirt/RHV environments.
DRoVirt's main objective is to provide simple way to replicate VMs running on one oVirt environment.

Our plan is to deliver a Python-based solution that consists of 3 components:

* **Data-mover** - responsible for grabbing periodically data and transferring it
* **Server/API** - central management point to invoke tasks
* **Database** - small DB to store current tasks
* **CLI** - util to easier manage replication tasks and configuration

The actual implementation of the recplication is subject of discussion. Initially we want to start with oVirt/RHV 4.2 Disk Image Transfer API and later add additional strategies.

## Proposed architecture

DRoVirt data mover is suppsoed to periodically snapshot and export data from RHV/oVirt API and transfer it to second location where increments can be restored.
![DRoVirt architecture](https://raw.githubusercontent.com/Storware/drovirt/master/img/DRoVirt-architecture.png)
