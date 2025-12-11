from typing import List, Dict, Any, cast
import unittest
from unittest.mock import patch, MagicMock
import urllib.error
from email.message import Message
import json
from github_activity import fetch_github_activity


class TestGithubEvents(unittest.TestCase):

    @patch("github_activity.urllib.request.urlopen")
    def test_successful_fetch(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps([
            {"type": "PushEvent", "repo": {"name": "repo1"}, "created_at": "2025-01-10"}
        ]).encode()
        mock_response.getcode.return_value = 200

        # urlopen() must return a context manager
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = fetch_github_activity("animstephen")
        self.assertIsInstance(result, list)

        events = cast(List[Dict[str, Any]], result)
        self.assertEqual(events[0]["type"], "PushEvent")

    @patch("github_activity.urllib.request.urlopen")
    def test_user_not_found(self, mock_urlopen):
        # Fix: hdrs must be a Message object
        error_headers = Message()
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="", code=404, msg="Not Found", hdrs=error_headers, fp=None
        )

        result = fetch_github_activity("nonexistent")
        result_dict = cast(Dict[str, str], result)
        self.assertEqual(result_dict.get("error"), "User not found")

    def test_empty_username(self):
        with self.assertRaises(ValueError):
            fetch_github_activity("")

    @patch("github_activity.urllib.request.urlopen")
    def test_network_error(self, mock_urlopen):
        mock_urlopen.side_effect = urllib.error.URLError("No connection")

        result = fetch_github_activity("testuser")
        result_dict = cast(Dict[str, str], result)
        self.assertEqual(result_dict.get("error"), "Network connection failed")

    @patch("github_activity.urllib.request.urlopen")
    def test_invalid_json(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b"NOT JSON"
        mock_response.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = fetch_github_activity("testuser")
        result_dict = cast(Dict[str, str], result)
        self.assertEqual(result_dict.get("error"), "Invalid JSON received")

    @patch("github_activity.urllib.request.urlopen")
    def test_unexpected_api_response(self, mock_urlopen):
        mock_response = MagicMock()
        # API returns dict instead of list
        mock_response.read.return_value = json.dumps({"some": "dict"}).encode()
        mock_response.getcode.return_value = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = fetch_github_activity("testuser")
        result_dict = cast(Dict[str, str], result)
        self.assertEqual(result_dict.get("error"), "Unexpected API response")


if __name__ == "__main__":
    unittest.main()
