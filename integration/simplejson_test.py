import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../extra")
from test_helper import run_test

ENV_NAME = "simplejson_test_env_" + os.path.basename(sys.executable)
SIMPLEJSON_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../lib/simplejson"
PYTHON_EXE = os.path.abspath(os.path.join(ENV_NAME, "bin", "python"))

expected = [{"ran": 122}]
print "Running tests..."
run_test([sys.executable, "simplejson/tests/__init__.py"], cwd=SIMPLEJSON_DIR, expected=expected)

