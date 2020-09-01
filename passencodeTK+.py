# ---> Please read the requirements     <---#
# --->                                  <---#
# ---> (In the same folder)             <---#
# ---> 1) A csv file named 'pwencodeDB' <---#
# ---> 1.1) column 1: web               <---#
# ---> 1.2) column 2: login             <---#
# ---> 1.3) column 3: pass              <---#


# Importing libs. #

import csv
from tkinter import *


# Defining value

return_value = "The program has correctly started; Waiting for command:"


# Importing font. #
large_font = ('Verdana',20)
medium_font = ('Verdana',15)


# Counting rows in csv file. #

with open("pwencodeDB.csv","r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)

def exit_funct():
    window.destroy()

def exit_answer():
    global answer_pop
    answer_pop.destroy()

def encode_process():
    pw = masterentry.get()
    to_encode = ptextentry.get()
    web_ = webentry.get()
    urs = ursentry.get()


# Modifying master password to 16 character. #
    if len(pw) < 16:
        j = 0
        while len(pw) != 16:
        
            pw = pw + pw[j]
            j = j + 1

    elif len(pw) > 16:
        pw = pw[:16]


# Tranfering master to multiplier. #
    key = 1
    for letters in pw:
        
# Lower letters. #
        if letters == "a":
            key = key * 5.4
        elif letters == "b":
            key = key * 8.3
        elif letters == "c":
            key = key * 6.7
        elif letters == "d":
            key = key * 2.1
        elif letters == "e":
            key = key * 5.5
        elif letters == "f":
            key = key * 8.9
        elif letters == "g":
            key = key * 8.2
        elif letters == "h":
            key = key * 5.6
        elif letters == "i":
            key = key * 9.7
        elif letters == "j":
            key = key * 6.1
        elif letters == "k":
            key = key * 1.9
        elif letters == "l":
            key = key * 8.4
        elif letters == "m":
            key = key * 5.8
        elif letters == "n":
            key = key * 6.0
        elif letters == "o":
            key = key * 6.8
        elif letters == "p":
            key = key * 9.3
        elif letters == "q":
            key = key * 7.6
        elif letters == "r":
            key = key * 5.9
        elif letters == "s":
            key = key * 9.8
        elif letters == "t":
            key = key * 5.1
        elif letters == "u":
            key = key * 9.1
        elif letters == "v":
            key = key * 7.7
        elif letters == "w":
            key = key * 8.0
        elif letters == "x":
            key = key * 9.2
        elif letters == "y":
            key = key * 1.2
        elif letters == "z":
            key = key * 3.4
        elif letters == "-":
            key = key * 5.2


# Upper letters. #
        elif letters == "A":
            key = key * 5.3
        elif letters == "B":
            key = key * 9.9
        elif letters == "C":
            key = key * 6.6
        elif letters == "D":
            key = key * 2.0
        elif letters == "E":
            key = key * 3.1
        elif letters == "F":
            key = key * 1.0
        elif letters == "G":
            key = key * 4.8
        elif letters == "H":
            key = key * 6.9
        elif letters == "I":
            key = key * 2.9
        elif letters == "J":
            key = key * 4.9
        elif letters == "K":
            key = key * 6.5
        elif letters == "L":
            key = key * 3.3
        elif letters == "M":
            key = key * 3.2
        elif letters == "N":
            key = key * 6.2
        elif letters == "O":
            key = key * 9.5
        elif letters == "P":
            key = key * 4.6
        elif letters == "Q":
            key = key * 8.6
        elif letters == "R":
            key = key * 4.1
        elif letters == "S":
            key = key * 8.7
        elif letters == "T":
            key = key * 3.8
        elif letters == "U":
            key = key * 4.4
        elif letters == "V":
            key = key * 3.7
        elif letters == "W":
            key = key * 2.5
        elif letters == "X":
            key = key * 4.0
        elif letters == "Y":
            key = key * 3.0
        elif letters == "Z":
            key = key * 6.3

# Numbers. #
        elif letters == "1":
            key = key * 1.6
        elif letters == "2":
            key = key * 8.5
        elif letters == "3":
            key = key * 7.5
        elif letters == "4":
            key = key * 2.2
        elif letters == "5":
            key = key * 1.7
        elif letters == "6":
            key = key * 4.2
        elif letters == "7":
            key = key * 8.1
        elif letters == "8":
            key = key * 7.4
        elif letters == "9":
            key = key * 3.6
        elif letters == "0":
            key = key * 4.5

# Special character. #
        elif letters == "-":
            key = key * 5.2
        elif letters == "!":
            key = key * 9.6
        elif letters == "@":
            key = key * 1.8
        elif letters == "?":
            key = key * 5.7
        elif letters == "%":
            key = key * 3.5

    key1 = round(key)
    

# Transfering plain text to encoded text. #
    key = ""

    for letters in to_encode:
        

# Lower character. #

        if letters == "a":
            key = key + str(54 * key1) + "/"
        elif letters == "b":
            key = key + str(83 * key1) + "/"
        elif letters == "c":
            key = key + str(67 * key1) + "/"
        elif letters == "d":
            key = key + str(21 * key1) + "/"
        elif letters == "e":
            key = key + str(55 * key1) + "/"
        elif letters == "f":
            key = key + str(89 * key1) + "/"
        elif letters == "g":
            key = key + str(82 * key1) + "/"
        elif letters == "h":
            key = key + str(56 * key1) + "/"
        elif letters == "i":
            key = key + str(97 * key1) + "/"
        elif letters == "j":
            key = key + str(61 * key1) + "/"
        elif letters == "k":
            key = key + str(19 * key1) + "/"
        elif letters == "l":
            key = key + str(84 * key1) + "/"
        elif letters == "m":
            key = key + str(58 * key1) + "/"
        elif letters == "n":
            key = key + str(60 * key1) + "/"
        elif letters == "o":
            key = key + str(68 * key1) + "/"
        elif letters == "p":
            key = key + str(93 * key1) + "/"
        elif letters == "q":
            key = key + str(76 * key1) + "/"
        elif letters == "r":
            key = key + str(59 * key1) + "/"
        elif letters == "s":
            key = key + str(98 * key1) + "/"
        elif letters == "t":
            key = key + str(51 * key1) + "/"
        elif letters == "u":
            key = key + str(91 * key1) + "/"
        elif letters == "v":
            key = key + str(77 * key1) + "/"
        elif letters == "w":
            key = key + str(80 * key1) + "/"
        elif letters == "x":
            key = key + str(92 * key1) + "/"
        elif letters == "y":
            key = key + str(12 * key1) + "/"
        elif letters == "z":
            key = key + str(34 * key1) + "/"


# Upper character. #
        if letters == "A":
            key = key + str(53 * key1) + "/"
        elif letters == "B":
            key = key + str(99 * key1) + "/"
        elif letters == "C":
            key = key + str(66 * key1) + "/"
        elif letters == "D":
            key = key + str(20 * key1) + "/"
        elif letters == "E":
            key = key + str(31 * key1) + "/"
        elif letters == "F":
            key = key + str(10 * key1) + "/"
        elif letters == "G":
            key = key + str(48 * key1) + "/"
        elif letters == "H":
            key = key + str(69 * key1) + "/"
        elif letters == "I":
            key = key + str(29 * key1) + "/"
        elif letters == "J":
            key = key + str(49 * key1) + "/"
        elif letters == "K":
            key = key + str(65 * key1) + "/"
        elif letters == "L":
            key = key + str(33 * key1) + "/"
        elif letters == "M":
            key = key + str(32 * key1) + "/"
        elif letters == "N":
            key = key + str(62 * key1) + "/"
        elif letters == "O":
            key = key + str(95 * key1) + "/"
        elif letters == "P":
            key = key + str(46 * key1) + "/"
        elif letters == "Q":
            key = key + str(86 * key1) + "/"
        elif letters == "R":
            key = key + str(41 * key1) + "/"
        elif letters == "S":
            key = key + str(87 * key1) + "/"
        elif letters == "T":
            key = key + str(38 * key1) + "/"
        elif letters == "U":
            key = key + str(44 * key1) + "/"
        elif letters == "V":
            key = key + str(37 * key1) + "/"
        elif letters == "W":
            key = key + str(25 * key1) + "/"
        elif letters == "X":
            key = key + str(40 * key1) + "/"
        elif letters == "Y":
            key = key + str(30 * key1) + "/"
        elif letters == "Z":
            key = key + str(63 * key1) + "/"
        
        
        
        elif letters == "-":
            key = key + str(52 * key1) + "/"
        elif letters == "!":
            key = key + str(96 * key1) + "/"
        elif letters == "@":
            key = key + str(18 * key1) + "/"
        elif letters == "?":
            key = key + str(57 * key1) + "/"
        elif letters == "%":
            key = key + str(35 * key1) + "/"

# Numbers. #
        elif letters == "1":
            key = key + str(16 * key1) + "/"
        elif letters == "2":
            key = key + str(85 * key1) + "/"
        elif letters == "3":
            key = key + str(75 * key1) + "/"
        elif letters == "4":
            key = key + str(22 * key1) + "/"
        elif letters == "5":
            key = key + str(17 * key1) + "/"
        elif letters == "6":
            key = key + str(42 * key1) + "/"
        elif letters == "7":
            key = key + str(81 * key1) + "/"
        elif letters == "8":
            key = key + str(74 * key1) + "/"
        elif letters == "9":
            key = key + str(36 * key1) + "/"
        elif letters == "0":
            key = key + str(45 * key1) + "/"


# Writing into the csv file. #

    f = open('pwencodeDB.csv', 'a', newline='')
    with f as csvfile:
        fieldnames = ['web', 'login', "pass"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'web': web_, 'login': urs, "pass": key})


    return_value = "The entry has been saved"   
    status_bar = Label(window, text=return_value, relief=SUNKEN, bd=3, bg ='white', font=('Verdana',12), justify='left')     
    status_bar.place(x=20, y=505, width=780, height=90)



