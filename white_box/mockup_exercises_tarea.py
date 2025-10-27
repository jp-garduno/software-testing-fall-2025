# -*- coding: utf-8 -*-
"""Unit tests for mockup exercises functions."""

import subprocess
import unittest
from unittest.mock import Mock, mock_open, patch

import requests  # pylint: disable=import-error

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFetchDataFromApiAdditional(unittest.TestCase):
    """Additional tests for fetch_data_from_api function"""

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_with_list_response(self, mock_get):
        """Test API returning a list of data"""
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
        ]

        result = fetch_data_from_api("https://exampleapi.com/items")

        self.assertEqual(
            result, [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        )
        mock_get.assert_called_once_with("https://exampleapi.com/items", timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_requests_exception(self, mock_get):
        """Test when requests.get raises an exception"""
        mock_get.side_effect = requests.RequestException("Connection error")

        with self.assertRaises(requests.RequestException):
            fetch_data_from_api("https://exampleapi.com/data")

        mock_get.assert_called_once_with("https://exampleapi.com/data", timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_json_decode_error(self, mock_get):
        """Test when response.json() raises a JSON decode error."""
        mock_get.return_value.json.side_effect = ValueError("Invalid JSON")

        with self.assertRaises(ValueError):
            fetch_data_from_api("https://exampleapi.com/data")

        mock_get.assert_called_once_with("https://exampleapi.com/data", timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_timeout(self, mock_get):
        """Test when request times out."""
        mock_get.side_effect = requests.Timeout("Request timed out")

        with self.assertRaises(requests.Timeout):
            fetch_data_from_api("https://exampleapi.com/data")

        mock_get.assert_called_once_with("https://exampleapi.com/data", timeout=10)

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_empty_response(self, mock_get):
        """Test API returning empty data."""
        mock_get.return_value.json.return_value = {}

        result = fetch_data_from_api("https://exampleapi.com/empty")

        self.assertEqual(result, {})
        mock_get.assert_called_once_with("https://exampleapi.com/empty", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """Tests for read_data_from_file function"""

    @patch("builtins.open", new_callable=mock_open, read_data="Hello world!")
    def test_read_data_from_file_success(self, mock_file):
        """Test successfully reading data from a file"""
        result = read_data_from_file("test.txt")

        self.assertEqual(result, "Hello world!")
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_data_from_file_empty_file(self, mock_file):
        """Test reading from an empty file"""
        result = read_data_from_file("test.txt")

        self.assertEqual(result, "")
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_not_found(self, mock_file):
        """Test when file is not found"""
        mock_file.side_effect = FileNotFoundError("File not found")

        with self.assertRaises(FileNotFoundError):
            read_data_from_file("test.txt")

        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="Line 1\nLine 2\nLine 3")
    def test_read_data_from_file_multiline(self, mock_file):
        """Test reading multiline data from a file"""
        result = read_data_from_file("test.txt")

        self.assertEqual(result, "Line 1\nLine 2\nLine 3")
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_permission_error(self, mock_file):
        """Test when permission is denied"""
        mock_file.side_effect = PermissionError("Permission denied")

        with self.assertRaises(PermissionError):
            read_data_from_file("restricted.txt")

        mock_file.assert_called_once_with("restricted.txt", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="Special chars: áéíóú ñ")
    def test_read_data_from_file_utf8_content(self, mock_file):
        """Test reading UTF-8 encoded content"""
        result = read_data_from_file("utf8.txt")

        self.assertEqual(result, "Special chars: áéíóú ñ")
        mock_file.assert_called_once_with("utf8.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_io_error(self, mock_file):
        """Test when an IO error occurs during reading"""
        mock_file.return_value.__enter__.return_value.read.side_effect = IOError(
            "IO Error"
        )

        with self.assertRaises(IOError):
            read_data_from_file("error.txt")

        mock_file.assert_called_once_with("error.txt", encoding="utf-8")


class TestExecuteCommand(unittest.TestCase):
    """Tests for execute_command function"""

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """Test successful command execution"""
        mock_result = Mock()
        mock_result.stdout = "Command executed successfully"
        mock_run.return_value = mock_result

        result = execute_command(["echo", "hello"])

        self.assertEqual(result, "Command executed successfully")
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_empty_output(self, mock_run):
        """Test command with empty stdout"""
        mock_result = Mock()
        mock_result.stdout = ""
        mock_run.return_value = mock_result

        result = execute_command(["ls", "/empty"])

        self.assertEqual(result, "")
        mock_run.assert_called_once_with(
            ["ls", "/empty"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_multiline_output(self, mock_run):
        """Test command with multiline output"""
        mock_result = Mock()
        mock_result.stdout = "Line 1\nLine 2\nLine 3\n"
        mock_run.return_value = mock_result

        result = execute_command(["cat", "file.txt"])

        self.assertEqual(result, "Line 1\nLine 2\nLine 3\n")
        mock_run.assert_called_once_with(
            ["cat", "file.txt"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_called_process_error(self, mock_run):
        """Test when subprocess.run raises CalledProcessError"""
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd=["invalid", "command"]
        )

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["invalid", "command"])

        mock_run.assert_called_once_with(
            ["invalid", "command"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_file_not_found_error(self, mock_run):
        """Test when command is not found"""
        mock_run.side_effect = FileNotFoundError("Command not found")

        with self.assertRaises(FileNotFoundError):
            execute_command(["nonexistent_command"])

        mock_run.assert_called_once_with(
            ["nonexistent_command"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_timeout_error(self, mock_run):
        """Test when command times out"""
        mock_run.side_effect = subprocess.TimeoutExpired(cmd=["sleep", "10"], timeout=5)

        with self.assertRaises(subprocess.TimeoutExpired):
            execute_command(["sleep", "10"])

        mock_run.assert_called_once_with(
            ["sleep", "10"], capture_output=True, check=False, text=True
        )


class TestPerformActionBasedOnTime(unittest.TestCase):
    """Tests for perform_action_based_on_time function"""

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_less_than_10(self, mock_time):
        """Test when current time is less than 10"""
        mock_time.return_value = 5.0

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_equal_to_10(self, mock_time):
        """Test when current time equals 10"""
        mock_time.return_value = 10.0

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_greater_than_10(self, mock_time):
        """Test when current time is greater than 10"""
        mock_time.return_value = 15

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_zero(self, mock_time):
        """Test when current time is zero"""
        mock_time.return_value = 0

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_boundary_just_under_10(self, mock_time):
        """Test boundary case just under 10"""
        mock_time.return_value = 9.99

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_boundary_just_over_10(self, mock_time):
        """Test boundary case just over 10"""
        mock_time.return_value = 10.01

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action B")
        mock_time.assert_called_once()

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_time_negative(self, mock_time):
        """Test when current time is negative"""
        mock_time.return_value = -5

        result = perform_action_based_on_time()

        self.assertEqual(result, "Action A")
        mock_time.assert_called_once()


if __name__ == "__main__":
    unittest.main()
