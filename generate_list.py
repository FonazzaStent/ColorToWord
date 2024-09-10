import sys

import os
import io

import math

import csv


#init
def init():
    global c
    global rc
    global bc
    global gc
    global blue
    global red
    global green
    global lettern
    global numbersum
    global redsum
    global greensum
    global bluesum
    global redlength
    global greenlength
    global bluelength
    c=9.84
    rc=28.44
    bc=23.27
    gc=42.5
    blue=0
    red=0
    green=0
    lettern=1
    numbersum=0
    redsum=0
    greensum=0
    bluesum=0
    redlength=0
    greenlength=0
    bluelength=0  



#GenerateColor

def sine(value, letternumber):
    global blue
    blue=blue+value
    global bluelength
    bluelength=bluelength+1
    global bluesum
    bluesum=bluesum+letternumber

def triangle (value, letternumber):
    global red
    red=red+value
    global redlength
    redlength=redlength+1
    global redsum
    redsum=redsum+letternumber

def square (value, letternumber):
    global green
    green=green+value
    global greenlength
    greenlength= greenlength+1
    global greensum
    greensum=greensum+letternumber

def sine2(value, letternumber):
    global blue
    blue=blue+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern

def triangle2 (value, letternumber):
    global red
    red=red+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern    

def square2 (value, letternumber):
    global green
    green=green+value
    global lettern
    lettern=letternumber
    global numbersum
    numbersum=numbersum+lettern

    
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

def GenerateColor(text):
    global blue
    blue=0
    global red
    red=0
    global green
    green=0
    global numbersum
    global redsum
    global redlength
    global greensum
    global greenlength
    global bluesum
    global bluelength
    numbersum=0

    textvalidate=0
    length=len(text)-1
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            textvalidate=1
    if textvalidate==0:
        text="Hello"
    length=len(text)-1
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            if char=="A" or char=="a":
                triangle(int(1*rc), 1)
            if char=="B" or char=="b":
                sine (int(1*bc), 1)
            if char=="C" or char=="c":
                sine(int(2*bc), 2)
            if char=="D" or char=="d":
                sine(int(3*bc),3)
            if char=="E" or char=="e":
                square(int(1*gc),1)
            if char=="F" or char=="f":
                square(int(2*gc),2)
            if char=="G" or char=="g":
                sine(int(4*bc),4)
            if char=="H" or char=="h":
                square(int(3*gc),3)
            if char=="i" or char=="I":
                square(int(4*gc),4)
            if char=="J" or char=="j":
                sine(int(5*bc),5)
            if char=="K" or char=="k":
                triangle(int(2*rc),2)
            if char=="L" or char=="l":
                square(int(5*gc),5)
            if char=="M" or char=="m":
                triangle(int(3*rc),3)
            if char=="N" or char=="n":
                triangle(int(4*rc),4)
            if char=="O" or char=="o":
                sine(int(6*bc),6)
            if char=="P" or char=="p":
                sine(int(7*bc),7)
            if char=="Q" or char=="q":
                sine(int(8*bc),8)
            if char=="R" or char=="r":
                sine(int(9*bc),9)
            if char=="S" or char=="s":
                sine(int(10*bc),10)
            if char=="T" or char=="t":
                square(int(6*gc),6)
            if char=="U" or char=="u":
                sine(int(11*bc),11)
            if char=="V" or char=="v":
                triangle(int(5*rc),5)
            if char=="W" or char=="w":
                triangle(int(6*rc),6)
            if char=="X" or char=="x":
                triangle(int(7*rc),7)
            if char=="Y" or char=="y":
                triangle(int(8*rc),8)
            if char=="Z" or char=="z":
                triangle(int(9*rc),9)
    if bluelength>0:
        blue=int(blue/bluelength)
        bluevalue=int(blue*bluelength)
    else:
        blue=0
        bluevalue=0
    if redlength>0:
        red=int(red/redlength)
        redvalue=int(red*redlength)
    else:
        red=0
        redvalue=0
    if greenlength>0:
        green=int(green/greenlength)
        greenvalue=int(green*greenlength)
    else:
        green=0
        greenvalue=0
    RGB=[redvalue,greenvalue,bluevalue]
    RGB2=[red,green,blue]
    maxvalue=max(RGB)
    maxvalue2=max(RGB2)
    R1=int(maxvalue2/maxvalue*redvalue)
    G1=int(maxvalue2/maxvalue*greenvalue)
    B1=int(maxvalue2/maxvalue*bluevalue)



