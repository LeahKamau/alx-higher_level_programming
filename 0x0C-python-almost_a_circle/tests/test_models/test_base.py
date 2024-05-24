#!/usr/bin/pyhton3
"""This module contains unittest for class Base"""

import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """Tests for Base class"""

    def test_with_id(self):
        """ Test with id assigned """
        newobj = Base(12)
        self.assertEqual(newobj.id, 12)

    def test_default_id(self):
        """ Test increment if id not assigned """
        newobj1 = Base()
        newobj2 = Base()
        self.assertEqual(newobj1.id, 1)
        self.assertEqual(newobj2.id, 2)
