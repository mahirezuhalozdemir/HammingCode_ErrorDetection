import random
from tkinter import *
from tkinter import scrolledtext, messagebox

#mahire zühal özdemir

global emoji1
emoji1 = "\U0001F7E0"
global emoji2
emoji2 = "\U0001F4BB"
# pencere tanımlama
global window
window = Tk()
window.title("Hamming Code Error Detection")
window.configure(bg="#FAF0D7")
window.geometry("1100x600")

global numbers
numbers = []
number = 0
while number < 7:
    numbers.insert(number, pow(2, number))
    number += 1

def hammingCodeError(data):
    global labelData
    labelData = Label(window)
    labelData.place(x=5, y=150)

    for i in data:
        message = i
        text_box = Text(labelData, height=1, width=3)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        text_box.pack(side=LEFT, padx=5)
    global m
    m = len(data)
    txtScrolled.insert(INSERT, emoji1 + 'the length of the data  ' + emoji2 + '  ' + str(m))
    txtScrolled.insert(INSERT, '\n')
    global k
    for k in range(1, 10):
        if ((pow(2, k) - 1) >= m + k):
            break
    global length
    length = m + k
    txtScrolled.insert(INSERT,emoji1 + 'the number of parity bits to use for the data  ' + emoji2 + '  ' + str(k))
    txtScrolled.insert(INSERT, '\n')
    global word
    word = []
    data = list(data)
    c = 0
    for i in range(0, length):
        if i + 1 in numbers:
            word.insert(i, 9)
        else:
            word.insert(i, int(data[-1 + (c * -1)]))
            c += 1
    word.reverse()  # yazilan blok ters çevrilir

    global checkList
    checkList = []
    # 1lerin konumunu bulur
    for i in range(0, length):
        if word[i] == 1:
            checkList.append(length - i)
    txtScrolled.insert(INSERT, emoji1 + "1s position in the data  " + emoji2 + '  ')
    for p in checkList:
        if checkList[-1]==p:
            txtScrolled.insert(INSERT, str(p)  )
        else:
            txtScrolled.insert(INSERT, str(p) + " , ")
    txtScrolled.insert(INSERT, '\n')

    global checkListBinary
    checkListBinary = []
    # binarye çevirme( yine string şeklinde çeviriyor)
    for j in checkList:
        binary = ('{0:0' + str(k) + 'b}').format(j)
        checkListBinary.append(binary)
    txtScrolled.insert(INSERT, emoji1 + "1s position in the data binary  " + emoji2 + '  ')
    for p in checkListBinary:
        if checkListBinary[-1]==p:
            txtScrolled.insert(INSERT, str(p))
        else:
            txtScrolled.insert(INSERT, str(p) + " , ")
    txtScrolled.insert(INSERT, '\n')
    global paritybits
    paritybits = []
    output1 = int('0', 2)
    # output= 0'ın ikili tabanda yazımı
    # xor işleminde etkisiz eleman 0'dır
    for j in checkListBinary:
        output = int(j, 2) ^ output1
        output1 = output
        paritybits = ('{0:0' + str(k) + 'b}').format(output)
    txtScrolled.insert(INSERT, emoji1 + 'parity bits of the data  ' + emoji2 + '  ' + paritybits)
    txtScrolled.insert(INSERT, '\n')

    # parity biti integerdır
    # parity bitlerini hamming code'a ekleme

    j = 0
    paritybits = list(paritybits)
    paritybits.reverse()
    for sayi in paritybits:
        if pow(2, j) < m + k:
            word.pop(length - pow(2, j))
            word.insert((length - pow(2, j)), sayi)
            j += 1
        else:
            break
    global labelOutput
    global labelPositions
    if k == 3:
        labelOutput = Label(window)
        labelOutput.place(x=820, y=220)
        labelPositions = Label(window)
        labelPositions.place(x=820, y=200)
    elif k == 4:
        labelOutput = Label(window)
        labelOutput.place(x=630, y=220)
        labelPositions = Label(window)
        labelPositions.place(x=630, y=200)
    elif k == 5:
        labelOutput = Label(window)
        labelOutput.place(x=290, y=220)
        labelPositions = Label(window)
        labelPositions.place(x=290, y=200)
    datacount = m
    paritycount = k
    for i in range(0, length):
        if length - (i * 1) in numbers:
            textbox_positions = Text(labelPositions, height=1, width=3, fg="red")
            textbox_positions.insert('end', 'P' + str(paritycount))
            textbox_output = Text(labelOutput, height=1, width=3, fg="red")
            textbox_output.insert('end', word[i])
            paritycount -= 1
        else:
            textbox_positions = Text(labelPositions, height=1, width=3, fg="black")
            textbox_positions.insert('end', 'D' + str(datacount))
            textbox_output = Text(labelOutput, height=1, width=3)
            textbox_output.insert('end', word[i])
            datacount -= 1
        textbox_output.config(state='disabled')
        textbox_output.pack(side=LEFT, padx=5)
        textbox_positions.config(state='disabled')
        textbox_positions.pack(side=LEFT, padx=5)

    labelBitSelect = Label(window, text="DO YOU WANNA GENERATE A BIT ERROR?")
    labelBitSelect.place(x=50, y=50)

    global textError
    textError = Entry(window, width=4, fg="BLACK", bg="White")
    textError.config(state=NORMAL)
    textError.place(x=50, y=70)
    btnError = Button(window, text="ERROR", command=error, bg="#8CC0DE", fg="black")
    btnError.place(x=80, y=70)
    global labelOr
    labelOr = Label(window, text="OR")
    labelOr.place(x=150, y=70)
    btnrandom = Button(window, text="RANDOM", command=randomError, bg="#8CC0DE", fg="black")
    btnrandom.place(x=200, y=70)


