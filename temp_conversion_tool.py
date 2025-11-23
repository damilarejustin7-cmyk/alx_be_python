"""
Root shim for temperature conversion tool.

Some checkers run from the repository root and expect a module
named `temp_conversion_tool`. The real implementation lives in
`fns_and_dsa/temp_conversion_tool.py`. This shim re-exports the
functions so imports like `import temp_conversion_tool` succeed.
"""
from fns_and_dsa.temp_conversion_tool import (
    convert_to_celsius,
    convert_to_fahrenheit,
    main,
)

__all__ = ["convert_to_celsius", "convert_to_fahrenheit", "main"]
