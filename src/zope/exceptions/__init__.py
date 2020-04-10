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

from zope.exceptions.interfaces import (  # noqa: F401
    DuplicationError,
    IDuplicationError,
    UserError,
    IUserError,
)

from zope.exceptions.exceptionformatter import (  # noqa: F401
    format_exception,
    print_exception,
    extract_stack,
)

# avoid dependency on zope.security:
try:
    import zope.security  # noqa: F401
except ImportError as v:  # pragma: no cover
    # "ImportError: No module named security"
    if 'security' not in str(v):
        raise
else:  # pragma: no cover
    from zope.security.interfaces import (  # noqa: F401
        IUnauthorized,
        Unauthorized,
        IForbidden,
        IForbiddenAttribute,
        Forbidden,
        ForbiddenAttribute,
    )