#algorithm 2
    blue=0
    red=0
    green=0
    numbersum=0
    textvalidate=0
    length=len(text)-1
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            textvalidate=1
    if textvalidate==0:
        text="Hello"
    length=len(text)
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            if char=="A" or char=="a":
                triangle2(int(1*rc), 1)
            if char=="B" or char=="b":
                sine2 (int(1*bc), 1)
            if char=="C" or char=="c":
                sine2(int(2*bc), 2)
            if char=="D" or char=="d":
                sine2(int(3*bc),3)
            if char=="E" or char=="e":
                square2(int(1*gc),1)
            if char=="F" or char=="f":
                square2(int(2*gc),2)
            if char=="G" or char=="g":
                sine2(int(4*bc),4)
            if char=="H" or char=="h":
                square2(int(3*gc),3)
            if char=="i" or char=="I":
                square2(int(4*gc),4)
            if char=="J" or char=="j":
                sine2(int(5*bc),5)
            if char=="K" or char=="k":
                triangle2(int(2*rc),2)
            if char=="L" or char=="l":
                square2(int(5*gc),5)
            if char=="M" or char=="m":
                triangle2(int(3*rc),3)
            if char=="N" or char=="n":
                triangle2(int(4*rc),4)
            if char=="O" or char=="o":
                sine2(int(6*bc),6)
            if char=="P" or char=="p":
                sine2(int(7*bc),7)
            if char=="Q" or char=="q":
                sine2(int(8*bc),8)
            if char=="R" or char=="r":
                sine2(int(9*bc),9)
            if char=="S" or char=="s":
                sine2(int(10*bc),10)
            if char=="T" or char=="t":
                square2(int(5*gc),6)
            if char=="U" or char=="u":
                sine2(int(11*bc),11)
            if char=="V" or char=="v":
                triangle2(int(5*rc),5)
            if char=="W" or char=="w":
                triangle2(int(6*rc),6)
            if char=="X" or char=="x":
                triangle2(int(7*rc),7)
            if char=="Y" or char=="y":
                triangle2(int(8*rc),8)
            if char=="Z" or char=="z":
                triangle2(int(9*rc),9)
    if bluelength>0:
        blue=int(blue/bluelength)
        blue=int(blue*bluelength)
    else:
        blue=0
    if redlength>0:
        red=int(red/redlength)
        red=int(red*redlength)
    else:
        red=0
    if greenlength>0:
        green=int(green/greenlength)
        green=int(green*greenlength)
    else:
        green=0
    RGB=[red,green,blue]
    maxvalue=max(RGB)
    if red>0:
        R=int(255/maxvalue*red)
    else:
        R=0
    if green>0:
        G=int(255/maxvalue*green)
    else:
        G=0
    if blue>0:
        B=int(255/maxvalue*blue)
    else:
        B=0
    maxredlightness=redlength*9
    maxgreenlightness=greenlength*6
    maxbluelightness=bluelength*11
    if maxredlightness>0:
        redlightness=int(100*redsum/maxredlightness)
    else:
        redlightness=0
    if maxgreenlightness>0:
        greenlightness=int(100*greensum/maxgreenlightness)
    else:
        greenlightness=0
    if maxbluelightness>0:
        bluelightness=int(100*bluesum/maxbluelightness)
    else:
        bluelightness=0
    R2=int(redlightness*R/100)
    G2=int(greenlightness*G/100)
    B2=int(bluelightness*B/100)


