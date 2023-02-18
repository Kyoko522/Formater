#!/usr/bin/env python3
import subprocess
import sys
import ast

def main():
    open_file()
    toBinary()
    format()
    print("-d\tdownload")
    print("-c\tcopy to clipboard")
    print("-n\tnotes (comments) ")
    print("-a\tshow addresses")
    print("  \tnothing will just print in terminal")
    option = (input("Pick your option: "))
    count = 0
    for i in range(len(option) - 1):
        if option[i:i + 2] == "-d":
            to_write()
            count = 1
        if option[i:i + 2] == "-c":
            copy_to_clip()
            count = 1
        if option[i:i + 2] == "-n":
            toprint(anotation(format()))
            count = 1
        if option[i:i + 2] == "-a":
            count = 1
            toprint(addresses())
    if count == 0:
        toprint(format())
# Open the file and safe the machine code that has already been converted inot hex
def open_file():
    lines = []
    n = (sys.argv[1])
    data = open(n)
    for  line in data:
        lines.append(line.strip().lower()[9::]) #remove the address hex we only want the machine code
    data.close()
    lines = lines[1::]
    return lines

def getAddress():
    lines = []
    declist = []
    n = (sys.argv[1])
    data = open(n)
    for line in data:
        lines.append(line.strip().lower()[:8])
    data.close()
    lines = lines[1::]
    for i in lines:
       declist.append(hex_to_dec(i))
    return declist


def toBinary():
    binary = ""
    binarylist = []
    for hex in open_file():
        for j in range (len(hex)):
            if hex[j] == "0":
                binary = binary + "0000"
            elif hex[j] == "1":
                binary = binary + "0001"
            elif hex[j] == "2":
                binary = binary + "0010"
            elif hex[j] == "3":
                binary = binary + "0011"
            elif hex[j] == "4":
                binary = binary + "0100"
            elif hex[j] == "5":
                binary = binary + "0101"
            elif hex[j] == "6":
                binary = binary + "0110"
            elif hex[j] == "7":
                binary = binary + "0111"
            elif hex[j] == "8":
                binary = binary + "1000"
            elif hex[j] == "9":
                binary = binary + "1001"
            elif hex[j] == "a":
                binary = binary + "1010"
            elif hex[j] == "b":
                binary = binary + "1011"
            elif hex[j] == "c":
                binary = binary + "1100"
            elif hex[j] == "d":
                binary = binary + "1101"
            elif hex[j] == "e":
                binary = binary + "1110"
            elif hex[j] == "f":
                binary = binary + "1111"
        binarylist.append(binary)
        binary = ""
    return binarylist


def hex_to_dec(hex):
    return int(hex, 16)

def bin_to_dec(bin):
    return int(bin, 2)



def format():
    fl = []

    for i in toBinary():
        formated = ""
        if i[0:2] == "00" and i[7:10] == "100":
            formated = i[0:2] + " "+ i[2:7] + " " + i[7: 10] + " " + i[10::]

        elif i[0:2] == "00" and i[7:10] == "010":
            formated = i[0:2] + " " + i[2] + " " + i[3:7] + " " + i[7:10] + " " + i[10::]

        elif i[0:2] == "01":
            formated = i[0:2] + " " + i[2::]

        elif i[0] == "1" and i[18] == "0":
            formated = i[0:2] + " " + i[2:7] + " " + i[7:13] + " " + i[13 : 18] + " " + i[18] + " " + i[19:27] + " " + i[27::]

        elif i[0] == "1" and i[18] == "1":
            formated = i[0:2] + " " + i[2:7] + " " + i[7:13] + " " + i[13 : 18] + " " + i[18] + " " + i[19::]

        else:
            formated = i
        fl.append(formated)

    return fl


def toprint(list):
    print ("\n")
    for i in list:
        print(str(i))
    print("\n")

def copy_to_clip():
    cp = ""
    for i in format():
        cp += i + "\n"
    subprocess.run("pbcopy", text=True, input=cp)

def to_first_comp(comp2):
    comp2 = comp2-1
    s_and_m =""
    for i in comp2:
        if i == 1:
            s_and_m += "1"
        else:
            s_and_m += "0"
    return s_and_m

def to_write():
    cp = ""
    f = open("result.txt","w")
    for i in format():
        cp += i + "\n"
    f.write(cp)

def anotation(list):
    anotationed_list = []
    resultlist = []
    for i in (toBinary()):
        notes = ""
        if i[0:2] == "00" and i[7:10] == "010":
            notes = "-> Branch Format, "
            if i[3:7] == "0001":
                notes += "Branch if equal, " #+ "Branch to " + bin_to_dec(i[10::])
            elif i[3:7] == "0101":
                notes += "Branch on carry"
            elif i[3:7] == "0110":
                notes += "Branch on negative"
            elif i[3:7] == "0111":
                notes += "Branch on overflow"
            elif i[3:7] == "1000":
                notes += "Branch always"

        elif i[0:2] == "00" and i[7:10] == "100":
            notes = "-> SETHI Format, "

        elif i[0:2] == "01":
            notes = "-> CALL format, "

        elif i[0:2] == "10":
            notes = "-> Arithmetic Format, "
            if i[7:13] == "010000":
                notes += "Add "
            elif i[7:13] == "010100":
                notes += "Subtraction "
            elif i[7:13] == "010001":
                notes += "Bitwise logical AND "
            elif i[7:13] == "010010":
                notes += "Bitwise logical OR "
            elif i[7:13] == "010110":
                notes += "Bitwise logical NOR "
            elif i[7:13] == "100110":
                notes += "Shift right (logical) "
            elif i[7:13] == "111000":
                notes += "Jump and link (return from subroutine call) "

        elif i[0:2] == "11": #and (i[7:13] != "111111" and i[7:13] != "000000"):
            notes= "-> Memory Format, "
            if i[7:13] == "000000":
                if i[18] == "0":
                    notes += "Load register " + str(bin_to_dec(i[2:7])) + " with what's in register " + str(bin_to_dec(i[27]))
                elif i[18] == "1":
                    notes += "Load register " + str(bin_to_dec(i[2:7])) + " from memory " + str(bin_to_dec(i[19::]))
        else:
            notes= "-> Data: " + str(bin_to_dec(i))

        anotationed_list.append(notes)

    for i in range (len(format())):
        result = list[i] +"\t\t"+anotationed_list[i]
        resultlist.append(result)

    return resultlist

def upadte_list():
    pass

def addresses():
    addresList = []
    for i in range(len(format())):
        addresList.append(str(getAddress()[i]) + ":\t" + str(format()[i]))
    return addresList

if __name__ == "__main__":
    main()



