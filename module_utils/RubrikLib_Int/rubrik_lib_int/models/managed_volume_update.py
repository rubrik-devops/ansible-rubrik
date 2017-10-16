# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedVolumeUpdate(Model):
    """ManagedVolumeUpdate.

    :param name: Change the name of this managed volume
    :type name: str
    :param configured_sla_domain_id: Assign this managed volume to the given
     SLA domain.
    :type configured_sla_domain_id: str
    :param volume_size: Increase capacity for the volume across all the
     channels.
    :type volume_size: long
    :param config:
    :type config: :class:`ManagedVolumeExportConfig
     <rubriklib_int.models.ManagedVolumeExportConfig>`
    """

    _validation = {
        'volume_size': {'minimum': 0},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'configured_sla_domain_id': {'key': 'configuredSlaDomainId', 'type': 'str'},
        'volume_size': {'key': 'volumeSize', 'type': 'long'},
        'config': {'key': 'config', 'type': 'ManagedVolumeExportConfig'},
    }

    def __init__(self, name=None, configured_sla_domain_id=None, volume_size=None, config=None):
        self.name = name
        self.configured_sla_domain_id = configured_sla_domain_id
        self.volume_size = volume_size
        self.config = config