from Registers import *


class Command:
    def __init__(self, *args):
        pass

    #     try:
    #         self.destination = args[0]
    #         self.source = args[1]
    #     except:
    #         pass
    def res(self, *args, **kwargs):
        pass


class And(Command):
    def __init__(self):
        super(And, self).__init__()

    def res(self, destination, source):
        if not isinstance(destination, Register):
            try:
                dest_value = destination(0, True)
                dest_value &= source.value
                destination(dest_value, False)
                return
            except:
                destination(0, True)
                dest_value &= source
                destination(dest_value, False)
                return
        if not isinstance(source, Register) and not isinstance(source, int):
            try:
                destination.value &= source(0, True)
                return
            except:

                destination &= source(0, True)
                return
        try:
            destination.value &= source.value
        except:
            try:
                destination.value &= source
            except:
                try:
                    destination &= source
                except:
                    destination &= source.value


class Or(Command):
    def __init__(self):
        super(Or, self).__init__()

    def res(self, destination, source):
        if not isinstance(destination, Register):
            try:
                dest_value = destination(0, True)
                dest_value |= source.value
                destination(dest_value, False)
                return
            except:
                destination(0, True)
                dest_value |= source
                destination(dest_value, False)
                return
        if not isinstance(source, Register) and not isinstance(source, int):
            try:
                destination.value |= source(0, True)
                return
            except:

                destination |= source(0, True)
                return
        try:
            destination.value |= source.value
        except:
            try:
                destination.value |= source
            except:
                try:
                    destination |= source
                except:
                    destination |= source.value


class Sub(Command):
    def __init__(self):
        super(Sub, self).__init__()

    def res(self, destination, source):
        if not isinstance(destination, Register):
            try:
                dest_value = destination(0, True)
                dest_value -= source.value
                destination(dest_value, False)
                return
            except:
                destination(0, True)
                dest_value -= source
                destination(dest_value, False)
                return
        if not isinstance(source, Register) and not isinstance(source, int):
            try:
                destination.value -= source(0, True)
                return
            except:

                destination -= source(0, True)
                return
        try:
            destination.value -= source.value
        except:
            try:
                destination.value -= source
            except:
                try:
                    destination -= source
                except:
                    destination -= source.value


class Add(Command):
    def __init__(self):
        super(Add, self).__init__()

    def res(self, destination, source):
        if not isinstance(destination, Register):
            try:
                dest_value = destination(0, True)
                dest_value += source.value
                destination(dest_value, False)
                return
            except:
                destination(0, True)
                dest_value += source
                destination(dest_value, False)
                return

        if not isinstance(source, Register) and not isinstance(source, int):
            try:
                destination.value += source(0, True)
                return
            except:

                destination += source(0, True)
                return
        try:
            destination.value += source.value
        except:
            try:
                destination.value += source
            except:
                try:
                    destination += source
                except:
                    destination += source.value


class Mov(Command):
    def __init__(self):
        super(Mov, self).__init__()

    def res(self, destination, source):
        if not isinstance(destination, Register):
            try:
                destination(source, False)
                return
            except:
                destination(source.value, False)
                return
        if not isinstance(source, Register) and not isinstance(source, int):
            try:
                destination.value = source(0, True)
                return
            except:

                destination = source(0, True)
                return
        try:
            destination.value = source.value
        except:
            try:
                destination.value = source
            except:
                try:
                    destination = source
                except:
                    destination = source.value
