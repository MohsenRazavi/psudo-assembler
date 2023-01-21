from Commands import *
from Registers import *
from assembler import *

# command & register test

# and_ = And()
# or_ = Or()
# sub = Sub()
# add = Add()
# mov = Mov()
#
# eax = Eax()
# ebx = Ebx()
#
# mov.res(eax, 4)
# mov.res(ebx, 5)
# and_.res(eax, 5)
# or_.res(ebx, 4)
#
# print("eax\t", eax.get_ax())
# print("ebx\t", ebx.get_bh())

st = """
mov eax, 1024
mov ebx, 4

add eax, bl
"""
eax = Eax()
# FIXME compare types in commands
print(isinstance(eax.set_ah, classmethod))
print(execute(st))
# a =32*"0"
# for i in a:
#     print(i, end="\t")
# print()
# for i in range(32):
#     print(i, end='\t')
