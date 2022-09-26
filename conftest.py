"""Корневое расширение фреймворка pytest."""
import signal
import subprocess
from pathlib import Path

pytest_plugins = []

SIKULI_API_FILE = Path(__file__).parent.joinpath("sikulixapi-2.0.5-win.jar").absolute()
process_api = subprocess.Popen("", shell=True)


def pytest_configure(config):
    """Передварительная настрока до парсинга аргументов."""
    _ = config
    global process_api
    process_api.terminate()
    process_api = subprocess.Popen(f"java -jar {SIKULI_API_FILE} -p", shell=True)
    from sikulix4python.sikulix.sxundotted import reset
    reset()


def pytest_keyboard_interrupt(excinfo):
    """При ручном прерывании тестов."""
    _ = excinfo
    process_api.send_signal(signal.CTRL_C_EVENT)
    process_api.terminate()


def pytest_unconfigure(config):
    """Настройка после завершения тестов."""
    _ = config
    process_api.send_signal(signal.CTRL_C_EVENT)
    process_api.terminate()
