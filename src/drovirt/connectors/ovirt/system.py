
def get_vms(connection):
    vms_service = connection.system_service().vms_service()
    vms = vms_service.list()
    return vms
