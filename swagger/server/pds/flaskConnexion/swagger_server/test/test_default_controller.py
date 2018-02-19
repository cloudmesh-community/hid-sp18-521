# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.provider import Provider  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_provider(self):
        """Test case for create_provider

        
        """
        provider = Provider()
        response = self.client.open(
            '/PDS/provider',
            method='POST',
            data=json.dumps(provider),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_provider(self):
        """Test case for delete_provider

        
        """
        response = self.client.open(
            '/PDS/provider/{npi}'.format(npi=56),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_provider(self):
        """Test case for get_provider

        
        """
        response = self.client.open(
            '/PDS/provider/{npi}'.format(npi=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_providers(self):
        """Test case for get_providers

        
        """
        response = self.client.open(
            '/PDS/provider',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_provider(self):
        """Test case for update_provider

        
        """
        response = self.client.open(
            '/PDS/provider/{npi}'.format(npi=56),
            method='PATCH',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
