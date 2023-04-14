# Karpyncho FormData Null Middleware

[![PyPI version](https://badge.fury.io/py/karpyncho-formdata-null-middleware.svg)](https://badge.fury.io/py/karpyncho-formdata-null-middleware)
[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/karpyncho-formdata-null-middleware.svg)](https://pypi.python.org/pypi/karpyncho-formdata-null-middleware/)
[![check](https://github.com/tox-dev/tox-gh/actions/workflows/check.yml/badge.svg)](https://github.com/tox-dev/tox-gh/actions/workflows/check.yml)
[![codecov](https://codecov.io/gh/karpyncho/formdata-null-middleware/branch/main/graph/badge.svg?token=M4IT5AXE88)](https://codecov.io/gh/karpyncho/formdata-null-middleware)


Django middleware to catch "null" string in FormData and transform it to None

# configuration

For using this package you must install it with:

```sh
pip install karpyncho_formdata_null_middleware
```

and then configure the middleware in your django settings

```python

MIDDLEWARE = [
    ...
    'karpyncho.formdata_null_middleware.FormDataNullMiddleware',
    ...
]

```
