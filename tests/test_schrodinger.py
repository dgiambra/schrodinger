#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_schrodinger
----------------------------------

Tests for `schrodinger` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from schrodinger import schrodinger
from schrodinger import cli
import numpy as np



class TestSchrodinger(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_different_series(self):
        self.assertTrue(schrodinger.schrodinger(1, 1 , 9 , np.sin, "f", -1,1)[0].all()==(schrodinger.schrodinger(1, 1 , 9 , np.sin, "f", -1,1))[0].all())