def decode_process():
    Process_decode = False
    a = 0
    Is_found = False
    key = 1
    pw = masterentry.get()
    queryName = linkentry.get()

# Collecting information for querry. #
    with open("pwencodeDB.csv", 'r') as csvfile: 

# creating a csv reader object 

      csvreader = csv.reader(csvfile) 



# Checking all row in csv file. #

      while a < row_count:
        field = next(csvreader)
        a = a + 1

# Finding if query name exists in database. #
        if field[0] == queryName:
            row = a
            line_found = "Trouvé" + " sur la ligne " + str(row) + " du fichier CSV"

            Is_found = True  
            Process_decode = True

 
        
    if Is_found == False:
        print("Service inconnu")

    if Process_decode == True:
        a = 0
        with open("pwencodeDB.csv", 'r') as csvfile: 

# creating a csv reader object 

            csvreader = csv.reader(csvfile) 

            while a < (row):    
                field = next(csvreader)
                a = a + 1
        brut = field[2]


# Asking for the master to decode info. #

    if Process_decode == True:

# Input and modifying master password to 16 character. #


        if len(pw) < 16:
            j = 0
        while len(pw) != 16:
        
            pw = pw + pw[j]
            j = j + 1

    elif len(pw) > 16:
        pw = pw[:16]


