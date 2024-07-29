#!/usr/bin/env python3
"""Test_utils."""
import unittest
from parameterized import parameterized
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    """Test class."""

    @parameterized.expand([
        (nested_map={"a": 1}, path=("a",), 1),
        (nested_map={"a": {"b": 2}}, path=("a",), {"b": 2}),
        (nested_map={"a": {"b": 2}}, path=("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path):
        """Test that the method returns what is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
