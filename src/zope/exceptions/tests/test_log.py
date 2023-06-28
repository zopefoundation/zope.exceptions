##############################################################################
#
# Copyright (c) 2012 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""log.Formatter tests.
"""
import unittest


class FormatterTests(unittest.TestCase):

    def _getTargetClass(self):
        from zope.exceptions.log import Formatter
        return Formatter

    def _makeOne(self, *args, **kw):
        return self._getTargetClass()(*args, **kw)

    def test_simple_exception(self):
        import traceback
        tb = DummyTB()
        exc = ValueError('testing')
        fmt = self._makeOne()
        result = fmt.formatException((ValueError, exc, tb))
        lines = result.splitlines()
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines[0], 'Traceback (most recent call last):')
        self.assertEqual(lines[1], '  File "dummy/filename.py", line 14, '
                                   'in dummy_function')
        emsg = traceback.format_exception_only(ValueError, exc)[0]
        self.assertEqual(lines[2], emsg[:-1])  # strip trailing \n from emsg

    def test_unicode_traceback_info(self):
        import traceback
        __traceback_info__ = "Have a Snowman: \u2603"
        tb = DummyTB()
        tb.tb_frame.f_locals['__traceback_info__'] = __traceback_info__
        exc = ValueError('testing')
        fmt = self._makeOne()
        result = fmt.formatException((ValueError, exc, tb))
        self.assertIsInstance(result, str)
        lines = result.splitlines()
        self.assertEqual(len(lines), 4)
        self.assertEqual(lines[0], 'Traceback (most recent call last):')
        self.assertEqual(lines[1], '  File "dummy/filename.py", line 14, '
                                   'in dummy_function')
        expected = '   - __traceback_info__: Have a Snowman: \u2603'

        self.assertEqual(lines[2], expected)

        emsg = traceback.format_exception_only(ValueError, exc)[0]
        self.assertEqual(lines[3], emsg[:-1])  # strip trailing \n from emsg


class DummyTB:
    tb_lineno = 14
    tb_next = None

    def __init__(self):
        self.tb_frame = DummyFrame()


class DummyFrame:
    f_lineno = 137
    f_back = None

    def __init__(self):
        self.f_locals = {}
        self.f_globals = {}
        self.f_code = DummyCode()


class DummyCode:
    co_filename = 'dummy/filename.py'
    co_name = 'dummy_function'