# Tranfering master to decode.multiplier. #

    key = 1
    for letters in pw:
        
# Lower letters. #
        if letters == "a":
            key = key * 5.4
        elif letters == "b":
            key = key * 8.3
        elif letters == "c":
            key = key * 6.7
        elif letters == "d":
            key = key * 2.1
        elif letters == "e":
            key = key * 5.5
        elif letters == "f":
            key = key * 8.9
        elif letters == "g":
            key = key * 8.2
        elif letters == "h":
            key = key * 5.6
        elif letters == "i":
            key = key * 9.7
        elif letters == "j":
            key = key * 6.1
        elif letters == "k":
            key = key * 1.9
        elif letters == "l":
            key = key * 8.4
        elif letters == "m":
            key = key * 5.8
        elif letters == "n":
            key = key * 6.0
        elif letters == "o":
            key = key * 6.8
        elif letters == "p":
            key = key * 9.3
        elif letters == "q":
            key = key * 7.6
        elif letters == "r":
            key = key * 5.9
        elif letters == "s":
            key = key * 9.8
        elif letters == "t":
            key = key * 5.1
        elif letters == "u":
            key = key * 9.1
        elif letters == "v":
            key = key * 7.7
        elif letters == "w":
            key = key * 8.0
        elif letters == "x":
            key = key * 9.2
        elif letters == "y":
            key = key * 1.2
        elif letters == "z":
            key = key * 3.4
        elif letters == "-":
            key = key * 5.2


