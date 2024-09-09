#!/usr/bin/env python3
"""Unit tests for utils functions."""
import unittest
from unittest.mock import patch, Mock
from client import GithubOrgClient
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the expected value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),  # The key 'a' does not exist
        ({"a": 1}, ("a", "b"), "'b'"),  # The key 'b' does not exist
    ])
    def test_access_nested_map_exception(
        self, nested_map, path, expected_exception
    ):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), expected_exception)


class TestGetJson(unittest.TestCase):
    """Test the get_json function in utils."""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test get_json returns expected result and was called correctly."""
        # Define test cases
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            # Create a Mock object with a json method that returns test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function being tested
            result = get_json(test_url)

            # Check that requests.get was called with the correct URL
            mock_get.assert_called_once_with(test_url)

            # Check if output is as expected
            self.assertEqual(result, test_payload)

            # Reset mock for the next test_payload
            mock_get.reset_mock()


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    class TestClass:
        """A class to test the memoize decorator."""

        def a_method(self):
            """Method that returns 42."""
            return 42

        @memoize
        def a_property(self):
            """A memoized property that calls a_method."""
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """Test that memoize caches the result and calls a_method only once."""
        obj = self.TestClass()

        # Call a_property twice
        self.assertEqual(obj.a_property, 42)
        self.assertEqual(obj.a_property, 42)

        # Ensure a_method was called only once
        mock_method.assert_called_once()


class TestGithubOrg(unittest.TestCase):
    """Test cases for GithubOrgClient."""
    
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value. """
        # Arrange: mock the return value for get_json
        mock_get_json.return_value = {"login": org_name}
        
        
        # Act: create an instance of GithubOrgClient /
        # and call the org method
        client = GithubOrgClient(org_name)
        result = client.org
        
        # Assert: verify get_json was called once with the /
        # correct URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        
        # Assert: check that the result matches the mocked/
        # return value
        self.assertEqual(result, {"login": org_name})

if __name__ == "__main__":
    unittest.main()
