from Commands import *
from Registers import *


def get_instructions(str_code):
    mov_list = ["mov", "Mov", "MOV"]
    add_list = ["add", "Add", "ADD"]
    sub_list = ["sub", "Sub", "SUB"]
    and_list = ["and", "And", "AND"]
    or_list = ["or", "Or", "OR"]

    eax_list = ["eax", "Eax", "EAX"]
    ax_list = ["ax", "Ax", "AX"]
    al_list = ["al", "Al", "AL"]
    ah_list = ["ah", "Ah", "AH"]

    ebx_list = ["ebx", "Ebx", "EBX"]
    bx_list = ["bx", "Bx", "BX"]
    bl_list = ["bl", "Bl", "BL"]
    bh_list = ["bh", "Bh", "BH"]

    ecx_list = ["ecx", "Ecx", "ECX"]
    cx_list = ["cx", "Cx", "CX"]
    cl_list = ["cl", "Cl", "CL"]
    ch_list = ["ch", "Ch", "Ch"]

    edx_list = ["edx", "Edx", "EDX"]
    dx_list = ["dx", "Dx", "DX"]
    dl_list = ["dl", "Dl", "DL"]
    dh_list = ["dh", "Dh", "DH"]

    operations = []
    list_code = str_code.split("\n")
    command = ""
    destination = ""
    source = ""
    for opr in list_code:
        if opr:
            if opr[0] == ";":
                continue
            operation = opr.split(" ")
            #  check command
            try:
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
                #  check destination
                if operation[1][:-1].strip() in eax_list:
                    destination = "eax"
                elif operation[1][:-1].strip() in ax_list:
                    destination = "ax"
                elif operation[1][:-1].strip() in al_list:
                    destination = "al"
                elif operation[1][:-1].strip() in ah_list:
                    destination = "ah"

                elif operation[1][:-1].strip() in ebx_list:
                    destination = "ebx"
                elif operation[1][:-1].strip() in bx_list:
                    destination = "bx"
                elif operation[1][:-1].strip() in bl_list:
                    destination = "bl"
                elif operation[1][:-1].strip() in bh_list:
                    destination = "bh"

                elif operation[1][:-1].strip() in ecx_list:
                    destination = "ecx"
                elif operation[1][:-1].strip() in cx_list:
                    destination = "cx"
                elif operation[1][:-1].strip() in cl_list:
                    destination = "cl"
                elif operation[1][:-1].strip() in ch_list:
                    destination = "ch"

                elif operation[1][:-1].strip() in edx_list:
                    destination = "edx"
                elif operation[1][:-1].strip() in dx_list:
                    destination = "dx"
                elif operation[1][:-1].strip() in dl_list:
                    destination = "dl"
                elif operation[1][:-1].strip() in dh_list:
                    destination = "dh"

                # check source
                if operation[2].strip() in eax_list:
                    source = "eax"
                elif operation[2].strip() in ax_list:
                    source = "ax"
                elif operation[2].strip() in al_list:
                    source = "al"
                elif operation[2].strip() in ah_list:
                    source = "ah"

                elif operation[2].strip() in ebx_list:
                    source = "ebx"
                elif operation[2].strip() in bx_list:
                    source = "bx"
                elif operation[2].strip() in bl_list:
                    source = "bl"
                elif operation[2].strip() in bh_list:
                    source = "bh"

                elif operation[2].strip() in ecx_list:
                    source = "ecx"
                elif operation[2].strip() in cx_list:
                    source = "cx"
                elif operation[2].strip() in cl_list:
                    source = "cl"
                elif operation[2].strip() in ch_list:
                    source = "ch"

                elif operation[2].strip() in edx_list:
                    source = "edx"
                elif operation[2].strip() in dx_list:
                    source = "dx"
                elif operation[2].strip() in dl_list:
                    source = "dl"
                elif operation[2].strip() in dh_list:
                    source = "dh"
                else:
                    try:
                        source = int(operation[2].strip())
                    except:
                        if operation[2][-1] == "d":
                            source = int(operation[2][:-1], 10)
                        elif operation[2][-1] == "b":
                            source = int(operation[2][:-1], 2)
                        elif operation[2][-1] == "h":
                            source = int(operation[2][:-1], 16)
                        elif operation[2][-1] == "o":
                            source = int(operation[2][:-1], 8)
                operations.append([command, destination, source])
            except:
                return []
    return operations


def execute(raw_code):
    instructions = get_instructions(raw_code)
    print(instructions)
    eax = Eax()
    ebx = Ebx()
    ecx = Ecx()
    edx = Edx()

    registers = {
        "eax": eax,
        "ax": eax.set_ax,
        "al": eax.set_al,
        "ah": eax.set_ah,

        "ebx": ebx,
        "bx": ebx.set_bx,
        "bl": ebx.set_bl,
        "bh": ebx.set_bh,

        "ecx": ecx,
        "cx": ecx.set_cx,
        "cl": ecx.set_cl,
        "ch": ecx.set_ch,

        "edx": edx,
        "dx": edx.set_dx,
        "dl": edx.set_dl,
        "dh": edx.set_dh
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

    output = {
        "eax": 0,
        "ebx": 0,
        "ecx": 0,
        "edx": 0,
        "carry_flag": 0,
        "overflow_flag": 0,
        "zero_flag": 0,
        "negative_flag": 0,
    }
    if instructions:
        for instruction in instructions:

            try:
                output = commands[instruction[0]].res(registers[instruction[1]], registers[instruction[2]], **output)
            except:
                output = commands[instruction[0]].res(registers[instruction[1]], instruction[2], **output)
    else:
        output["error"] = "no assembly code found !"

    output["eax"] = '{0:032b}'.format(eax.value)
    output["ebx"] = '{0:032b}'.format(ebx.value)
    output["ecx"] = '{0:032b}'.format(ecx.value)
    output["edx"] = '{0:032b}'.format(edx.value)

    return output
