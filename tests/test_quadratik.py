import pytest

import src.quadratik as q


def test_discriminant_calculation():
    a, b, c = 1, -5, 6
    target_discriminant = 1
    output_discriminant = q.cal_d(a, b, c)
    assert output_discriminant == target_discriminant


@pytest.mark.parametrize(
    "a_test, b_test, c_test, target_disc",
    [
        (1, -5, 6, 1),
        (4, 3, -1, 25),
    ],
)
def test_multiple_abc_disc(a_test, b_test, c_test, target_disc):
    output_discriminant = q.cal_d(a_test, b_test, c_test)
    assert output_discriminant == target_disc


# todo: add tests for q.solve_quad function
