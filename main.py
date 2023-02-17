#!/usr/bin/env python3
import subprocess
import sys


def open_file():
    lines = []
    n = (sys.argv[1])
    data = open(n)
    for  line in data:
        lines.append(line.strip().lower()[9::])
    data.close()
    lines = lines[1::]
    return lines


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


def toprint():
    for i in format():
        print(str(i))

def copy_to_clip():
    cp = ""
    for i in format():
        cp += i + "\n"
    subprocess.run("pbcopy", text=True, input=cp)

def to_write():
    cp = ""
    f = open("result.txt","w")
    for i in format():
        cp += i + "\n"
    f.write(cp)

def anotation():
    pass

def addresses():
    pass


if __name__ == "__main__":
    open_file ()
    toBinary()
    format()
    print ("-p\tprint")
    print ("-d\tdownload")
    print ("-c\tcopy to clipboard")
    print ("-n\tnotes (comments)")
    print ("-a\tshow addresses")
    option = (input("Pick your option: "))
    if option == "-p":
        toprint()
    elif option == "-d":
        to_write()
    elif option == "-c":
        copy_to_clip()
    elif option == "-n":
        anotation ()


