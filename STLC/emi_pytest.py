import pytest
from math import isclose
from loan import calculate_emi

@pytest.mark.parametrize("principal, rate, years", [
    (100000, 0.06, 1),
    (100000, 0.06, 5),
    (100000, 0.06, 30),
])
def test_emi_total_payment(principal, rate, years):
    emi = calculate_emi(principal, rate, years)
    total_paid = round(emi * years * 12, 2)
    interest = round(total_paid - principal, 2)
    assert isclose(total_paid, principal + interest, rel_tol=1e-2)
