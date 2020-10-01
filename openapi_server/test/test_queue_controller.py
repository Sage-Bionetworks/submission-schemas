# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestQueueController(BaseTestCase):
    """QueueController integration test stubs"""

    def test_queue_post(self):
        """Test case for queue_post

        Create queue
        """
        headers = { 
        }
        response = self.client.open(
            '/queue',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_queue_queue_id_delete(self):
        """Test case for queue_queue_id_delete

        Deletes queue
        """
        headers = { 
        }
        response = self.client.open(
            '/queue/{queue_id}'.format(queue_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_queue_queue_id_get(self):
        """Test case for queue_queue_id_get

        Get Queue
        """
        headers = { 
        }
        response = self.client.open(
            '/queue/{queue_id}'.format(queue_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_queue_queue_id_put(self):
        """Test case for queue_queue_id_put

        Updates queue
        """
        headers = { 
        }
        response = self.client.open(
            '/queue/{queue_id}'.format(queue_id=56),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
