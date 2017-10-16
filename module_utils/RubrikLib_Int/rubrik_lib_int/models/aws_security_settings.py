# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AwsSecuritySettings(Model):
    """AwsSecuritySettings.

    :param aws_security_group_ids: For AWS instances, this is the security
     group ID. For images, this is the default security group ID for new
     instances from this image.
    :type aws_security_group_ids: list of str
    """

    _attribute_map = {
        'aws_security_group_ids': {'key': 'awsSecurityGroupIds', 'type': '[str]'},
    }

    def __init__(self, aws_security_group_ids=None):
        self.aws_security_group_ids = aws_security_group_ids