# Upper letters. #
        elif letters == "A":
            key = key * 5.3
        elif letters == "B":
            key = key * 9.9
        elif letters == "C":
            key = key * 6.6
        elif letters == "D":
            key = key * 2.0
        elif letters == "E":
            key = key * 3.1
        elif letters == "F":
            key = key * 1.0
        elif letters == "G":
            key = key * 4.8
        elif letters == "H":
            key = key * 6.9
        elif letters == "I":
            key = key * 2.9
        elif letters == "J":
            key = key * 4.9
        elif letters == "K":
            key = key * 6.5
        elif letters == "L":
            key = key * 3.3
        elif letters == "M":
            key = key * 3.2
        elif letters == "N":
            key = key * 6.2
        elif letters == "O":
            key = key * 9.5
        elif letters == "P":
            key = key * 4.6
        elif letters == "Q":
            key = key * 8.6
        elif letters == "R":
            key = key * 4.1
        elif letters == "S":
            key = key * 8.7
        elif letters == "T":
            key = key * 3.8
        elif letters == "U":
            key = key * 4.4
        elif letters == "V":
            key = key * 3.7
        elif letters == "W":
            key = key * 2.5
        elif letters == "X":
            key = key * 4.0
        elif letters == "Y":
            key = key * 3.0
        elif letters == "Z":
            key = key * 6.3

# Special character. #
        elif letters == "-":
            key = key * 5.2
        elif letters == "!":
            key = key * 9.6
        elif letters == "@":
            key = key * 1.8
        elif letters == "?":
            key = key * 5.7
        elif letters == "%":
            key = key * 3.5


# Numbers. #
        elif letters == "1":
            key = key * 1.6
        elif letters == "2":
            key = key * 8.5
        elif letters == "3":
            key = key * 7.5
        elif letters == "4":
            key = key * 2.2
        elif letters == "5":
            key = key * 1.7
        elif letters == "6":
            key = key * 4.2
        elif letters == "7":
            key = key * 8.1
        elif letters == "8":
            key = key * 7.4
        elif letters == "9":
            key = key * 3.6
        elif letters == "0":
            key = key * 4.5

    key = round(key)


# Decoding encoded text with key. #

    string = field[2]
    passw = ""
    while string != "":
        pos = string.find("/")
        if pos == 0:
            string = ""
        temp = string[0:pos]
        string = string[(pos + 1):]
        temp2 =int(temp) / key
        
        
