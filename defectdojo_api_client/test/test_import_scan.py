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
from defectdojo_api_client.models.import_scan import ImportScan  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestImportScan(unittest.TestCase):
    """ImportScan unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ImportScan
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.import_scan.ImportScan()  # noqa: E501
        if include_optional :
            return ImportScan(
                scan_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                minimum_severity = 'Info', 
                active = True, 
                verified = True, 
                scan_type = '', 
                endpoint_to_add = 56, 
                test_type = '0', 
                file = '0', 
                engagement = 56, 
                lead = 56, 
                tags = [
                    '0'
                    ], 
                close_old_findings = True, 
                push_to_jira = True
            )
        else :
            return ImportScan(
                scan_type = '',
                engagement = 56,
        )

    def testImportScan(self):
        """Test ImportScan"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
