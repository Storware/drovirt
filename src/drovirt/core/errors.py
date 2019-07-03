
class UnsupportedHypervisorManagerAction(Exception):
    def __init__(self, manager_type, action):
        self.action = action
        self.manager_type = manager_type

    def __str__(self):
        return "Hypervisor Manager of type %s does not support %s" % (self.manager_type, self.action)
