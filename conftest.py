"""Корневое расширение фреймворка pytest."""
import subprocess
from pathlib import Path

pytest_plugins = []

SIKULI_API_FILE = Path(__file__).parent.parent.joinpath("sikulixapi-2.0.5-win.jar").absolute()


def run_sikuli_api():
    proc = subprocess.Popen(f"java -jar {SIKULI_API_FILE} -p", shell=True)
    return proc

process_api = run_sikuli_api()

try:
    from sikulix4python import reset
    reset()
    from sikulix4python.tests.login import test_authorization

    test_example.run_test()
except:
    process_api.terminate()
    raise
else:
    process_api.terminate()
