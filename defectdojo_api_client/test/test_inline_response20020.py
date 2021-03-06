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
from defectdojo_api_client.models.inline_response20020 import InlineResponse20020  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestInlineResponse20020(unittest.TestCase):
    """InlineResponse20020 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20020
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.inline_response20020.InlineResponse20020()  # noqa: E501
        if include_optional :
            return InlineResponse20020(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    defectdojo_api_client.models.tool_product_settings.ToolProductSettings(
                        id = 56, 
                        setting_url = '0', 
                        name = '0', 
                        description = '0', 
                        url = '0', 
                        tool_project_id = '0', 
                        product = 56, 
                        tool_configuration = 56, 
                        notes = [
                            56
                            ], )
                    ]
            )
        else :
            return InlineResponse20020(
                count = 56,
                results = [
                    defectdojo_api_client.models.tool_product_settings.ToolProductSettings(
                        id = 56, 
                        setting_url = '0', 
                        name = '0', 
                        description = '0', 
                        url = '0', 
                        tool_project_id = '0', 
                        product = 56, 
                        tool_configuration = 56, 
                        notes = [
                            56
                            ], )
                    ],
        )

    def testInlineResponse20020(self):
        """Test InlineResponse20020"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
