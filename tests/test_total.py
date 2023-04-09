import sys
sys.path.append("..")
from comsumer.tasks import total


def test_total():
    assert total(3,2,2,2) == 9
