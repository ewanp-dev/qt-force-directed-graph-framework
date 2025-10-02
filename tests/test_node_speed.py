import pytest
from src.widget import FDNodeGraphWidget


@pytest.fixture
def instance() -> FDNodeGraphWidget:
    return FDNodeGraphWidget()
