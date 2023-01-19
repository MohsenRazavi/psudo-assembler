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
