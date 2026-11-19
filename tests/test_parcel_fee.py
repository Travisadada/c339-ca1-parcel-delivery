
import pytest
from src.parcel_fee import delivery_fee


@pytest.mark.parametrize("weight, expected", [
    (1, 500),        # lower boundary, band 1
    (500, 500),      # mid band 1
    (999, 500),      # just below band edge
    (1000, 500),     # upper boundary, band 1 (inclusive)
    (1001, 1000),    # lower boundary, band 2
    (10000, 1000),   # mid band 2
    (19999, 1000),   # just below max
    (20000, 1000),   # upper boundary, band 2
])
def test_delivery_fee_valid_weights(weight, expected):
    assert delivery_fee(weight) == expected


def test_delivery_fee_returns_int():
    assert type(delivery_fee(500)) is int


@pytest.mark.parametrize("weight", [0, -1, -1000, 20001, 100000])
def test_delivery_fee_out_of_range_raises_valueerror(weight):
    with pytest.raises(ValueError):
        delivery_fee(weight)


@pytest.mark.parametrize("weight", ["500", 500.0, 1.5, None, True, False, [500]])
def test_delivery_fee_invalid_type_raises_typeerror(weight):
    with pytest.raises(TypeError):
        delivery_fee(weight)
