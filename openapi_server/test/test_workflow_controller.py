# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestWorkflowController(BaseTestCase):
    """WorkflowController integration test stubs"""

    def test_cancel_submission(self):
        """Test case for cancel_submission

        Creates cancel request
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/cancel'.format(submission_id=56),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission_log(self):
        """Test case for get_submission_log

        Gets submission log
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/logs'.format(submission_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission_run(self):
        """Test case for get_submission_run

        Gets submission run
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/schedule'.format(submission_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_queue_queue_id_logs_get(self):
        """Test case for queue_queue_id_logs_get

        Monitor queue
        """
        headers = { 
        }
        response = self.client.open(
            '/queue/{queue_id}/logs'.format(queue_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_submission(self):
        """Test case for run_submission

        Schedules a submission workflow
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/schedule'.format(submission_id=56),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submission_submission_id_output_get(self):
        """Test case for submission_submission_id_output_get

        Get submission workflow output
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/output'.format(submission_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submission_submission_id_restart_post(self):
        """Test case for submission_submission_id_restart_post

        Restart submissions
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/restart'.format(submission_id=56),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submission_submission_id_status_get(self):
        """Test case for submission_submission_id_status_get

        Gets submission status
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/status'.format(submission_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submission_submission_id_status_put(self):
        """Test case for submission_submission_id_status_put

        Update submission status
        """
        headers = { 
        }
        response = self.client.open(
            '/submission/{submission_id}/status'.format(submission_id=56),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
