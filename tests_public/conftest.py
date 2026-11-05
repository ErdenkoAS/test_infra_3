"""Фикстуры публичных тестов. Работают и в CI студента (без грейдера), и при проверке грейдером."""
import os
from pathlib import Path

import pytest


@pytest.fixture
def repo_dir() -> Path:
    return Path(os.environ.get("GRADER_REPO_DIR", Path(__file__).resolve().parent.parent))


def pytest_configure(config):
    config.addinivalue_line("markers", "points(n): сколько баллов даёт тест")
