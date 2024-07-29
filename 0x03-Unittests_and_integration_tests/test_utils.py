#!/usr/bin/env python3
"""Test_utils."""
import unittest
import parameterized
access_nested_map = __import__('utils').access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Test class."""

    @parameterized.expand([
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b":2}}, path=("a", "b")
        ])
    def test_access_nested_map(self, nested_map, path):
        """Test that the method returns what is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), nested_map)
