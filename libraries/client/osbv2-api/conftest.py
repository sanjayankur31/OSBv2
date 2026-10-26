import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OSBV2_API = os.path.join(ROOT, "osbv2_api")
if OSBV2_API not in sys.path:
    sys.path.insert(0, OSBV2_API)
