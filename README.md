# drovirt
Disaster Recovery / Replication for oVirt/RHV

DRoVirt project has been created to address the need of Disaster-Recovery process of oVirt/RHV environments.
DRoVirt's main objective is to provide simple way to replicate VMs running on one oVirt environment.

Our plan is to deliver a Python-based solution that consists of 3 components:
* Data-mover - responsible for grabbing periodically data and transferring it
* Server/API - central management point to invoke tasks
* Database - small DB to store current tasks
* CLI - util to easier manage replication tasks and configuration

