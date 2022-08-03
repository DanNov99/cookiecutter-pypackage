from kata_green_valley.green_valley import make_valley
import pytest


@pytest.mark.parametrize(
    "amount, result",
    [
        (["1", 2, 3], -1),
        ([], -1),
        (25, -1),
        ([79, 35, 54, 19, 35, 25], [79, 35, 25, 19, 35, 54]),
        ([67, 93, 100, -16, 65, 97, 92], [100, 93, 67, -16, 65, 92, 97]),
        ([14, 14, 14, 14, 7, 14], [14, 14, 14, 7, 14, 14]),
        ([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1], [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]),
    ],
)
def test_make_valley(amount, result):
    assert make_valley(amount) == result
