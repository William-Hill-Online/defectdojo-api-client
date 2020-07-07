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
from defectdojo_api_client.models.inline_response2007 import InlineResponse2007  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestInlineResponse2007(unittest.TestCase):
    """InlineResponse2007 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2007
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.inline_response2007.InlineResponse2007()  # noqa: E501
        if include_optional :
            return InlineResponse2007(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    defectdojo_api_client.models.jira.JIRA(
                        id = 56, 
                        project_key = '0', 
                        component = '0', 
                        push_all_issues = True, 
                        enable_engagement_epic_mapping = True, 
                        push_notes = True, 
                        product = 56, 
                        conf = 56, )
                    ]
            )
        else :
            return InlineResponse2007(
                count = 56,
                results = [
                    defectdojo_api_client.models.jira.JIRA(
                        id = 56, 
                        project_key = '0', 
                        component = '0', 
                        push_all_issues = True, 
                        enable_engagement_epic_mapping = True, 
                        push_notes = True, 
                        product = 56, 
                        conf = 56, )
                    ],
        )

    def testInlineResponse2007(self):
        """Test InlineResponse2007"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()