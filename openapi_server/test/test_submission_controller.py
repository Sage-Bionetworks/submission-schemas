# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestSubmissionController(BaseTestCase):
    """SubmissionController integration test stubs"""

    def test_delete_submission(self):
        """Test case for delete_submission

        Deletes a submission
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}'.format(submission_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission(self):
        """Test case for get_submission

        Gets submission metadata
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}'.format(submission_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission_data(self):
        """Test case for get_submission_data

        Gets submission data
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/data'.format(submission_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submit(self):
        """Test case for submit

        Submits a submission
        """
        headers = { 
        }
        response = self.client.open(
            '/submission',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_submission(self):
        """Test case for update_submission

        Updates a submission
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}'.format(submission_id=56),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
