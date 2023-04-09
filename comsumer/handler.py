import sys
sys.path.append(".")
from comsumer.tasks import add, multiply

count = 3
add_list = []
multiply_list = []


@staticmethod
def get_result(data):
    print('----')
    print(data.status)
    print(data.get())
    print(data.status)
    print('----')

for i in range(count):
    add_list.append(add.delay(4, 4))
    multiply_list.append(multiply.delay(4, 4))

for i in range(count):
    get_result(add_list[i])
    get_result(multiply_list[i])
