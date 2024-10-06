#!/usr/bin/python3
"""
UTF8 validation
"""

def is_utf8(data):
    """Checks whether a sequence of integers represents valid UTF-8 encoding."""
    continuation_bytes = 0

    for byte in data:
        if 128 <= byte <= 191:
            if continuation_bytes == 0:
                return False
            continuation_bytes -= 1
        else:
            if continuation_bytes != 0:
                return False
            if byte < 128:
                continue
            elif byte < 224:
                continuation_bytes = 1
            elif byte < 240:
                continuation_bytes = 2
            elif byte < 248:
                continuation_bytes = 3
            else:
                return False
    return continuation_bytes == 0
