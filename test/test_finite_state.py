"""Tests for finte_state"""
import pytest
from automata.base.exceptions import RejectionException

from finite_state import FiniteState


@pytest.mark.parametrize(
    "value",
    [
        "110",
        "1010",
    ]
)
def test_finite_state(value):
    """Testing good values, and returning the final value"""
    sut = FiniteState()
    result = sut.get_final_value(value)
    print(f"\nFor: {value} Result: {result}")


@pytest.mark.parametrize(
    "value",
    [
        "1010",
    ]
)
def test_rejection(value):
    """Testing RejectionException based on invalid final state"""
    sut = FiniteState(final_states={'S0'})
    with pytest.raises(RejectionException) as exinfo:
        sut.get_final_value(value)
    print(f"\nFor: {value} Result: {str(exinfo.value)}")
