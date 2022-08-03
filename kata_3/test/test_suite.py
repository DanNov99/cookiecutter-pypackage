from kata_3.ATM import atm_withdrow
import pytest


@pytest.mark.parametrize("amount, result", [(23, -1), (-23, -1), (1600, -1), (50, 1), (150, 2), (240, 3), (1310, 5)])
def test_atm_withdraw_amount(amount, result):
    assert atm_withdrow(amount) == result
