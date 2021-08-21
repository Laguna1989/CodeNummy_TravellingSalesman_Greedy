import pytest
from math import sqrt
from src.city import compute_distance, City


@pytest.mark.parametrize("ax, ay, bx, by, expected_distance", [(0.0, 0.0, 1.0, 0.0, 1.0),
                                                               (0.0, 0.0, 0.0, 1.0, 1.0),
                                                               (1.0, 1.0, 0.5, 1.0, 0.5),
                                                               (1.0, 1.0, 1.0, 0.5, 0.5),
                                                               (0.0, 0.0, 1.0, 1.0, sqrt(2.0))])
def test_distance_calculation_returns_correct_value(ax, ay, bx, by, expected_distance):
    cityA = City(ax, ay)
    cityB = City(bx, by)

    distance = compute_distance(cityA, cityB)

    assert distance == pytest.approx(expected_distance)
