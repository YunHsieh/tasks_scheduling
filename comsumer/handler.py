import sys
sys.path.append(".")
from comsumer.tasks import add, multiply
from celery import group

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
    add_list.append(add.s(i, i*i+1))
    multiply_list.append(multiply.s(i, i*i+1))

add_list = group(add_list)()
multiply_list = group(multiply_list)()

for i in range(count):
    get_result(add_list[i])
    get_result(multiply_list[i])
