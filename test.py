from Commands import *
from Registers import *

and_ = And()
or_ = Or()
sub = Sub()
add = Add()
mov = Mov()

eax = Eax()
ebx = Ebx()

mov.res(eax, 4)
mov.res(ebx, 5)
and_.res(eax, 5)
or_.res(ebx, 4)

print("eax\t", eax.get_ax())
print("ebx\t", ebx.get_bh())

