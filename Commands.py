from Registers import *


class Command:
    def __init__(self, *args):
        pass

    def res(self, destination, source, func, **flags):
        if not isinstance(destination, Register) and not isinstance(source, Register):
            dest_size = destination(0, get_size=True)
            src_val = source(0, get_value=True)
            dest_val = destination(0, get_value=True)
            ans = func(dest_val, src_val)
            destination(ans, get_value=False)
            if src_val > dest_size:
                flags["carry_flag"] = 1

            return
        elif not isinstance(destination, Register):
            try:
                dest_size = destination(0, get_size=True)
                src_val = source
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val)
                destination(ans, get_value=False)
                if source > dest_size:
                    flags["carry_flag"] = 1

                return
            except:
                dest_size = destination(0, get_size=True)
                src_val = source
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val)
                destination(ans, get_value=False)
                if source.value > dest_size:
                    flags["carry_flag"] = 1

                return
        elif not isinstance(source, Register) and not isinstance(source, int):
            try:
                dest_size = destination(0, get_size=True)
                src_val = source(0, get_value=True)
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val)
                destination.value = ans
                if source(get_value=True) > dest_size:
                    flags["carry_flag"] = 1
                return
            except:
                dest_size = destination(0, get_size=True)
                src_val = source
                dest_val = destination(0, get_value=True)
                ans = func(dest_val, src_val)
                destination = ans
                if source(get_value=True) > dest_size:
                    flags["carry_flag"] = 1
                return

        try:
            dest_size = destination.max_size
            src_val = source.value
            dest_val = destination.value
            ans = func(dest_val, src_val)
            destination.value = ans
        except:
            try:
                src_val = source
                dest_val = destination.value
                ans = func(dest_val, src_val)
                destination.value = ans
            except:
                try:
                    src_val = source
                    dest_val = destination
                    ans = func(dest_val, src_val)
                    destination = ans
                except:
                    src_val = source.value
                    dest_val = destination(0, get_value=True)
                    ans = func(dest_val, src_val)
                    destination = ans

        if src_val > dest_size:
            flags["carry_flag"] = 1


class And(Command):
    def __init__(self):
        super(And, self).__init__()

    def and_(self, dest_val, src_val):
        ans = dest_val & src_val
        return ans

    def res(self, destination, source, **flags):
        super().res(destination, source, func=self.and_, **flags)
        # try:
        #     dest_size = destination(0, get_size=True)
        # except:
        #     dest_size = destination.max_size
        # if not isinstance(destination, Register) and not isinstance(source, Register):
        #     source_val = source(0, get_value=True)
        #     dest_val = destination(0, get_value=True)
        #     dest_val &= source_val
        #     destination(dest_val, get_value=False)
        #     return
        # elif not isinstance(destination, Register):
        #     try:
        #         dest_value = destination(0, get_value=True)
        #         dest_value &= source.value
        #         destination(dest_value, get_value=False)
        #         return
        #     except:
        #         destination(0, get_value=True)
        #         dest_value &= source
        #         destination(dest_value, get_value=False)
        #         return
        # elif not isinstance(source, Register) and not isinstance(source, int):
        #     try:
        #         destination.value &= source(0, get_value=True)
        #         return
        #     except:
        #
        #         destination &= source(0, get_value=True)
        #         return
        # try:
        #     destination.value &= source.value
        # except:
        #     try:
        #         destination.value &= source
        #     except:
        #         try:
        #             destination &= source
        #         except:
        #             destination &= source.value


class Or(Command):
    def __init__(self):
        super(Or, self).__init__()

    def or_(self, dest_val, src_val):
        ans = dest_val | src_val
        return ans

    def res(self, destination, source, **flags):
        super().res(destination, source, func=self.or_, **flags)
        # try:
        #     dest_size = destination(0, get_size=True)
        # except:
        #     dest_size = destination.max_size
        # if not isinstance(destination, Register) and not isinstance(source, Register):
        #     source_val = source(0, get_value=True)
        #     dest_val = destination(0, get_value=True)
        #     dest_val |= source_val
        #     destination(dest_val, get_value=False)
        #     return
        # elif not isinstance(destination, Register):
        #     try:
        #         dest_value = destination(0, get_value=True)
        #         dest_value |= source.value
        #         destination(dest_value, get_value=False)
        #         return
        #     except:
        #         destination(0, get_value=True)
        #         dest_value |= source
        #         destination(dest_value, get_value=False)
        #         return
        # elif not isinstance(source, Register) and not isinstance(source, int):
        #     try:
        #         destination.value |= source(0, get_value=True)
        #         return
        #     except:
        #         destination |= source(0, get_value=True)
        #         return
        # try:
        #     destination.value |= source.value
        # except:
        #     try:
        #         destination.value |= source
        #     except:
        #         try:
        #             destination |= source
        #         except:
        #             destination |= source.value
        #


