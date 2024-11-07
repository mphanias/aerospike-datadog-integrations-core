# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from functools import wraps

import requests


def handle_error(f):
    @wraps(f)
    def wrapper(check, *args, **kwargs):
        try:
            result = f(check, *args, **kwargs)
            return result
        except requests.exceptions.RequestException as e:
            check.log.info(
                "Encountered a RequestException in '%s' [%s]: %s",
                f.__name__,
                type(e),
                e,
            )

    return wrapper