def error():
    global labelError
    labelError = Label(window)
    labelError.place(x=10, y=300)
    errorbit = textError.get()
    if int(errorbit)>length:
        messagebox.showinfo("alert", "please enter a number smaller than the sum of the data length and parity bits")
    else:
        txtScrolled.insert(INSERT, emoji1 + 'the location of the error bit  ' + emoji2 + '  ' + errorbit)
        txtScrolled.insert(INSERT, '\n')
        errorbit = int(errorbit)
        if errorbit in numbers:
            txtScrolled.insert(INSERT, emoji1 + 'the error bit was not changed because it is the parity bit')
            txtScrolled.insert(INSERT, '\n')
            pass
        else:
            if word[length - errorbit] == 1:
                txtScrolled.insert(INSERT, emoji1 + 'the bit at the error bit location has been changed from 1 to 0')
                txtScrolled.insert(INSERT, '\n')
                word.pop(length - errorbit)
                word.insert((length - errorbit), 0)

            else:
                txtScrolled.insert(INSERT, emoji1 + 'the bit at the error bit location has been changed from 0 to 1')
                txtScrolled.insert(INSERT, '\n')
                word.pop(length - errorbit)
                word.insert((length - errorbit), 1)

        global labelError_positions
        labelError_positions = Label(window)
        labelError_positions.place(x=10, y=280)

        datacount = m
        paritycount = k
        for i in range(0, length):
            if length - i in numbers:
                text_boxOc = Text(labelError_positions, height=1, width=3, fg="red")
                text_boxOc.insert('end', 'P' + str(paritycount))
                paritycount -= 1
            else:
                text_boxOc = Text(labelError_positions, height=1, width=3, fg="black")
                text_boxOc.insert('end', 'D' + str(datacount))
                datacount -= 1
            text_boxOc.config(state='disabled')
            text_boxOc.pack(side=LEFT, padx=5)

        for i in range(0, length):
            if i == length - errorbit:
                text_box = Text(labelError, height=1, width=3, fg="black", bg="green")
                text_box.insert('end', word[i])
            else:
                text_box = Text(labelError, height=1, width=3)
                text_box.insert('end', word[i])
            text_box.config(state='disabled')
            text_box.pack(side=LEFT, padx=5)

        correctingCode(errorbit)


