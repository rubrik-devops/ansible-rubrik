# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ThrottlingSettings(Model):
    """ThrottlingSettings.

    :param enable_throttling: Whether or not to enable throttling
    :type enable_throttling: bool
    :param vm_io_latency_threshold: Latency threshold in ms observed by a VM
     beyond which to throttle VM backups
    :type vm_io_latency_threshold: int
    :param datastore_io_latency_threshold: Latency threshold in ms observed
     across all of a VM's datastores beyond which to throttle VM backups
    :type datastore_io_latency_threshold: int
    :param cpu_utilization_threshold: CPU utilization percentage beyond which
     to throttle VM backups
    :type cpu_utilization_threshold: int
    :param mssql_host_io_latency_threshold: Latency threshold in ms observed
     by a Mssql host beyond which to throttle database backups
    :type mssql_host_io_latency_threshold: int
    :param mssql_cpu_utilization_threshold: CPU utilization percentage of
     Mssql host beyond which to throttle Mssql database backups
    :type mssql_cpu_utilization_threshold: int
    :param fileset_host_io_latency_threshold: Latency threshold in ms observed
     by a Fileset host beyond which to throttle backups
    :type fileset_host_io_latency_threshold: int
    :param fileset_cpu_utilization_threshold: CPU utilization percentage of a
     Fileset host beyond which to throttle backups
    :type fileset_cpu_utilization_threshold: int
    """

    _validation = {
        'enable_throttling': {'required': True},
    }

    _attribute_map = {
        'enable_throttling': {'key': 'enableThrottling', 'type': 'bool'},
        'vm_io_latency_threshold': {'key': 'vmIoLatencyThreshold', 'type': 'int'},
        'datastore_io_latency_threshold': {'key': 'datastoreIoLatencyThreshold', 'type': 'int'},
        'cpu_utilization_threshold': {'key': 'cpuUtilizationThreshold', 'type': 'int'},
        'mssql_host_io_latency_threshold': {'key': 'mssqlHostIoLatencyThreshold', 'type': 'int'},
        'mssql_cpu_utilization_threshold': {'key': 'mssqlCpuUtilizationThreshold', 'type': 'int'},
        'fileset_host_io_latency_threshold': {'key': 'filesetHostIoLatencyThreshold', 'type': 'int'},
        'fileset_cpu_utilization_threshold': {'key': 'filesetCpuUtilizationThreshold', 'type': 'int'},
    }

    def __init__(self, enable_throttling, vm_io_latency_threshold=None, datastore_io_latency_threshold=None, cpu_utilization_threshold=None, mssql_host_io_latency_threshold=None, mssql_cpu_utilization_threshold=None, fileset_host_io_latency_threshold=None, fileset_cpu_utilization_threshold=None):
        self.enable_throttling = enable_throttling
        self.vm_io_latency_threshold = vm_io_latency_threshold
        self.datastore_io_latency_threshold = datastore_io_latency_threshold
        self.cpu_utilization_threshold = cpu_utilization_threshold
        self.mssql_host_io_latency_threshold = mssql_host_io_latency_threshold
        self.mssql_cpu_utilization_threshold = mssql_cpu_utilization_threshold
        self.fileset_host_io_latency_threshold = fileset_host_io_latency_threshold
        self.fileset_cpu_utilization_threshold = fileset_cpu_utilization_threshold