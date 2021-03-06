# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import defectdojo_api_client
from defectdojo_api_client.models.scan_settings_create import ScanSettingsCreate  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestScanSettingsCreate(unittest.TestCase):
    """ScanSettingsCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ScanSettingsCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.scan_settings_create.ScanSettingsCreate()  # noqa: E501
        if include_optional :
            return ScanSettingsCreate(
                id = 56, 
                user = 56, 
                product = 56, 
                data = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                addresses = '0', 
                date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                frequency = '0', 
                email = '0', 
                protocol = '0'
            )
        else :
            return ScanSettingsCreate(
                user = 56,
                product = 56,
                email = '0',
        )

    def testScanSettingsCreate(self):
        """Test ScanSettingsCreate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
