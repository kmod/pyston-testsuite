import os
import subprocess
import sys

sys.path.append(os.path.dirname(__file__) + "/../extra")
from test_helper import create_virtenv, run_test

ENV_NAME = "pytest_test_env_" + os.path.basename(sys.executable)
PYTEST_EXE = os.path.abspath(os.path.join(ENV_NAME, "bin", "py.test"))

packages = ["pytest==2.3.4"]
create_virtenv(ENV_NAME, packages, force_create = True)

print "Running pytest..."
subprocess.check_call([PYTEST_EXE, "pytest_test_target.py"], cwd=os.path.dirname(__file__))
