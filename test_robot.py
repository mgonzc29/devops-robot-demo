import pytest
from robot import can_move

def test_safe_distance():
    assert can_move(1.0) is True

def test_unsafe_distance():
    assert can_move(0.2) is False

def test_boundary_distance():
    assert can_move(0.5) is False

def test_invalid_distance():
    with pytest.raises(ValueError):
        can_move(-1.0)