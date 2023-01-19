class Register:
    bytes = 0
    max_size = 2 ** (8 * bytes)

    def __init__(self):
        self.value = 0

    def set_value(self, val):
        if val > self.max_size:
            print("value is bigger than max size")
            return
        self.value = val

    def get_value(self):
        pass


class Eax(Register):
    bytes = 4

    def get_ax(self):
        val = '{0:032b}'.format(self.value)
        return val[15:]

    def get_al(self):
        val = '{0:032b}'.format(self.value)
        return val[23:]

    def get_ah(self):
        val = '{0:032b}'.format(self.value)
        return val[16:24]


class Ebx(Register):
    bytes = 4

    def get_bx(self):
        val = '{0:032b}'.format(self.value)
        return val[15:]

    def get_bl(self):
        val = '{0:032b}'.format(self.value)
        return val[23:]

    def get_bh(self):
        val = '{0:032b}'.format(self.value)
        return val[16:24]


class Ecx(Register):
    bytes = 4

    def get_cx(self):
        val = '{0:032b}'.format(self.value)
        return val[15:]

    def get_cl(self):
        val = '{0:032b}'.format(self.value)
        return val[23:]

    def get_ch(self):
        val = '{0:032b}'.format(self.value)
        return val[16:24]


class Edx(Register):
    bytes = 4

    def get_dx(self):
        val = '{0:032b}'.format(self.value)
        return val[15:]

    def get_dl(self):
        val = '{0:032b}'.format(self.value)
        return val[23:]

    def get_dh(self):
        val = '{0:032b}'.format(self.value)
        return val[16:24]
