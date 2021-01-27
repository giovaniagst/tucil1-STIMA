# tucil 1 :)

import re
import time

def from_file (nama_file):
    open_file = open(nama_file, 'r')
    read_file = open_file.read()
    alphabet = re.sub('[\W_]+', ' ', read_file)
    words = alphabet.split()
    return words

def permutasi (angka):
    if (len(angka) == 0):
        return []
    elif (len(angka) == 1):
        return [angka]
    else:
        list_angka = []
        for i in range (len(angka)):
            b = angka[i]
            cur_list = angka[:i] + angka[i+1:]
            for p in permutasi(cur_list):
                list_angka.append([b] + p)
        return list_angka

def adding_number (word, angka):
    total = 0
    faktor = 1
    for letter in reversed(word):
        total += faktor*int(angka[letter])
        faktor *= 10
    return total

def isNol (solusi,firstLetter_list):
    condition = True
    for i in range (len(firstLetter_list)):
        for key in solusi:
            if (key == firstLetter_list[i]):
                if (solusi[key] == '0'):
                    condition = False
                    break
    return condition


def solving (angka,words):
    # huruf pada tiap kata
    letters = []
    for kata in words:
        for i in range (len(kata)):
            letters.append(kata[i])

    letter_set = set()
    for i in range(len(letters)):
        letter_set.update(letters[i])
    letter_list = (list(letter_set))
    letter_list.sort()
    
    # pisahin soal sama jawaban
    count = 0
    for kata in words:
        count += 1

    i = count-1
    j = 0
    soal = []
    jawab = []
    while (i >= 0):
        if (i == count-1):
            jawab.insert(j,words[i])
        elif (i < count-1):
            soal.insert(j,words[i])
            j += 1
        i -= 1

    # huruf pertama tiap kata
    first_letter = []
    for kata in words:
        for i in range (len(kata)):
            if (i == 0):
                first_letter.append(kata[i])

    firstLetter_set = set()
    for i in range(len(first_letter)):
        firstLetter_set.update(first_letter[i])
    firstLetter_list = (list(firstLetter_set))
    firstLetter_list.sort()

    percobaan = 0
    for p in permutasi(angka):
        solusi = dict(zip(letter_list,p))
        total_soal = sum(adding_number(word,solusi) for word in soal)
        total_jawab = sum(adding_number(word,solusi) for word in jawab)
        nol = isNol(solusi,firstLetter_list)
        if (total_soal == total_jawab):
            if (nol == True):
                sol = solusi
        percobaan += 1
    
    printJawaban(words,sol)
    print("Jumlah percobaan : ", percobaan)

def printSoal (words):
    print('S O A L :')
    # pisahin soal sama jawaban
    count = 0
    for kata in words:
        count += 1

    i = count-1
    j = 0
    soal = []
    jawab = []
    while (i >= 0):
        if (i == count-1):
            jawab.insert(j,words[i])
        elif (i < count-1):
            soal.insert(j,words[i])
            j += 1
        i -= 1

    for kata in soal:
        print(kata)
    for kata in jawab:
        separator = len(kata)*'-' + ' +'
        print(separator)
        print(kata)
    print('\n')

def printJawaban (words,solusi):
    print("J A W A B A N :")
    # pisahin soal sama jawaban
    count = 0
    for kata in words:
        count += 1

    i = count-1
    j = 0
    soal = []
    jawab = []
    while (i >= 0):
        if (i == count-1):
            jawab.insert(j,words[i])
        elif (i < count-1):
            soal.insert(j,words[i])
            j += 1
        i -= 1

    for kata in soal:
        huruf = list(kata)
        for i in range (len(huruf)):
            for key in solusi:
                if (huruf[i] == key):
                    print(solusi[key],end='')
        print('')

    for kata in jawab:
        huruf = list(kata)
        separator = len(huruf)*'-' + ' +'
        print(separator)
        for i in range (len(huruf)):
            for key in solusi:
                if (huruf[i] == key):
                    print(solusi[key],end='')
        print('')
    print('\n')

# main
nama_file = input("masukkan nama file : ")
direct = '../test/'
words = from_file(direct+nama_file)
start_time = time.time()
angka = list('0123456789')
printSoal(words)
solving(angka,words)
print("Waktu yang dibutuhkan : %s seconds" % (time.time() - start_time)) 


        



