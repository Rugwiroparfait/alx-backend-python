#!/usr/bin/env python3
"""Unit tests for GithubOrgClient in client module."""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange: mock the return value for get_json
        mock_get_json.return_value = {"login": org_name}

        # Act: create an instance of GithubOrgClient and call the org method
        client = GithubOrgClient(org_name)
        result = client.org()

        # Assert: verify get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        # Assert: check that the result matches the mocked return value
        self.assertEqual(result, {"login": org_name})


if __name__ == "__main__":
    unittest.main()
