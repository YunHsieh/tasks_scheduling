import sys
sys.path.append("..")
from comsumer.tasks import multiply


def test_multiply():
    assert multiply(3,2) == 6
