
import pytest
import source.Shape as shape
import json

@pytest.fixture
def my_circle():
    return shape.Circle(10)

@pytest.fixture(scope= "module", autouse=True)
def load_data():
    with open (r"C:\Users\tanvi\PycharmProjects\pytestProject\tests\data.json", "r") as f:
        data =json.load(f)
    return data
