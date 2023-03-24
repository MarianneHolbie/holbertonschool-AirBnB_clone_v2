#!/usr/bin/python3
""" Unittest for class BaseModel"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ Unittest for class base_model"""

    def __init__(self, *args, **kwargs):
        """ Tests initialization of model """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ test setUp """
        pass

    def tearDown(self):
        """ Test teardow method of test class"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ test default """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test kwargs """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """  Test type int of kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_str(self):
        """  Test type string"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_save(self):
        """ Test save """
        model = BaseModel()
        before = model.updated_at
        model.save()
        after = model.updated_at
        self.assertLess(before, after)

    def test_to_dict(self):
        """  Test dic """
        i = self.value()
        y = i.to_dict()
        self.assertEqual(i.to_dict(), y)

    def test_kwargs_none(self):
        """  test if no kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ test id type """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ test created attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

if __name__ == "__main__":
    unittest.main()
