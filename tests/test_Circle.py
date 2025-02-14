import pytest
import math
import source.Shape as shapes


class TestCircle:

    def test_area(self, my_circle):
        area = my_circle.area()
        assert area == math.pi * my_circle.radius ** 2


