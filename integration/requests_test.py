import os
import sys

sys.path.append(os.path.dirname(__file__) + "/../extra")
from test_helper import create_virtenv, run_test

ENV_NAME = "requests_test_env_" + os.path.basename(sys.executable)
REQUESTS_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../lib/requests"
PYTHON_EXE = os.path.abspath(os.path.join(ENV_NAME, "bin", "python"))

packages = ["pytest==2.3.4"]
create_virtenv(ENV_NAME, packages, force_create = True)

expected = [{"ran": 143}]
print "Running test_requests.py..."
run_test([PYTHON_EXE, "test_requests.py"], cwd=REQUESTS_DIR, expected=expected)
