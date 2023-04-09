import sys
sys.path.append("..")
from comsumer.tasks import add


def test_add():
    assert add(2,2) == 4
