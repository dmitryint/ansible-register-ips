#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import unittest


def filter_ints(_ifacelist, _regex_str):
    """
    filter list of interfaces based on a regex string
    """
    _regex = re.compile(_regex_str)
    return [iface for iface in _ifacelist
            if _regex.match(iface)]


class FilterModule(object):
    """ Ansible custom filter plugin """

    def filters(self):
        return {
            'filter_ints': filter_ints
        }


class TestFilterInt(unittest.TestCase):
    """
    Test case for this filter plugin. Run python script to run test
    e.g python filter_ints.py
    """
    def test_filter_ints(self):
        self.assertEqual(filter_ints(
            ['eth1', 'lo', 'em0'], 'eth|em'), ['eth1', 'em0'])


if __name__ == '__main__':
    unittest.main()