def randomError():
    global labelError
    labelError = Label(window)

    labelError.place(x=10, y=300)
    errorbit = random.randint(1, length)
    global labelError_positions
    labelError_positions = Label(window)
    labelError_positions.place(x=10, y=280)

    datacount = m
    paritycount = k
    for i in range(0, length):
        if length - i in numbers:
            text_boxOc = Text(labelError_positions, height=1, width=3, fg="red")
            text_boxOc.insert('end', 'P' + str(paritycount))
            paritycount -= 1
        else:
            text_boxOc = Text(labelError_positions, height=1, width=3, fg="black")
            text_boxOc.insert('end', 'D' + str(datacount))
            datacount -= 1
        text_boxOc.config(state='disabled')
        text_boxOc.pack(side=LEFT, padx=5)

    if errorbit in numbers:
        txtScrolled.insert(INSERT, emoji1 + 'the error bit was not changed because it is the parity bit')
        txtScrolled.insert(INSERT, '\n')
        pass
    else:
        if word[length - errorbit] == 1:
            txtScrolled.insert(INSERT, emoji1 + 'the bit at the error bit location has been changed from 1 to 0')
            txtScrolled.insert(INSERT, '\n')
            word.pop(length - errorbit)
            word.insert((length - errorbit), 0)
        elif word[length - errorbit] == 0:
            txtScrolled.insert(INSERT, emoji1 + 'the bit at the error bit location has been changed from 0 to 1')
            txtScrolled.insert(INSERT, '\n')
            word.pop(length - errorbit)
            word.insert((length - errorbit), 1)

    for i in range(0, length):
        if i == length - errorbit:
            text_box = Text(labelError, height=1, width=3, fg="black", bg="green")
            text_box.insert('end', word[i])
        else:
            text_box = Text(labelError, height=1, width=3)
            text_box.insert('end', word[i])
        text_box.config(state='disabled')
        text_box.pack(side=LEFT, padx=5)

    correctingCode(errorbit)


def correctingCode(errorbit):
    newcheckList = []
    for i in range(0, length):
        if (length - i) in numbers:
            pass
        else:
            if word[i] == 1:
                newcheckList.append(length - i)
            else:
                pass
    # binarye çevirme( yine string şeklinde çeviriyor)
    txtScrolled.insert(INSERT, emoji1 + "the position of the 1s in the new data  " + emoji2 + '  ')
    for p in newcheckList:
        if newcheckList[-1]==p:
            txtScrolled.insert(INSERT, str(p))
        else:
            txtScrolled.insert(INSERT, str(p) + " , ")
    txtScrolled.insert(INSERT, '\n')

    newcheckListBinary = []
    key = k
    for j in newcheckList:
        binary = ('{0:0' + str(key) + 'b}').format(j)
        newcheckListBinary.append(binary)
    txtScrolled.insert(INSERT, emoji1 + "the position of the 1s in the new data binary  " + emoji2 + '  ')
    for p in newcheckListBinary:
        if newcheckListBinary[-1] == p:
            txtScrolled.insert(INSERT, str(p))
        else:
            txtScrolled.insert(INSERT, str(p) + " , ")
    txtScrolled.insert(INSERT, '\n')

    parityBit = ''.join(str(i) for i in paritybits)
    parityBit = parityBit[::-1]
    parityBit = int(parityBit, 2)
    output1 = int('0', 2)

    binary = ('{0:0' + str(k) + 'b}').format(parityBit)
    newcheckListBinary.append(binary)
    for j in newcheckListBinary:
        output = int(j, 2) ^ output1
        output1 = output
        bitError = ('{0:0' + str(k) + 'b}').format(output)
    txtScrolled.insert(INSERT, emoji1 + "error bit location binary  " + emoji2 + '  ' + bitError)
    txtScrolled.insert(INSERT, '\n')

    bitError = int(bitError, 2)

    txtScrolled.insert(INSERT, emoji1 + "error bit location decimal  " + emoji2 + '  ' + str(bitError))
    txtScrolled.insert(INSERT, '\n')

    if errorbit in numbers:
        pass
    else:
        if word[length - errorbit] == 1:
            word[length - bitError] = 0
        else:
            word[length - bitError] = 1
    global labelCorrect
    global labelCorrect_positions
    if k == 3:
        labelCorrect = Label(window)
        labelCorrect.place(x=820, y=400)
        labelCorrect_positions = Label(window)
        labelCorrect_positions.place(x=820, y=380)
    elif k == 4:
        labelCorrect = Label(window)
        labelCorrect.place(x=630, y=400)
        labelCorrect_positions = Label(window)
        labelCorrect_positions.place(x=630, y=380)
    elif k == 5:
        labelCorrect = Label(window)
        labelCorrect.place(x=290, y=400)
        labelCorrect_positions = Label(window)
        labelCorrect_positions.place(x=290, y=380)

    datacount = length - k
    paritycount = k
    for i in range(0, length):
        if length - i in numbers:
            text_boxOc = Text(labelCorrect_positions, height=1, width=3, fg="red")
            text_boxOc.insert('end', 'P' + str(paritycount))
            paritycount -= 1
        else:
            text_boxOc = Text(labelCorrect_positions, height=1, width=3, fg="black")
            text_boxOc.insert('end', 'D' + str(datacount))
            datacount -= 1
        text_boxOc.config(state='disabled')
        text_boxOc.pack(side=LEFT, padx=5)

    for i in range(0, length):
        if i == length - bitError:
            text_boxO = Text(labelCorrect, height=1, width=3, fg="black", bg="green")
            text_boxO.insert('end', word[i])
        else:
            text_boxO = Text(labelCorrect, height=1, width=3, fg="black")
            text_boxO.insert('end', word[i])

        text_boxO.config(state='disabled')
        text_boxO.pack(side=LEFT, padx=5)


