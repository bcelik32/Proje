import serial
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from random import randint , choice
from tkinter import messagebox
from time import sleep
import Proje
import serial
import time
import tkinter as tk
import threading
import continuous_threading as ct
dizi = [] 
ser = serial.Serial('COM6', 9800, timeout=1)
serioku=ser.readline()
sleep(2)

_debug = True # False to eliminate debug printing from callback functions.

#değişkenler#

isitici_is = False
sogutucu_is = False
cati_is = False
su_is = False


def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1 , sure , sicaklik
    _top1 = root
    _w1 = Proje.Sera_Programi(_top1)
    root.mainloop()


def sogukfank(*args):
    global sogutucu_is
    sogutucu_is = False
    print("Soğutucu Fan Kapandı")

def sogukfana(*args):
    global cati_is
    global isitici_is
    global sogutucu_is

    if isitici_is == True:
        messagebox.showinfo("", "Isıtıcı Fan Açıktır Lütfen Isıtıcı Fanı Kapatınız")
    elif cati_is == True:
        messagebox.showinfo("", "Çatı Açıktır Lütfen Çatı Kapatınız")
    else:
        sogutucu_is = True
        print("Soğutucu Fan Açıldı")

def sula(*args):
    global su_is
    su_is = True
    sure = _w1.Süreİnput.get()
    sure = int(sure)
    print("Sulama Başladı")
    sleep(sure)
    print("Sulama Bitti")
    su_is = False

def catia(*args):
    global cati_is
    global isitici_is
    global sogutucu_is

    if isitici_is == True or sogutucu_is == True:
        messagebox.showinfo("", "Fan Açıktır Lütfen Fanı Kapatınız")
    else:
        ser.write(b"A")   # send a byte
        cati_is = True
        print("Çatı Açıldı")
    
def catik(*args):
    global cati_is
    ser.write(b"B")   # send a byte
    cati_is = False
    print("Çatı Kapandı")

def isifana(*args):
    global cati_is
    global isitici_is
    global sogutucu_is
    if sogutucu_is == True:
        messagebox.showinfo("", "Soğutucu Fan Açıktır Lütfen Soğutucu Fanı Kapatınız")
    elif cati_is == True:
        messagebox.showinfo("", "Çatı Açıktır Lütfen Çatı Kapatınız")
    else:
        isitici_is = True
        print("Isı Fan Açıldı")
    
def isifank(*args):
    global isitici_is
    isitici_is = False
    print("Isı Fan Kapandı")

def degis(*args):
    dizi.append(serioku) # seri porttan okunan veriyi diziye ekle
    _w1.DeğişSıc.configure(text=serioku)
    dizi.clear()
        
t1 = ct.PeriodicThread(0.1,degis) # readSerial fonksiyonunu periyodik olarak çalıştır






if __name__ == '__main__':
    Proje.start_up()

t1.start()
ser.close()

