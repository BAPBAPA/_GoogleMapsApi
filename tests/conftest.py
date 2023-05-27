import pytest
from api_methods.methods import *
from src.assistants_function import *


@pytest.fixture
def api_instance():

    return FullLifeCycle()


@pytest.fixture
def json_comparison():

    return json_parse
