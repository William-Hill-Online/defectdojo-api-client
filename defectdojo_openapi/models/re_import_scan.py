# coding: utf-8

"""
    Defect Dojo API

    To use the API you need be authorized.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from defectdojo_openapi.configuration import Configuration


class ReImportScan(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'scan_date': 'date',
        'minimum_severity': 'str',
        'active': 'bool',
        'verified': 'bool',
        'scan_type': 'str',
        'endpoint_to_add': 'int',
        'file': 'str',
        'test': 'int',
        'push_to_jira': 'bool'
    }

    attribute_map = {
        'scan_date': 'scan_date',
        'minimum_severity': 'minimum_severity',
        'active': 'active',
        'verified': 'verified',
        'scan_type': 'scan_type',
        'endpoint_to_add': 'endpoint_to_add',
        'file': 'file',
        'test': 'test',
        'push_to_jira': 'push_to_jira'
    }

    def __init__(self, scan_date=None, minimum_severity='Info', active=True, verified=True, scan_type=None, endpoint_to_add=None, file=None, test=None, push_to_jira=False, local_vars_configuration=None):  # noqa: E501
        """ReImportScan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scan_date = None
        self._minimum_severity = None
        self._active = None
        self._verified = None
        self._scan_type = None
        self._endpoint_to_add = None
        self._file = None
        self._test = None
        self._push_to_jira = None
        self.discriminator = None

        self.scan_date = scan_date
        if minimum_severity is not None:
            self.minimum_severity = minimum_severity
        if active is not None:
            self.active = active
        if verified is not None:
            self.verified = verified
        self.scan_type = scan_type
        if endpoint_to_add is not None:
            self.endpoint_to_add = endpoint_to_add
        if file is not None:
            self.file = file
        self.test = test
        if push_to_jira is not None:
            self.push_to_jira = push_to_jira

    @property
    def scan_date(self):
        """Gets the scan_date of this ReImportScan.  # noqa: E501


        :return: The scan_date of this ReImportScan.  # noqa: E501
        :rtype: date
        """
        return self._scan_date

    @scan_date.setter
    def scan_date(self, scan_date):
        """Sets the scan_date of this ReImportScan.


        :param scan_date: The scan_date of this ReImportScan.  # noqa: E501
        :type scan_date: date
        """
        if self.local_vars_configuration.client_side_validation and scan_date is None:  # noqa: E501
            raise ValueError("Invalid value for `scan_date`, must not be `None`")  # noqa: E501

        self._scan_date = scan_date

    @property
    def minimum_severity(self):
        """Gets the minimum_severity of this ReImportScan.  # noqa: E501


        :return: The minimum_severity of this ReImportScan.  # noqa: E501
        :rtype: str
        """
        return self._minimum_severity

    @minimum_severity.setter
    def minimum_severity(self, minimum_severity):
        """Sets the minimum_severity of this ReImportScan.


        :param minimum_severity: The minimum_severity of this ReImportScan.  # noqa: E501
        :type minimum_severity: str
        """
        allowed_values = ["Info", "Low", "Medium", "High", "Critical"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and minimum_severity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `minimum_severity` ({0}), must be one of {1}"  # noqa: E501
                .format(minimum_severity, allowed_values)
            )

        self._minimum_severity = minimum_severity

    @property
    def active(self):
        """Gets the active of this ReImportScan.  # noqa: E501


        :return: The active of this ReImportScan.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ReImportScan.


        :param active: The active of this ReImportScan.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def verified(self):
        """Gets the verified of this ReImportScan.  # noqa: E501


        :return: The verified of this ReImportScan.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this ReImportScan.


        :param verified: The verified of this ReImportScan.  # noqa: E501
        :type verified: bool
        """

        self._verified = verified

    @property
    def scan_type(self):
        """Gets the scan_type of this ReImportScan.  # noqa: E501


        :return: The scan_type of this ReImportScan.  # noqa: E501
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this ReImportScan.


        :param scan_type: The scan_type of this ReImportScan.  # noqa: E501
        :type scan_type: str
        """
        if self.local_vars_configuration.client_side_validation and scan_type is None:  # noqa: E501
            raise ValueError("Invalid value for `scan_type`, must not be `None`")  # noqa: E501
        allowed_values = ["", "Netsparker Scan", "Burp Scan", "Nessus Scan", "Nmap Scan", "Nexpose Scan", "AppSpider Scan", "Veracode Scan", "Checkmarx Scan", "Checkmarx Scan detailed", "Crashtest Security JSON File", "Crashtest Security XML File", "ZAP Scan", "Arachni Scan", "VCG Scan", "Dependency Check Scan", "Dependency Track Finding Packaging Format (FPF) Export", "Retire.js Scan", "Node Security Platform Scan", "NPM Audit Scan", "Qualys Scan", "Qualys Infrastructure Scan (WebGUI XML)", "Qualys Webapp Scan", "OpenVAS CSV", "Snyk Scan", "Generic Findings Import", "Trustwave Scan (CSV)", "SKF Scan", "Clair Klar Scan", "Bandit Scan", "ESLint Scan", "SSL Labs Scan", "Acunetix Scan", "Fortify Scan", "Gosec Scanner", "SonarQube Scan", "SonarQube Scan detailed", "SonarQube API Import", "MobSF Scan", "Trufflehog Scan", "Nikto Scan", "Clair Scan", "Brakeman Scan", "SpotBugs Scan", "AWS Scout2 Scan", "AWS Prowler Scan", "IBM AppScan DAST", "PHP Security Audit v2", "PHP Symfony Security Check", "Safety Scan", "DawnScanner Scan", "Anchore Engine Scan", "Bundler-Audit Scan", "Twistlock Image Scan", "Kiuwan Scan", "Blackduck Hub Scan", "Blackduck Component Risk", "Openscap Vulnerability Scan", "Wapiti Scan", "Immuniweb Scan", "Sonatype Application Scan", "Cobalt.io Scan", "Mozilla Observatory Scan", "Whitesource Scan", "Contrast Scan", "Microfocus Webinspect Scan", "Wpscan", "Sslscan", "JFrog Xray Scan", "Sslyze Scan", "Testssl Scan", "Hadolint Dockerfile check", "Aqua Scan", "HackerOne Cases", "Xanitizer Scan", "Outpost24 Scan", "Burp Enterprise Scan", "DSOP Scan", "Trivy Scan", "Anchore Enterprise Policy Check", "Gitleaks Scan", "Choctaw Hog Scan", "Harbor Vulnerability Scan", "Yarn Audit Scan", "BugCrowd Scan", "GitLab SAST Report", "HuskyCI Report", "CCVS Report"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and scan_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `scan_type` ({0}), must be one of {1}"  # noqa: E501
                .format(scan_type, allowed_values)
            )

        self._scan_type = scan_type

    @property
    def endpoint_to_add(self):
        """Gets the endpoint_to_add of this ReImportScan.  # noqa: E501


        :return: The endpoint_to_add of this ReImportScan.  # noqa: E501
        :rtype: int
        """
        return self._endpoint_to_add

    @endpoint_to_add.setter
    def endpoint_to_add(self, endpoint_to_add):
        """Sets the endpoint_to_add of this ReImportScan.


        :param endpoint_to_add: The endpoint_to_add of this ReImportScan.  # noqa: E501
        :type endpoint_to_add: int
        """

        self._endpoint_to_add = endpoint_to_add

    @property
    def file(self):
        """Gets the file of this ReImportScan.  # noqa: E501


        :return: The file of this ReImportScan.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ReImportScan.


        :param file: The file of this ReImportScan.  # noqa: E501
        :type file: str
        """

        self._file = file

    @property
    def test(self):
        """Gets the test of this ReImportScan.  # noqa: E501


        :return: The test of this ReImportScan.  # noqa: E501
        :rtype: int
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this ReImportScan.


        :param test: The test of this ReImportScan.  # noqa: E501
        :type test: int
        """
        if self.local_vars_configuration.client_side_validation and test is None:  # noqa: E501
            raise ValueError("Invalid value for `test`, must not be `None`")  # noqa: E501

        self._test = test

    @property
    def push_to_jira(self):
        """Gets the push_to_jira of this ReImportScan.  # noqa: E501


        :return: The push_to_jira of this ReImportScan.  # noqa: E501
        :rtype: bool
        """
        return self._push_to_jira

    @push_to_jira.setter
    def push_to_jira(self, push_to_jira):
        """Sets the push_to_jira of this ReImportScan.


        :param push_to_jira: The push_to_jira of this ReImportScan.  # noqa: E501
        :type push_to_jira: bool
        """

        self._push_to_jira = push_to_jira

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReImportScan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReImportScan):
            return True

        return self.to_dict() != other.to_dict()