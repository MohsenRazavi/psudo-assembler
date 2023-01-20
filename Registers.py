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
        return int(val[16:], 2)

    def get_al(self):
        val = '{0:032b}'.format(self.value)
        return int(val[25:], 2)

    def get_ah(self):
        val = '{0:032b}'.format(self.value)
        return int(val[17:25], 2)

    def set_ax(self, ax_val, get_vlue):
        if get_vlue:
            return self.get_ax()

        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:016b}'.format(ax_val)
        for i in range(16, 32):
            val[i] = new_sub_val[i-16]
        self.value = int(''.join(val), 2)
        return

    def set_al(self, al_val, get_vlue):
        if get_vlue:
            return self.get_al()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(al_val)
        for i in range(25, 32):
            val[i] = new_sub_val[i-24]
        self.value = int(''.join(val), 2)

    def set_ah(self, ah_val, get_vlue):
        if get_vlue:
            return self.get_ah()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(ah_val)
        for i in range(17, 25):
            val[i] = new_sub_val[i - 17]
        self.value = int(''.join(val), 2)


class Ebx(Register):
    bytes = 4

    def get_bx(self):
        val = '{0:032b}'.format(self.value)
        return int(val[16:], 2)

    def get_bl(self):
        val = '{0:032b}'.format(self.value)
        return int(val[25:], 2)

    def get_bh(self):
        val = '{0:032b}'.format(self.value)
        return int(val[16:24], 2)

    def set_bx(self, bx_val, get_value):
        if get_value:
            return self.get_bx()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:016b}'.format(bx_val)
        for i in range(16, 32):
            val[i] = new_sub_val[i-16]
        self.value = int(''.join(val), 2)

    def set_bl(self, bl_val, get_value):
        if get_value:
            return self.get_bl()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(bl_val)
        for i in range(25, 32):
            val[i] = new_sub_val[i-24]
        self.value = int(''.join(val), 2)

    def set_bh(self, bh_val, get_value):
        if get_value:
            return self.get_bh()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(bh_val)
        for i in range(17, 25):
            val[i] = new_sub_val[i - 17]
        self.value = int(''.join(val), 2)


class Ecx(Register):
    bytes = 4

    def get_cx(self):
        val = '{0:032b}'.format(self.value)
        return int(val[16:], 2)

    def get_cl(self):
        val = '{0:032b}'.format(self.value)
        return int(val[25:], 2)

    def get_ch(self):
        val = '{0:032b}'.format(self.value)
        return int(val[16:24], 2)

    def set_cx(self, cx_val, get_value):
        if get_value:
            return self.get_cx()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:016b}'.format(cx_val)
        for i in range(16, 32):
            val[i] = new_sub_val[i-16]
        self.value = int(''.join(val), 2)

    def set_cl(self, cl_val, get_value):
        if get_value:
            return self.get_cl()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(cl_val)
        for i in range(25, 32):
            val[i] = new_sub_val[i-24]
        self.value = int(''.join(val), 2)

    def set_ch(self, ch_val, get_value):
        if get_value:
            return self.get_ch()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(ch_val)
        for i in range(17, 25):
            val[i] = new_sub_val[i - 17]
        self.value = int(''.join(val), 2)


class Edx(Register):
    bytes = 4

    def get_dx(self):
        val = '{0:032b}'.format(self.value)
        return int(val[16:], 2)

    def get_dl(self):
        val = '{0:032b}'.format(self.value)
        return int(val[25:], 2)

    def get_dh(self):
        val = '{0:032b}'.format(self.value)
        return int(val[16:24], 2)

    def set_dx(self, dx_val, get_value):
        if get_value:
            return self.get_dx()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:016b}'.format(dx_val)
        for i in range(16, 32):
            val[i] = new_sub_val[i-16]
        self.value = int(''.join(val), 2)

    def set_dl(self, dl_val, get_value):
        if get_value:
            return self.get_dl()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(dl_val)
        for i in range(25, 32):
            val[i] = new_sub_val[i-24]
        self.value = int(''.join(val), 2)

    def set_dh(self, dh_val, get_value):
        if get_value:
            return self.get_dh()
        val = list('{0:032b}'.format(self.value))
        new_sub_val = '{0:08b}'.format(dh_val)
        for i in range(17, 25):
            val[i] = new_sub_val[i - 17]
        self.value = int(''.join(val), 2)
