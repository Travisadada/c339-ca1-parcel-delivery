
import pytest
from src.parcel_acceptance import is_parcel_accepted


@pytest.mark.parametrize("weight, length", [
    (1, 1),          # both lower boundaries
    (20000, 199),    # max weight, length just below max
    (20000, 200),    # both upper boundaries (inclusive)
    (1, 200),
    (20000, 1),
    (10000, 100),    # typical
])
def test_accepted_parcels(weight, length):
    assert is_parcel_accepted(weight, length) is True


@pytest.mark.parametrize("weight, length", [
    (0, 100),        # zero weight
    (100, 0),        # zero length
    (0, 0),
    (20001, 100),    # weight above limit
    (100, 201),      # length above limit
    (20001, 201),    # both above
])
def test_rejected_parcels_return_false(weight, length):
    assert is_parcel_accepted(weight, length) is False


@pytest.mark.parametrize("weight, length", [
    (-1, 100), (100, -1), (-1, -1),
])
def test_negative_values_raise_valueerror(weight, length):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight, length)


@pytest.mark.parametrize("weight, length", [
    ("100", 100), (100, "100"), (100.5, 100), (100, 100.5),
    (None, 100), (100, None),
    (True, 100), (100, True), (False, 100), (100, False),
])
def test_invalid_type_raises_typeerror(weight, length):
    with pytest.raises(TypeError):
        is_parcel_accepted(weight, length)
