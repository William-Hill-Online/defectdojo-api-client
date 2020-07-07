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
from defectdojo_api_client.models.inline_response2002 import InlineResponse2002  # noqa: E501
from defectdojo_api_client.rest import ApiException

class TestInlineResponse2002(unittest.TestCase):
    """InlineResponse2002 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2002
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = defectdojo_api_client.models.inline_response2002.InlineResponse2002()  # noqa: E501
        if include_optional :
            return InlineResponse2002(
                count = 56, 
                next = '0', 
                previous = '0', 
                results = [
                    defectdojo_api_client.models.engagement.Engagement(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        name = '0', 
                        description = '0', 
                        version = '0', 
                        first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        reason = '0', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        active = True, 
                        tracker = '0', 
                        test_strategy = '0', 
                        threat_model = True, 
                        api_test = True, 
                        pen_test = True, 
                        check_list = True, 
                        status = 'Not Started', 
                        progress = '0', 
                        tmodel_path = '0', 
                        risk_path = '0', 
                        done_testing = True, 
                        engagement_type = 'Interactive', 
                        build_id = '0', 
                        commit_hash = '0', 
                        branch_tag = '0', 
                        source_code_management_uri = '0', 
                        deduplication_on_engagement = True, 
                        eng_type = 56, 
                        lead = 56, 
                        requester = 56, 
                        preset = 56, 
                        report_type = 56, 
                        product = 56, 
                        build_server = 56, 
                        source_code_management_server = 56, 
                        orchestration_engine = 56, 
                        risk_acceptance = [
                            56
                            ], )
                    ]
            )
        else :
            return InlineResponse2002(
                count = 56,
                results = [
                    defectdojo_api_client.models.engagement.Engagement(
                        id = 56, 
                        tags = [
                            '0'
                            ], 
                        name = '0', 
                        description = '0', 
                        version = '0', 
                        first_contacted = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_start = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        target_end = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        reason = '0', 
                        updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        active = True, 
                        tracker = '0', 
                        test_strategy = '0', 
                        threat_model = True, 
                        api_test = True, 
                        pen_test = True, 
                        check_list = True, 
                        status = 'Not Started', 
                        progress = '0', 
                        tmodel_path = '0', 
                        risk_path = '0', 
                        done_testing = True, 
                        engagement_type = 'Interactive', 
                        build_id = '0', 
                        commit_hash = '0', 
                        branch_tag = '0', 
                        source_code_management_uri = '0', 
                        deduplication_on_engagement = True, 
                        eng_type = 56, 
                        lead = 56, 
                        requester = 56, 
                        preset = 56, 
                        report_type = 56, 
                        product = 56, 
                        build_server = 56, 
                        source_code_management_server = 56, 
                        orchestration_engine = 56, 
                        risk_acceptance = [
                            56
                            ], )
                    ],
        )

    def testInlineResponse2002(self):
        """Test InlineResponse2002"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()