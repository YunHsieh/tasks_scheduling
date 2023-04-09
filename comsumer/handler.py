import sys
sys.path.append(".")
from comsumer.tasks import add, multiply

for i in range(10):
    result1 = add.delay(4, 4)
    result2 = multiply.delay(4, 4)
    print(result1.get())
    print(result2.get())
