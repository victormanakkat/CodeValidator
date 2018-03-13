
import json
import unittest

# Nothing rocket science - import the class 'BaseTestCase' defined in 'project/tests/base'
from project.tests.base import BaseTestCase

class TestUserService(BaseTestCase):
    """Tests for the Users Service."""

    def test_users(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/users/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertEqual('pong', data['message'])
        # assertIn checks if the strings in present inside the sentence, whereas assertEqual checks absolute equality
        self.assertIn('success', data['status'])


if __name__ == '__main__':
    unittest.main()