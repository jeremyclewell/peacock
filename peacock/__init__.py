#!/usr/bin/env python -u
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018, Jeremy Clewell <jeremy.clewell@gmail.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import print_function

import fileinput
import logging
import os
import sys
import watchdog

from peacock.log import log
from peacock.output import monitor

VERSION = '0.0.1'

__all__ = ['usage', 'main']
__doc__ = """

USAGE

Options:
---------

-h   this help
-d   enable debug logging

Examples:
---------
peacock 
peacock /var/log
"""
 
def usage():
    return __doc__

def main():
    log.info('version: ' + VERSION)

    if len(sys.argv) > 1:
        if '-h' in sys.argv:
            log.info(usage())
            quit()
        if '-d' in sys.argv:
            log.setLevel(logging.DEBUG)
            sys.argv.pop(sys.argv.index('-d'))

    log.debug("Processed args: %s" % sys.argv)

    #knsdkfjds
    monitor()
