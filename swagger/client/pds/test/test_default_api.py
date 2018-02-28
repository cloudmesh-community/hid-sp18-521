# coding: utf-8

"""
    Provider Data System

    An API that interacts with a SQL database backend of medical provider data system.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_provider(self):
        """Test case for create_provider

        """
        pass

    def test_delete_provider(self):
        """Test case for delete_provider

        """
        pass

    def test_get_provider(self):
        """Test case for get_provider

        """
        pass

    def test_get_providers(self):
        """Test case for get_providers

        """
        pass

    def test_update_provider(self):
        """Test case for update_provider

        """
        pass


if __name__ == '__main__':
    unittest.main()
