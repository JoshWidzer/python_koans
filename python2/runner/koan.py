#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re


# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

def assert_match(pattern, string, msg=None):
    """
    Throw an exception if the regular expresson pattern is matched
    """
    # Not part of unittest, but convenient for some koans tests
    m = re.search(pattern, string)
    if not m or not m.group(0):
        raise Exception((msg or '{0!r} does not match {1!r}'.format(pattern, string)))

def assert_no_match(pattern, string, msg=None):
    """
    Throw an exception if the regular expresson pattern is not matched
    """
    m = re.search(pattern, string)
    if m and m.group(0):
        raise Exception ((msg or '{0!r} matches {1!r}'.format(pattern, string)))

__all__ = ["__", "___", "____", "_____", "assert_match","assert_no_match"]

__ = "-=> FILL ME IN! <=-"


class ___(Exception):
    pass


____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