def restart():
    txtScrolled.delete(1.0, END)
    text.delete(0, END)
    labelData.destroy()
    labelOutput.destroy()
    labelPositions.destroy()
    labelError_positions.destroy()
    labelError.destroy()
    labelCorrect.destroy()
    labelCorrect_positions.destroy()


def calculate():
    d = text.get()
    if (d):
        hammingCodeError(d)
    else:
        messagebox.showinfo("alert", "enter a data or create randomly")


def Main():
    # frame tanımlama
    menubar = Menu(window)
    frame1 = Frame(window)
    frame1.pack(side=TOP, fill=X)
    frame2 = Frame(window)
    frame2.pack(side=BOTTOM, fill=X)

    # memubar tanımlama
    menu1 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="MENU", menu=menu1)
    menu1.add_command(label="RESTART", command=restart)
    menu1.add_command(label="EXIT", command=exit)
    window.config(menu=menubar)

    buttonCalculate = Button(window, text="CALCULATE", command=calculate, bg="#8CC0DE", fg="black", width=9, height=2)
    buttonCalculate.place(x=430, y=90)

    labelBitSelect = Label(window, text="DO YOU WANNA CREATE A RANDOM DATA? PLEASE SELECT SIZE")
    labelBitSelect.place(x=700, y=50)

    button4Bit = Button(window, text="4 Bit", command=Bit4, bg="#8CC0DE", fg="black", width=9, height=2)
    button4Bit.place(x=700, y=80)

    button8Bit = Button(window, text="8 Bit", command=Bit8, bg="#8CC0DE", fg="black", width=9, height=2)
    button8Bit.place(x=800, y=80)

    button16Bit = Button(window, text="16 Bit", command=Bit16, bg="#8CC0DE", fg="black", width=9, height=2)
    button16Bit.place(x=900, y=80)

    # girdi bilgisi
    global text
    text = Entry(window, width=30, fg="BLACK", bg="White")
    text.config(state=NORMAL)
    text.place(x=381, y=55)

    # frame 2 -> grid
    # frame 1 -> packL
    global txtScrolled
    txtScrolled = scrolledtext.ScrolledText(frame2, width=1000, height=10, font=("Roboto", 11), bg="#FFD9C0",fg="black")
    txtScrolled.grid(column=0, row=0)
    window.mainloop()


def Bit4():
    liste = []
    for i in range(0, 4):
        a = random.randint(0, 1)
        liste.append(a)
    liste = ''.join(str(i) for i in liste)
    hammingCodeError(liste)


def Bit8():
    liste = []
    for i in range(0, 8):
        a = random.randint(0, 1)
        liste.append(a)
    liste = ''.join(str(i) for i in liste)
    hammingCodeError(liste)


def Bit16():
    liste = []
    for i in range(0, 16):
        a = random.randint(0, 1)
        liste.append(a)
    liste = ''.join(str(i) for i in liste)
    hammingCodeError(liste)


if __name__ == "__main__":
    Main()