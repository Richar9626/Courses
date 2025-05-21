import square
import pytest
#for similar inputs and expected outputs we can use a parametrize decorator
@pytest.mark.parametrize(
        ("input_n", "expected"),
        (
            (5, 25),
            (3., 9.),
        )
)
def test_square(input_n, expected):
    assert square.square(5) == 25

# def test_square_float():
#     assert square.square(3.) == 9.

#Test with classes
class TestSquare:
    def test_square(self):
        assert square.square(3) == 9