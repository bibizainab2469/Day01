"""
Inside it, one file hello.py that does exactly:
prints sys.version
prints platform.processor()
creates a list a = list(range(10**6)) and prints its memory size in MB (use sys.getsizeof)
"""

import sys
import platform

print(f"Sys.Version: {sys.version}")
print(f"Platform.Processor: {platform.processor()}")
a = list(range(10**6))

print(f"the size: {sys.getsizeof(a)/(1024**2):.2f} MB")