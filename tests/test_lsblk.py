# Copyright (c) 2018, 2021 Oracle and/or its affiliates. All rights reserved.
# Licensed under the Universal Permissive License v 1.0 as shown
# at http://oss.oracle.com/licenses/upl.

import os
import unittest

import oci_utils.lsblk
from tools.oci_test_case import OciTestCase

os.environ['LC_ALL'] = 'en_US.UTF8'


class TestLsBlk(OciTestCase):
    """ Test the lsblk module.
    """

    def test_list_root(self):
        """
        Tests lsblk.list give us the root filesystem.

        Returns
        -------
            No return value.
        """
        dev_list = oci_utils.lsblk.list()
        self.assertIsNotNone(dev_list, 'None returned as device list')
        self.assertTrue(len(dev_list), 'empty device list returned ')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLsBlk)
    unittest.TextTestRunner().run(suite)
