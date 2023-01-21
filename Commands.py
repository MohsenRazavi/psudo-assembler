from Registers import *


class Command:
    def __init__(self, *args):
        pass

    def res(self, destination, source, func, **flags):
        if not isinstance(destination, Register) and not isinstance(source, Register) and not isinstance(source, int):
            dest_size = destination(0, get_size=True)
            src_val = source(0, get_value=True)
            dest_val = destination(0, get_value=True)
            ans = func(dest_val, src_val)
            destination(ans, get_value=False)
            if src_val > dest_size:
                flags["carry_flag"] = 1
            if ans==0:
                flags["zero_flag"] = 1
            if ans<0:
                flags["negative_flag"] = 1

            return flags
        elif not isinstance(destination, Register):
            try:
                dest_size = destination(0, get_size=True)
                src_val = source
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val, dest_size=dest_size)
                destination(ans, get_value=False)
                if source > dest_size:
                    flags["carry_flag"] = 1
                if ans==0:
                    flags["zero_flag"] = 1
                if ans<0:
                    flags["negative_flag"] = 1

                return flags
            except:
                dest_size = destination(0, get_size=True)
                src_val = source
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val, dest_size=dest_size)
                destination(ans, get_value=False)
                if source.value > dest_size:
                    flags["carry_flag"] = 1
                if ans==0:
                    flags["zero_flag"] = 1
                if ans<0:
                    flags["negative_flag"] = 1

                return flags
        elif not isinstance(source, Register) and not isinstance(source, int):
            try:
                dest_size = destination(0, get_size=True)
                src_val = source(0, get_value=True)
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val, dest_size=dest_size)
                destination.value = ans
                if source(get_value=True) > dest_size:
                    flags["carry_flag"] = 1
                if ans==0:
                    flags["zero_flag"] = 1
                if ans<0:
                    flags["negative_flag"] = 1
                return flags
            except:
                dest_size = destination(0, get_size=True)
                src_val = source
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val, dest_size=dest_size)
                destination = ans
                if source(get_value=True) > dest_size:
                    flags["carry_flag"] = 1
                if ans==0:
                    flags["zero_flag"] = 1
                if ans<0:
                    flags["negative_flag"] = 1
                return flags

        try:
            dest_size = destination.max_size
            src_val = source.value
            dest_val = destination.value
            ans = func(dest_val, src_val, dest_size=dest_size)
            destination.value = ans
        except:
            try:
                dest_size = destination.max_size
                src_val = source
                dest_val = destination.value
                ans = func(dest_val, src_val, dest_size=dest_size)
                destination.value = ans
            except:
                try:
                    src_val = source
                    dest_val = destination
                    ans = func(dest_val, src_val, dest_size=dest_size)
                    destination = ans
                except:
                    src_val = source.value
                    dest_val = destination(0, get_value=True)
                    ans = func(dest_val, src_val, dest_size=dest_size)
                    destination = ans

        if src_val > dest_size:
            flags["carry_flag"] = 1
        if ans==0:
            flags["zero_flag"] = 1
        if ans<0:
            flags["negative_flag"] = 1
        return flags


class And(Command):
    def __init__(self):
        super(And, self).__init__()

    def and_(self, dest_val, src_val, **kwargs):
        ans = dest_val & src_val
        return ans

    def res(self, destination, source, **flags):
        flags = super().res(destination, source, func=self.and_, **flags)
        return flags

class Or(Command):
    def __init__(self):
        super(Or, self).__init__()

    def or_(self, dest_val, src_val, **kwargs):
        ans = dest_val | src_val
        return ans

    def res(self, destination, source, **flags):
        flags = super().res(destination, source, func=self.or_, **flags)
        return flags


class Sub(Command):
    def __init__(self):
        super(Sub, self).__init__()

    def sub(self, dest_val, src_val, **kwargs):
        ans = dest_val - src_val
        return ans

    def res(self, destination, source, **flags):
        flags = super().res(destination, source, func=self.sub, **flags)
        return flags

class Add(Command):
    def __init__(self):
        super(Add, self).__init__()

    def add(self, dest_val, src_val, **kwargs):
        ans = dest_val + src_val
        return ans

    def res(self, destination, source, **flags):
        flags = super().res(destination, source, func=self.add, **flags)
        return flags

class Mov(Command):
    def __init__(self):
        super(Mov, self).__init__()

    def mov(self, dest_val, src_val, **kwargs):
        ans = src_val
        return ans

    def res(self, destination, source, **flags):
        flags = super().res(destination, source, func=self.mov, **flags)
        return flags
