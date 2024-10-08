##############################################################################
#
# Copyright (c) 2001, 2002 Zope Foundation and Contributors.
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
"""General exceptions that wish they were standard exceptions

These exceptions are so general purpose that they don't belong in Zope
application-specific packages.
"""

from zope.exceptions.exceptionformatter import extract_stack
from zope.exceptions.exceptionformatter import format_exception
from zope.exceptions.exceptionformatter import print_exception
from zope.exceptions.interfaces import DuplicationError
from zope.exceptions.interfaces import IDuplicationError
from zope.exceptions.interfaces import IUserError
from zope.exceptions.interfaces import UserError


__all__ = [
    'DuplicationError',
    'IDuplicationError',
    'UserError',
    'IUserError',
    'format_exception',
    'print_exception',
    'extract_stack',
]

# avoid dependency on zope.security:
try:
    import zope.security  # noqa: suppress unused import warning from flake8
except ModuleNotFoundError as v:  # pragma: no cover
    # "ModuleNotFoundError: No module named security"
    if 'security' not in str(v):
        raise
else:  # pragma: no cover
    from zope.security.interfaces import Forbidden
    from zope.security.interfaces import ForbiddenAttribute
    from zope.security.interfaces import IForbidden
    from zope.security.interfaces import IForbiddenAttribute
    from zope.security.interfaces import IUnauthorized
    from zope.security.interfaces import Unauthorized
    __all__ += [
        'IUnauthorized',
        'Unauthorized',
        'IForbidden',
        'IForbiddenAttribute',
        'Forbidden',
        'ForbiddenAttribute',
    ]