class Sub(Command):
    def __init__(self):
        super(Sub, self).__init__()

    def sub(self, dest_val, src_val):
        ans = dest_val - src_val
        return ans

    def res(self, destination, source, **flags):
        super().res(destination, source, func=self.sub, **flags)
        # try:
        #     dest_size = destination(0, get_size=True)
        # except:
        #     dest_size = destination.max_size
        # if not isinstance(destination, Register) and not isinstance(source, Register):
        #     source_val = source(0, get_value=True)
        #     dest_val = destination(0, get_value=True)
        #     dest_val -= source_val
        #     destination(dest_val, get_value=False)
        #     return
        # elif not isinstance(destination, Register):
        #     try:
        #         dest_value = destination(0, get_value=True)
        #         dest_value -= source.value
        #         destination(dest_value, get_value=False)
        #         return
        #     except:
        #         destination(0, get_value=True)
        #         dest_value -= source
        #         destination(dest_value, get_value=False)
        #         return
        # elif not isinstance(source, Register) and not isinstance(source, int):
        #     try:
        #         destination.value -= source(0, get_value=True)
        #         return
        #     except:
        #         destination -= source(0, get_value=True)
        #         return
        # try:
        #     destination.value -= source.value
        # except:
        #     try:
        #         destination.value -= source
        #     except:
        #         try:
        #             destination -= source
        #         except:
        #             destination -= source.value


class Add(Command):
    def __init__(self):
        super(Add, self).__init__()

    def add(self, dest_val, src_val):
        ans = dest_val + src_val
        return ans

    def res(self, destination, source, **flags):
        super().res(destination, source, func=self.add, **flags)
        # try:
        #     dest_size = destination(0, get_size=True)
        # except:
        #     dest_size = destination.max_size
        # if not isinstance(destination, Register) and not isinstance(source, Register):
        #     source_val = source(0, get_value=True)
        #     dest_val = destination(0, get_value=True)
        #     dest_val += source_val
        #     destination(dest_val, get_value=False)
        #     return
        # elif not isinstance(destination, Register):
        #     try:
        #         dest_value = destination(0, get_value=True)
        #         dest_value += source.value
        #         destination(dest_value, get_value=False)
        #         return
        #     except:
        #         destination(0, get_value=True)
        #         dest_value += source
        #         destination(dest_value, get_value=False)
        #         return
        #
        # elif not isinstance(source, Register) and not isinstance(source, int):
        #     try:
        #         destination.value += source(0, get_value=True)
        #         return
        #     except:
        #
        #         destination += source(0, get_value=True)
        #         return
        #
        # try:
        #     destination.value += source.value
        # except:
        #     try:
        #         destination.value += source
        #     except:
        #         try:
        #             destination += source
        #         except:
        #             destination += source.value
        #


class Mov(Command):
    def __init__(self):
        super(Mov, self).__init__()

    def mov(self, dest_val, src_val):
        ans = src_val
        return ans

    def res(self, destination, source, **flags):
        super().res(destination, source, func=self.mov, **flags)
        # dest_size = destination(0, get_size=True)
        # if not isinstance(destination, Register) and not isinstance(source, Register):
        #     source_val = source(0, get_value=True)
        #     destination(source_val, get_value=False)
        #     if source_val > dest_size:
        #         flags["carry_flag"] = 1
        #
        #     return
        # elif not isinstance(destination, Register):
        #     try:
        #         destination(source, get_value=False)
        #         if source > dest_size:
        #             flags["carry_flag"] = 1
        #
        #         return
        #     except:
        #         destination(source.value, get_value=False)
        #         if source.value > dest_size:
        #             flags["carry_flag"] = 1
        #
        #         return
        # elif not isinstance(source, Register) and not isinstance(source, int):
        #     try:
        #         destination.value = source(0, get_value=True)
        #         if source(get_value=True) > dest_size:
        #             flags["carry_flag"] = 1
        #         return
        #     except:
        #
        #         destination = source(0, get_value=True)
        #         if source(get_value=True) > dest_size:
        #             flags["carry_flag"] = 1
        #         return
        #
        # try:
        #     destination.value = source.value
        # except:
        #     try:
        #         destination.value = source
        #     except:
        #         try:
        #             destination = source
        #         except:
        #             destination = source.value
        # try:
        #     if source > dest_size:
        #         flags["carry_flag"] = 1
        # except:
        #     if source.value > dest_size:
        #         flags["carry_flag"]


