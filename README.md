# DRoVirt
Disaster Recovery / Replication for oVirt/RHV

DRoVirt project has been created to address the need of Disaster-Recovery process of oVirt/RHV environments.
DRoVirt's main objective is to provide a simple way to replicate VMs running in an oVirt environment.

Our plan is to deliver a Python-based solution that consists of 3 components:

* **Data-mover** - responsible for grabbing data periodically and transferring it
* **Server/API** - central management point to invoke tasks
* **Database** - small DB to store current tasks
* **CLI** - utility to easier manage the replication configuration tasks

The actual implementation of the replication is subject to discussion. Initially we want to start with oVirt/RHV 4.2 Disk Image Transfer API and later add additional strategies.

## Proposed architecture

DRoVirt data mover is supposed to periodically snapshot and export data from RHV/oVirt API and transfer it to a second location where increments can be restored.
![DRoVirt architecture](https://raw.githubusercontent.com/Storware/drovirt/master/img/DRoVirt-architecture.png)