#algorithm 3

    blue=0
    red=0
    green=0
    numbersum=0
    textvalidate=0
    length=len(text)
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            textvalidate=1
    if textvalidate==0:
        text="Hello"
    length=len(text)
    for letters in range (0,length):
        char=text[letters]
        asciicode=ord(char)
        if (asciicode>64 and asciicode<91) or (asciicode>96 and asciicode<123):
            if char=="A" or char=="a":
                triangle(int(1*rc), 1)
            if char=="B" or char=="b":
                sine (int(1*bc), 2)
            if char=="C" or char=="c":
                sine(int(2*bc), 3)
            if char=="D" or char=="d":
                sine(int(3*bc),4)
            if char=="E" or char=="e":
                square(int(1*gc),5)
            if char=="F" or char=="f":
                square(int(2*gc),6)
            if char=="G" or char=="g":
                sine(int(4*bc),7)
            if char=="H" or char=="h":
                square(int(3*gc),8)
            if char=="i" or char=="I":
                square(int(4*gc),9)
            if char=="J" or char=="j":
                sine(int(5*bc),10)
            if char=="K" or char=="k":
                triangle(int(2*rc),11)
            if char=="L" or char=="l":
                square(int(5*gc),12)
            if char=="M" or char=="m":
                triangle(int(3*rc),13)
            if char=="N" or char=="n":
                triangle(int(4*rc),14)
            if char=="O" or char=="o":
                sine(int(6*bc),15)
            if char=="P" or char=="p":
                sine(int(7*bc),16)
            if char=="Q" or char=="q":
                sine(int(8*bc),17)
            if char=="R" or char=="r":
                sine(int(9*bc),18)
            if char=="S" or char=="s":
                sine(int(10*bc),19)
            if char=="T" or char=="t":
                square(int(5*gc),20)
            if char=="U" or char=="u":
                sine(int(11*bc),21)
            if char=="V" or char=="v":
                triangle(int(5*rc),22)
            if char=="W" or char=="w":
                triangle(int(6*rc),23)
            if char=="X" or char=="x":
                triangle(int(7*rc),24)
            if char=="Y" or char=="y":
                triangle(int(8*rc),25)
            if char=="Z" or char=="z":
                triangle(int(9*rc),26)

    if bluelength>0:
        blue=int(blue/bluelength)
        blue=int(blue*bluelength)
    else:
        blue=0
    if redlength>0:
        red=int(red/redlength)
        red=int(red*redlength)
    else:
        red=0
    if greenlength>0:
        green=int(green/greenlength)
        green=int(green*greenlength)
    else:
        green=0
    RGB=[red,green,blue]
    maxvalue=max(RGB)
    R3=int(255/maxvalue*red)
    G3=int(255/maxvalue*green)
    B3=int(255/maxvalue*blue)

    redsum=0
    greensum=0
    bluesum=0
    redlength=0
    bluelength=0
    greenlength=0
    return (R1,G1,B1,R2,G2,B2,R3,G3,B3)

def create_list():
    wordfile=open('words.txt','r')
    wordlist=wordfile.readlines()
    line_count = sum(1 for _ in wordlist)
    barmax=line_count/100

    if barmax<1:
        barmax=1
    wordfile.close()
    
    colorlist=open('wordcolor.txt','w',newline='')
    colorlist2=open('wordcolor2.txt','w',newline='')
    colorlist3=open('wordcolor3.txt','w',newline='')
    bar=0
    for text in wordlist:
        word= text[0:-1]
        bar=bar+1
        if bar>barmax:
            bar=0
            print('o', end='')
        try:
            (R1,G1,B1,R2,G2,B2,R3,G3,B3)=GenerateColor(word)
            RGB=[word,R1,G1,B1]
            RGB2=[word,R2,G2,B2]
            RGB3=[word,R3,G3,B3]
            #print (RGB)
            colorvalues=csv.writer(colorlist)
            colorvalues2=csv.writer(colorlist2)
            colorvalues3=csv.writer(colorlist3)
            #print (text,RGB)
            colorvalues.writerow(RGB)
            colorvalues2.writerow(RGB2)
            colorvalues3.writerow(RGB3)
        except Exception as ex:
            print (ex)
            True
    colorlist.close()
    colorlist2.close()
    colorlist3.close()
    print ('\nConversion complete. The file wordcolor.txt contains your word list followed by RGB color values')
        
        

#main
def main():
    init()
    create_list()
    

main()

