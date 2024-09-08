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
            # Create a Mock object with a json method
            # Returns test_payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function being tested
            result = get_json(test_url)

            # check that requests.get was called with the correct URL
            mock_get.assert_called_once_with(test_url)

            # check if output is as expected
            self.assertEqual(result, test_payload)

            # Reset mock for the next test_payload
            mock_get.reset_mock()


if __name__ == "__main__":
    unittest.main()
