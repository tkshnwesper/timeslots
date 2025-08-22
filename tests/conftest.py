import pytest
from datetime import datetime


@pytest.fixture
def now():
    return datetime.now()
