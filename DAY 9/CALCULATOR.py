import os

os.system("cls")
# ALL THE FUNCTIONS PART HERE >>
# ARITHMETIC FUNCTIONS <>
sum = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b
rem = lambda a, b: a % b
# UNIT CONVERTER <>
ftoc = lambda a: (0.555) * (a - 32)
ctof = lambda a: (a * 1.8) + 32
# Measure CONVERTER <>
# CM PART >>
cmtomm = lambda a: a * 10
cmtodm = lambda a: a / 10
cmtom = lambda a: a / 100
cmtodec = lambda a: a / 1000
cmtohec = lambda a: a / 10000
cmtokm = lambda a: a / 100000
# MTR PART >>
mtomm = lambda a: a * 1000
mtocm = lambda a: a * 100
mtodm = lambda a: a * 10
mtodec = lambda a: a / 10
mtohec = lambda a: a / 100
mtokm = lambda a: a / 1000
# BY IMRAN KHAN : @imranpgda
val_inp = input("Type -Start- to get tarted >> ")
k = 1
while val_inp != "exit":
    val_inp = input("\nENTER THE WHOLE OPERATION YOU WANT TO PERFORM >> ")
    if val_inp == "exit":
        print("YOU HAVE EXITED  <<< BYE BYEEE >>>")
        break
    # SPLITTING STRING HERE
    new = val_inp.split()
    print()

    # PRINTING PART HERE
    os.system("cls")
    print("RESULT", k, ": ", end="")
    k += 1
    if new[1] == "+":
        print(new[0], "+", new[-1], ">> ", sum(int(new[0]), int(new[-1])))
    elif new[1] == "-":
        print(new[0], "-", new[-1], ">> ", sub(int(new[0]), int(new[-1])))
    elif new[1] == "*":
        print(new[0], "*", new[-1], ">> ", mul(int(new[0]), int(new[-1])))
    elif new[1] == "/":
        print(new[0], "/", new[-1], ">> ", div(int(new[0]), int(new[-1])))
    elif new[1] == "%":
        print(new[0], "%", new[-1], ">> ", rem(int(new[0]), int(new[-1])))
    # TEMP CONVERT
    elif new[-1] == "c":
        print(new[0], "F", ">> ", ftoc(int(new[0])), "C")
    elif new[-1] == "f":
        print(new[0], "C", ">> ", ctof(int(new[0])), "F")
    # DIS CONVERT
    if new[1] == "cm":
        if new[-1] == "mm":
            print(new[0], "CM >>", cmtomm(int(new[0])), "MiliMeter")
        elif new[-1] == "dm":
            print(new[0], "CM >>", cmtodm(int(new[0])), "DeciMeter")
        elif new[-1] == "m":
            print(new[0], "CM  >>", cmtom(int(new[0])), "Meter")
        elif new[-1] == "dec":
            print(new[0], "CM  >>", cmtodec(int(new[0])), "DeciMeter")
        elif new[-1] == "hec":
            print(new[0], "CM  >>", cmtohec(int(new[0])), "HectoMeter")
        elif new[-1] == "km":
            print(new[0], "CM >>", cmtokm(int(new[0])), "KiloMeter")

    if new[1] == "m":
        if new[-1] == "mm":
            print(new[0], "Mtr >>", mtomm(int(new[0])), "MiliMeter")
        elif new[-1] == "cm":
            print(new[0], "Mtr >>", mtocm(int(new[0])), "CentiMeter")
        elif new[-1] == "dm":
            print(new[0], "Mtr >>", mtodm(int(new[0])), "Decimeter")
        elif new[-1] == "dec":
            print(new[0], "Mtr >>", mtodec(int(new[0])), "DecaMeter")
        elif new[-1] == "hec":
            print(new[0], "Mtr >>", mtohec(int(new[0])), "HectoMeter")
        elif new[-1] == "km":
            print(new[0], "Mtr >>", mtokm(int(new[0])), "KiloMeter")

print()