# Lower characters. #
    
        if temp2 == 54:
            passw = passw + "a"
        elif temp2 == 83:
            passw = passw + "b"
        elif temp2 == 67:
            passw = passw + "c"
        elif temp2 == 21:
            passw = passw + "d"
        elif temp2 == 55:
            passw = passw + "e"
        elif temp2 == 89:
            passw = passw + "f"
        elif temp2 == 82:
            passw = passw + "g"
        elif temp2 == 56:
            passw = passw + "h"
        elif temp2 == 97:
            passw = passw + "i"
        elif temp2 == 61:
            passw = passw + "j"
        elif temp2 == 19:
            passw = passw + "k"
        elif temp2 == 84:
            passw = passw + "l"
        elif temp2 == 58:
            passw = passw + "m"
        elif temp2 == 60:
            passw = passw + "n"
        elif temp2 == 68:
            passw = passw + "o"
        elif temp2 == 93:
            passw = passw + "p"
        elif temp2 == 76:
            passw = passw + "q"
        elif temp2 == 59:
            passw = passw + "r"
        elif temp2 == 98:
            passw = passw + "s"
        elif temp2 == 51:
            passw = passw + "t"
        elif temp2 == 91:
            passw = passw + "u"
        elif temp2 == 77:
            passw = passw + "v"
        elif temp2 == 80:
            passw = passw + "w"
        elif temp2 == 92:
            passw = passw + "x"
        elif temp2 == 12:
            passw = passw + "y"
        elif temp2 == 34:
            passw = passw + "z"


# Upper characters. #

        elif temp2 == 53:
            passw = passw + "A"
        elif temp2 == 99:
            passw = passw + "B"
        elif temp2 == 66:
            passw = passw + "C"
        elif temp2 == 20:
            passw = passw + "D"
        elif temp2 == 31:
            passw = passw + "E"
        elif temp2 == 10:
            passw = passw + "F"
        elif temp2 == 48:
            passw = passw + "G"
        elif temp2 == 69:
            passw = passw + "H"
        elif temp2 == 29:
            passw = passw + "I"
        elif temp2 == 49:
            passw = passw + "J"
        elif temp2 == 65:
            passw = passw + "K"
        elif temp2 == 33:
            passw = passw + "L"
        elif temp2 == 32:
            passw = passw + "M"
        elif temp2 == 62:
            passw = passw + "N"
        elif temp2 == 95:
            passw = passw + "O"
        elif temp2 == 46:
            passw = passw + "P"
        elif temp2 == 86:
            passw = passw + "Q"
        elif temp2 == 41:
            passw = passw + "R"
        elif temp2 == 87:
            passw = passw + "S"
        elif temp2 == 38:
            passw = passw + "T"
        elif temp2 == 44:
            passw = passw + "U"
        elif temp2 == 37:
            passw = passw + "V"
        elif temp2 == 25:
            passw = passw + "W"
        elif temp2 == 40:
            passw = passw + "X"
        elif temp2 == 30:
            passw = passw + "Y"
        elif temp2 == 63:
            passw = passw + "Z"
        
# Special characters. #

        elif temp2 == 52:
            passw = passw + "-"
        elif temp2 == 96:
            passw = passw + "!"
        elif temp2 == 18:
            passw = passw + "@"
        elif temp2 == 57:
            passw = passw + "?"
        elif temp2 == 35:
            passw = passw + "%"

# Numbers. #

        elif temp2 == 16:
            passw = passw + "1"
        elif temp2 == 85:
            passw = passw + "2"
        elif temp2 == 75:
            passw = passw + "3"
        elif temp2 == 22:
            passw = passw + "4"
        elif temp2 == 17:
            passw = passw + "5"
        elif temp2 == 42:
            passw = passw + "6"
        elif temp2 == 81:
            passw = passw + "7"
        elif temp2 == 74:
            passw = passw + "8"
        elif temp2 == 36:
            passw = passw + "9"
        elif temp2 == 45:
            passw = passw + "0"















    final = passw





    # Creating main Window app. #
    global answer_pop
    answer_pop = Tk()
    answer_pop.title("Password")
    answer_pop.iconbitmap("pass.ico")
    answer_pop.geometry("400x300")
    answer_pop.configure(bg='black')

    linefoundlabel = Label(answer_pop, text=line_found, bg='black',font=medium_font, fg = 'orange')
    linefoundlabel.place(x=6, y=6)

    finallabel = Label(answer_pop, text=final, bg='black', font=('Verdana',30), fg ='orange')
    finallabel.place(y=120, x=6)

    okbutton = Button(answer_pop, text='OK', command=exit_answer, bg='orange', font=medium_font)
    okbutton.place(y=250, x=6)

    answer_pop.mainloop()








