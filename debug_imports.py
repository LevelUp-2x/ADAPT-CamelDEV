import sys
import os

print("Python version:", sys.version)
print("Current working directory:", os.getcwd())

try:
    from langchain_integration import basic_agent
    print("Successfully imported basic_agent")
except ImportError as e:
    print("Failed to import basic_agent:", str(e))

try:
    import ray
    print("Successfully imported ray")
except ImportError as e:
    print("Failed to import ray:", str(e))

try:
    import unittest
    print("Successfully imported unittest")
except ImportError as e:
    print("Failed to import unittest:", str(e))

print("Python path:")
for path in sys.path:
    print(path)