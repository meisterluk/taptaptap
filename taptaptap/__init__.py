#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    taptaptap
    ~~~~~~~~~

    An object-oriented module handling the Test Anything Protocol (TAP).
    It's capable of handling TAP files in version 13,
    but will possibly accept older version. See the spec [0]_ [1]_.

    **Remarks:**
    * Implemented for python 2.7
    * I always try to assign a comment to a testcase. As such I assume that
      in a source code like::

          not ok
          Traceback (most recent call last):

      the Traceback line is related to the testcase; not the general document.
      The opposite is not required by the specification.

    Requirements to a TAP document:
    1. There is at least one plan (beginning or end of file)
    2. There is at least one test line in TAP output.
    3. All data structures are immutable. As such I am using some copy operations.

    .. [0] https://metacpan.org/pod/release/PETDANCE/Test-Harness-2.64/lib/Test/Harness/TAP.pod#THE-TAP-FORMAT
    .. [1] http://web.archive.org/web/20120730055134/http://testanything.org/wiki/index.php/TAP_specification

    (c) BSD 3-clause
"""

from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals

__author__ = 'Lukas Prokop <admin@lukas-prokop.at>'
__version__ = '1.0.0'
__license__ = '3-clause BSD license'
__docformat__ = 'reStructuredText'

from .impl import YamlData, TapTestcase, TapActualNumbering, TapNumbering
from .impl import TapDocument, TapDocumentIterator, TapDocumentActualIterator
from .impl import TapDocumentFailedIterator, TapDocumentTokenizer
from .impl import TapDocumentValidator, TapDocumentParser, TapContext, validate
from .impl import repr_harness, tapmerge, parse_file, parse_string

from .exc import TapParseError, TapMissingPlan, TapInvalidNumbering, TapBailout

from .api import doc_from_string, doc_from_file, TapWriter, TapCreator
from .api import SimpleTapCreator, UnittestResult, UnittestRunner

from . import proc