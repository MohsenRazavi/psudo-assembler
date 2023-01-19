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
            # else:
            #     destination = int(operation[1][:-1].strip())

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

    register_flag_value = {
        "eax": 0,
        "ebx": 0,
        "ecx": 0,
        "edx": 0,
        "carry_flag": 0,
        "overflow_flag": 0,
        "negative_flag": 0,
        "carry_flag": 0,
        "zero_flag": 0,
    }

    and_ = And()
    or_ = Or()
    sub = Sub()
    add = Add()
    mov = Mov()

    eax = Eax()
    ebx = Ebx()
    ecx = Ecx()
    edx = Edx()

    for instruction in instructions:
        pass
    return register_flag_value

    register_flag_value["eax"] = eax.value
    register_flag_value["ebx"] = ebx.value
    register_flag_value["ecx"] = ecx.value
    register_flag_value["edx"] = edx.value

    # if instruction[0] == "mov":
    #     if instruction[1] == "eax":
    #         if instruction[2] == "eax":
    #             mov.res(eax, eax)
    #
    #         elif instruction[2] == "ebx":
    #             mov.res(eax, ebx)
    #
    #         elif instruction[2] == "ecx":
    #             mov.res(eax, ecx)
    #
    #         elif instruction[2] == "edx":
    #             mov.res(eax, edx)
    #         else:
    #             source = int(instruction[2])
    #             mov.res(eax, source)
    #
    #     elif instruction[1] == "ebx":
    #         if instruction[2] == "eax":
    #             mov.res(ebx, eax)
    #
    #         elif instruction[2] == "ebx":
    #             mov.res(ebx, ebx)
    #
    #         elif instruction[2] == "ecx":
    #             mov.res(ebx, ecx)
    #
    #         elif instruction[2] == "edx":
    #             mov.res(ebx, edx)
    #         else:
    #             source = int(instruction[2])
    #             mov.res(eax, source)
    #     elif instruction[1] == "ecx":
    #         destination = "ecx"
    #
    #     elif instruction[1] == "edx":
    #         destination = "edx"
    # elif instruction[0] == "add":
    #     command = "add"
    # elif instruction[0] == "sub":
    #     command = "sub"
    # elif instruction[0] == "and":
    #     command = "and"
    # elif instruction[0] == "or":
    #     command = "or"
