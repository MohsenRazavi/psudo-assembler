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
mov ah, 1
add al, 1
add eax, 16
"""
eax = Eax()
print(type(eax.set_ah))
print(execute(st))
# a =32*"0"
# for i in a:
#     print(i, end="\t")
# print()
# for i in range(32):
#     print(i, end='\t')
