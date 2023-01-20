from Commands import *
from Registers import *


def get_instructions(str_code):
    mov_list = ["mov", "Mov", "mOv", "moV"]
    add_list = ["add"]
    sub_list = ["sub"]
    and_list = ["and"]
    or_list = ["or"]
    eax_list = ["eax", "ax", "al", "ah"]
    ebx_list = ["ebx", "bx", "bl", "bh"]
    ecx_list = ["ecx", "cx", "cl", "ch"]
    edx_list = ["edx", "dx", "dl", "dh"]

    operations = []
    list_code = str_code.split("\n")
    command = ""
    destination = ""
    source = ""
    for opr in list_code:
        if opr:
            operation = opr.split(" ")
            if operation[0].strip() in mov_list:
                command = "mov"
            elif operation[0].strip() in add_list:
                command = "add"
            elif operation[0].strip() in sub_list:
                command = "sub"
            elif operation[0].strip() in and_list:
                command = "and"
            elif operation[0].strip() in or_list:
                command = "or"

            if operation[1][:-1].strip() in eax_list:
                destination = "eax"

            elif operation[1][:-1].strip() in ebx_list:
                destination = "ebx"

            elif operation[1][:-1].strip() in ecx_list:
                destination = "ecx"

            elif operation[1][:-1].strip() in edx_list:
                destination = "edx"

            if operation[2].strip() in eax_list:
                source = "eax"

            elif operation[2].strip() in ebx_list:
                source = "ebx"

            elif operation[2].strip() in ecx_list:
                source = "ecx"

            elif operation[2].strip() in edx_list:
                source = "edx"
            else:
                source = int(operation[2].strip())

            operations.append([command, destination, source])
    return operations


def execute(raw_code):
    instructions = get_instructions(raw_code)
    eax = Eax()
    ebx = Ebx()
    ecx = Ecx()
    edx = Edx()

    registers = {
        "eax": eax,
        "ebx": ebx,
        "ecx": ecx,
        "edx": edx,
    }

    and_ = And()
    or_ = Or()
    sub = Sub()
    add = Add()
    mov = Mov()

    commands = {
        "and": and_,
        "or": or_,
        "sub": sub,
        "add": add,
        "mov": mov
    }

    for instruction in instructions:
        try:
            commands[instruction[0]].res(registers[instruction[1]], registers[instruction[2]])
        except:
            commands[instruction[0]].res(registers[instruction[1]], instruction[2])

    print(eax.value)
