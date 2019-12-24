#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pytest

try:
    import goodvibes_hmayes
    BASEPATH = os.path.join(goodvibes_hmayes.__path__[0])
except ImportError:
    here = os.path.dirname(os.path.abspath(__file__))
    BASEPATH = os.path.normpath(os.path.join(here, '..', 'goodvibes'))


def datapath(path):
    return os.path.join(BASEPATH, 'examples', path)
