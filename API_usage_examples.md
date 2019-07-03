# DRoVirt REST API documentation

**DRoVirt** uses REST API for communitation with GUI, external applications and its processing nodes. This document provides practical examples needed to test the configuration.


## Adding Hypervisor Manager

**POST /hypervisor_manager** containing JSON specification of hypervisor manager

    
    {
    	"name":"ovirt-1",
    	"api_url":"https://192.168.0.100/ovirt-engine/api",
    	"username":"admin@internal",
    	"password":"password",
    	"allow_insecure": true,
    	"manager_type": "ovirt"
    	
    }
    

## Adding VM manually

**POST /vm**

    {
    	"name": "new_vm",
    	"vm_type": "server",
    	"status": "ok",
    	"cpus": 1,
    	"memory": 10240654,
    	"uuid": "32234123sfsdf-dsfswr-23r-fds",
    	"hypervisor_manager_id": 1
    }

## Loading VM list from Hypervisor Manager

Databse can be populated with VMs from hypervisor manager with:

	POST /hypervisor_manager/<hypervisor_manager_id>/load_vms

To get the identifier for hypervisor manager you can use:

	GET /hypervisor_manager