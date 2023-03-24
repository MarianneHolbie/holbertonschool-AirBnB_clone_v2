#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel


class test_dbstorage(unittest.TestCase):
    """Class for testing db_storage"""
    def test_dbstorage(self):
        """Testing db_storage"""
        self.assertEqual(1, 1)

        
if __name__ == "__main__":
    unittest.main()
