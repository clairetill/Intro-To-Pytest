# ---------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator

# ---------------------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------------------


@pytest.fixture
def accum():
    return Accumulator
    
# ---------------------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------------------


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2