def init_encode():
# Master password entry $ text. #
    global masterlabel
    global masterentry
    global ptextentry
    global ptextlabel
    global webentry
    global weblabel
    global ursentry
    global urslabel
    global processbutton
    global linkentry
    global linklabel


    try:
        linkentry.winfo_ismapped()
        masterlabel.destroy()
        masterentry.destroy()
        processbutton.destroy()
        linkentry.destroy()
        linklabel.destroy()
    
    except:
        a = 0



    masterlabel = Label(window, text="Master password", font=medium_font)
    masterlabel.place(x=370, y=18)

    masterentry = Entry(window, width = 20, font=large_font)
    masterentry.place(x=370, y=50)


# Plain text entry $ text. #
    ptextlabel = Label(window, text="Password you want to encode", font=medium_font)
    ptextlabel.place(x=370, y=128)    
    
    ptextentry = Entry(window, width = 20, font=large_font)
    ptextentry.place(x=370, y=160)


# Web service entry $ text. #
    weblabel = Label(window, text="Name of the service", font=medium_font)
    weblabel.place(x=370, y=238)    
    
    webentry = Entry(window, width = 20, font=large_font)
    webentry.place(x=370, y=267)


# Username linked to service $ text. #
    urslabel = Label(window, text="Username to connect to the service", font=medium_font)
    urslabel.place(x=370, y=340)    
    
    ursentry = Entry(window, width = 20, font=large_font)
    ursentry.place(x=370, y=370)

# Process Button. #
    processbutton = Button(window, text ="Process", padx=45, pady=30, bd=4, font=('Verdana',18), command=encode_process, bg='green')
    processbutton.place(x=820, y=230)









def init_decode():
    global masterlabel
    global masterentry
    global ptextentry
    global ptextlabel
    global webentry
    global weblabel
    global ursentry
    global urslabel
    global processbutton
    global linkentry
    global linklabel


    try:
        ursentry.winfo_ismapped()
        masterlabel.destroy()
        masterentry.destroy()
        ptextentry.destroy()
        ptextlabel.destroy()
        webentry.destroy()
        weblabel.destroy()
        ursentry.destroy()
        urslabel.destroy()
        processbutton.destroy()
    
    except:
        a = 0







# Master password entry $ text. #
    masterlabel = Label(window, text="Master password", font=medium_font)
    masterlabel.place(x=370, y=18)

    masterentry = Entry(window, width = 20, font=large_font)
    masterentry.place(x=370, y=50)


# Plain text entry $ text. #
    linklabel = Label(window, text="Nom du service relié au mot de passe", font=medium_font)
    linklabel.place(x=370, y=128)    
    
    linkentry = Entry(window, width = 20, font=large_font)
    linkentry.place(x=370, y=160)


# Process Button. #
    processbutton = Button(window, text ="Process", padx=45, pady=30, bd=4, font=('Verdana',18), command=decode_process, bg='green')
    processbutton.place(x=820, y=230)







# Creating main Window app. #
window = Tk()
window.title("Password encoder")
window.iconbitmap("pass.ico")
window.geometry("1100x600")
window.configure(bg='black')

encodebutton = Button(window, text ="Encode", padx=60, pady=32, bd=6, font=large_font, command=init_encode, bg='red')
decodebutton = Button(window, text ="Decode", padx=60, pady=32, bd=6, font=large_font, command=init_decode, bg='blue')

encodebutton.place(x= 15, y=110)
decodebutton.place(x= 15, y=340)

exitbutton1 = Button(window, text ="Exit", padx=105, pady=19, command=exit_funct, bg="#dbdbdb", font=('verdana',20))
exitbutton1.place(x=810, y=504)


status_bar = Label(window, text=return_value, relief=SUNKEN, bd=3, bg ='white', font=('Verdana',12), justify='left')
status_bar.place(x=20, y=505, width=780, height=90)


window.mainloop()