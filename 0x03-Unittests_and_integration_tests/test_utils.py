#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map function."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns the expected payload."""
        # Creating a mock response object with
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Set the mock   get() to return the mock response
        mock_get.return_value = mock_response

        # Call the function with the test_url
        result = get_json(test_url)

        # Call the function with the test_url
        mock_get.assert_called_once_with(test_url)

        # Check that the returned value is the expected payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
