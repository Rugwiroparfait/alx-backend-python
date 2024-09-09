#!/usr/bin/env python3
"""Unit tests for GithubOrgClient in client module."""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
        result = client.org

        # Assert: verify get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        # Assert: check that the result matches the mocked return value
        self.assertEqual(result, {"login": org_name})

    @patch.object(GithubOrgClient, 'org', new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url returns correct URL."""
        # Arrange: Mock the 'org' property to return a specific dictionary
        mock_org.return_value = {
            "login": "google",
            "repos_url": "https://api.github.com/orgs/google/repos"
            }

        # Act: Create an instance of /
        # GithubOrgClient and access _public_repos_url
        client = GithubOrgClient("google")
        result = client._public_repos_url

        # Assert: Check that _public_repos_url returns the expected repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns the correct repo list."""
        # Arrange: Set up mock return value for get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Mock _public_repos_url to return a specific URL
        with patch.object(
            GithubOrgClient, '_public_repos_url',
                return_value="https://api.github.com/orgs/google/repos"):
            # Act: Create an instance of GithubOrgClient and call public_repos
            client = GithubOrgClient("google")
            repos = client.public_repos()

            # Assert: Check that the list of repos is correct
            self.assertEqual(repos, ["repo1", "repo2", "repo3"])

            # Assert: Check that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos"
                )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Case with no license in repo
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license method."""
        client = GithubOrgClient("test_org")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient."""

    @classmethod
    def setUpClass(cls):
        """Set up the class by patching requests.get."""
        cls.get_patcher = patch('requests.get')

        # Start the patcher
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect for requests.get().json() based on URL
        def side_effect(url):
            org_url = f"https://api.github.com/orgs/{cls.org_payload['login']}"
            repos_url = cls.org_payload['repos_url']

            if url == org_url:
                return Mock(json=lambda: cls.org_payload)
            elif url == repos_url:
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: None)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient(self.org_payload['login'])
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos method filtering by license."""
        client = GithubOrgClient(self.org_payload['login'])
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)
        
        # Assert the returned repos with apache2.0 licences match the fixture
        self.assertEqual(repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
