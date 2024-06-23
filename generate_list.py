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
    if textvalidate==1:
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

        R=int(maxvalue2/maxvalue*redvalue)
        G=int(maxvalue2/maxvalue*greenvalue)
        B=int(maxvalue2/maxvalue*bluevalue)
        redsum=0
        greensum=0
        bluesum=0
        redlength=0
        bluelength=0
        greenlength=0
        return (R,G,B)

def create_list():
    wordfile=open('words.txt','r')
    wordlist=wordfile.readlines()
    line_count = sum(1 for _ in wordlist)
    barmax=line_count/100

    if barmax<1:
        barmax=1
    wordfile.close()
    
    colorlist=open('wordcolor.txt','w',newline='')
    bar=0
    for text in wordlist:
        word= text[0:-1]
        bar=bar+1
        if bar>barmax:
            bar=0
            print('o', end='')
        try:
            (R,G,B)=GenerateColor(word)
            RGB=[word,R,G,B]
            #print (RGB)
            colorvalues=csv.writer(colorlist)
            #print (text,RGB)
            colorvalues.writerow(RGB)
        except Exception as ex:
            True
    colorlist.close()
    print ('\nConversion complete. The file wordcolor.txt contains your word list followed by RGB color values')
        
        

#main
def main():
    init()
    create_list()
    

main()

