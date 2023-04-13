#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Mar 28, 2023 08:20:38 PM +03  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import Proje_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='TkDefaultFont')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    _style_code_ran = 1

class Sera_Programi:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("653x470+323+95")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1,  1)
        top.title("Sera Programi")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        _style_code()
        self.OkulName = ttk.Label(self.top)
        self.OkulName.place(relx=0.368, rely=-0.021, height=41, width=166)
        self.OkulName.configure(background="#d9d9d9")
        self.OkulName.configure(foreground="#000000")
        self.OkulName.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 13")
        self.OkulName.configure(relief="flat")
        self.OkulName.configure(anchor='w')
        self.OkulName.configure(justify='center')
        self.OkulName.configure(text='''Menderes Anadolu Lisesi''')
        self.OkulName.configure(compound='center')
        self.SabitSıc = tk.Label(self.top)
        self.SabitSıc.place(relx=0.031, rely=0.134, height=22, width=54)
        self.SabitSıc.configure(activebackground="#f9f9f9")
        self.SabitSıc.configure(anchor='w')
        self.SabitSıc.configure(background="#d9d9d9")
        self.SabitSıc.configure(compound='left')
        self.SabitSıc.configure(disabledforeground="#a3a3a3")
        self.SabitSıc.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.SabitSıc.configure(foreground="#000000")
        self.SabitSıc.configure(highlightbackground="#d9d9d9")
        self.SabitSıc.configure(highlightcolor="black")
        self.SabitSıc.configure(text='''Sıcaklık:''')
        self.SeraNem = tk.Label(self.top)
        self.SeraNem.place(relx=0.031, rely=0.179, height=22, width=74)
        self.SeraNem.configure(activebackground="#f9f9f9")
        self.SeraNem.configure(anchor='w')
        self.SeraNem.configure(background="#d9d9d9")
        self.SeraNem.configure(compound='left')
        self.SeraNem.configure(disabledforeground="#a3a3a3")
        self.SeraNem.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.SeraNem.configure(foreground="#000000")
        self.SeraNem.configure(highlightbackground="#d9d9d9")
        self.SeraNem.configure(highlightcolor="black")
        self.SeraNem.configure(text='''Sera Nemi:''')
        self.ToprakNem = tk.Label(self.top)
        self.ToprakNem.place(relx=0.031, rely=0.221, height=22, width=94)
        self.ToprakNem.configure(activebackground="#f9f9f9")
        self.ToprakNem.configure(anchor='w')
        self.ToprakNem.configure(background="#d9d9d9")
        self.ToprakNem.configure(compound='left')
        self.ToprakNem.configure(disabledforeground="#a3a3a3")
        self.ToprakNem.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.ToprakNem.configure(foreground="#000000")
        self.ToprakNem.configure(highlightbackground="#d9d9d9")
        self.ToprakNem.configure(highlightcolor="black")
        self.ToprakNem.configure(text='''Toprak Nemi:''')
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.HavaDurum = tk.Label(self.top)
        self.HavaDurum.place(relx=0.031, rely=0.266, height=23, width=94)
        self.HavaDurum.configure(activebackground="#f9f9f9")
        self.HavaDurum.configure(anchor='w')
        self.HavaDurum.configure(background="#d9d9d9")
        self.HavaDurum.configure(compound='left')
        self.HavaDurum.configure(disabledforeground="#a3a3a3")
        self.HavaDurum.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.HavaDurum.configure(foreground="#000000")
        self.HavaDurum.configure(highlightbackground="#d9d9d9")
        self.HavaDurum.configure(highlightcolor="black")
        self.HavaDurum.configure(text='''Hava Durumu:''')
        self.IsıFanA = tk.Button(self.top)
        self.IsıFanA.place(relx=0.674, rely=0.134, height=24, width=47)
        self.IsıFanA.configure(activebackground="beige")
        self.IsıFanA.configure(activeforeground="black")
        self.IsıFanA.configure(background="#d9d9d9")
        self.IsıFanA.configure(compound='left')
        self.IsıFanA.configure(disabledforeground="#a3a3a3")
        self.IsıFanA.configure(foreground="#000000")
        self.IsıFanA.configure(highlightbackground="#d9d9d9")
        self.IsıFanA.configure(highlightcolor="black")
        self.IsıFanA.configure(pady="0")
        self.IsıFanA.configure(text='''Aç''')
        self.IsıFanA.bind('<Button-1>',Proje_support.isifana)
        self.FanText = tk.Label(self.top)
        self.FanText.place(relx=0.75, rely=0.066, height=23, width=64)
        self.FanText.configure(activebackground="#f9f9f9")
        self.FanText.configure(anchor='w')
        self.FanText.configure(background="#d9d9d9")
        self.FanText.configure(compound='left')
        self.FanText.configure(disabledforeground="#a3a3a3")
        self.FanText.configure(font="-family {Arial} -size 11 -weight bold")
        self.FanText.configure(foreground="#000000")
        self.FanText.configure(highlightbackground="#d9d9d9")
        self.FanText.configure(highlightcolor="black")
        self.FanText.configure(text='''Fanlar''')
        self.IsıFanK = tk.Button(self.top)
        self.IsıFanK.place(relx=0.842, rely=0.134, height=24, width=47)
        self.IsıFanK.configure(activebackground="beige")
        self.IsıFanK.configure(activeforeground="black")
        self.IsıFanK.configure(background="#d9d9d9")
        self.IsıFanK.configure(compound='left')
        self.IsıFanK.configure(disabledforeground="#a3a3a3")
        self.IsıFanK.configure(foreground="#000000")
        self.IsıFanK.configure(highlightbackground="#d9d9d9")
        self.IsıFanK.configure(highlightcolor="black")
        self.IsıFanK.configure(pady="0")
        self.IsıFanK.configure(text='''Kapat''')
        self.IsıFanK.bind('<Button-1>',Proje_support.isifank)
        self.IsıtıcıText = tk.Label(self.top)
        self.IsıtıcıText.place(relx=0.597, rely=0.134, height=22, width=44)
        self.IsıtıcıText.configure(activebackground="#f9f9f9")
        self.IsıtıcıText.configure(anchor='w')
        self.IsıtıcıText.configure(background="#d9d9d9")
        self.IsıtıcıText.configure(compound='left')
        self.IsıtıcıText.configure(disabledforeground="#a3a3a3")
        self.IsıtıcıText.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.IsıtıcıText.configure(foreground="#000000")
        self.IsıtıcıText.configure(highlightbackground="#d9d9d9")
        self.IsıtıcıText.configure(highlightcolor="black")
        self.IsıtıcıText.configure(text='''Isıtıcı''')
        self.Soğutucutext1 = tk.Label(self.top)
        self.Soğutucutext1.place(relx=0.567, rely=0.2, height=22, width=64)
        self.Soğutucutext1.configure(activebackground="#f9f9f9")
        self.Soğutucutext1.configure(anchor='w')
        self.Soğutucutext1.configure(background="#d9d9d9")
        self.Soğutucutext1.configure(compound='left')
        self.Soğutucutext1.configure(disabledforeground="#a3a3a3")
        self.Soğutucutext1.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.Soğutucutext1.configure(foreground="#000000")
        self.Soğutucutext1.configure(highlightbackground="#d9d9d9")
        self.Soğutucutext1.configure(highlightcolor="black")
        self.Soğutucutext1.configure(text='''Soğutucu''')
        self.SoğuFanA = tk.Button(self.top)
        self.SoğuFanA.place(relx=0.674, rely=0.2, height=24, width=47)
        self.SoğuFanA.configure(activebackground="beige")
        self.SoğuFanA.configure(activeforeground="black")
        self.SoğuFanA.configure(background="#d9d9d9")
        self.SoğuFanA.configure(compound='left')
        self.SoğuFanA.configure(disabledforeground="#a3a3a3")
        self.SoğuFanA.configure(foreground="#000000")
        self.SoğuFanA.configure(highlightbackground="#d9d9d9")
        self.SoğuFanA.configure(highlightcolor="black")
        self.SoğuFanA.configure(pady="0")
        self.SoğuFanA.configure(text='''Aç''')
        self.SoğuFanA.bind('<Button-1>',Proje_support.sogukfana)
        self.ÇatıA = tk.Button(self.top)
        self.ÇatıA.place(relx=0.674, rely=0.34, height=24, width=47)
        self.ÇatıA.configure(activebackground="beige")
        self.ÇatıA.configure(activeforeground="black")
        self.ÇatıA.configure(background="#d9d9d9")
        self.ÇatıA.configure(compound='left')
        self.ÇatıA.configure(disabledforeground="#a3a3a3")
        self.ÇatıA.configure(foreground="#000000")
        self.ÇatıA.configure(highlightbackground="#d9d9d9")
        self.ÇatıA.configure(highlightcolor="black")
        self.ÇatıA.configure(pady="0")
        self.ÇatıA.configure(text='''Aç''')
        self.ÇatıA.bind('<Button-1>',Proje_support.catia)
        self.SoğuFanK = tk.Button(self.top)
        self.SoğuFanK.place(relx=0.842, rely=0.2, height=24, width=47)
        self.SoğuFanK.configure(activebackground="beige")
        self.SoğuFanK.configure(activeforeground="black")
        self.SoğuFanK.configure(background="#d9d9d9")
        self.SoğuFanK.configure(compound='left')
        self.SoğuFanK.configure(disabledforeground="#a3a3a3")
        self.SoğuFanK.configure(foreground="#000000")
        self.SoğuFanK.configure(highlightbackground="#d9d9d9")
        self.SoğuFanK.configure(highlightcolor="black")
        self.SoğuFanK.configure(pady="0")
        self.SoğuFanK.configure(text='''Kapat''')
        self.SoğuFanK.bind('<Button-1>',Proje_support.sogukfank)
        self.ÇatıK = tk.Button(self.top)
        self.ÇatıK.place(relx=0.842, rely=0.334, height=24, width=47)
        self.ÇatıK.configure(activebackground="beige")
        self.ÇatıK.configure(activeforeground="black")
        self.ÇatıK.configure(background="#d9d9d9")
        self.ÇatıK.configure(compound='left')
        self.ÇatıK.configure(disabledforeground="#a3a3a3")
        self.ÇatıK.configure(foreground="#000000")
        self.ÇatıK.configure(highlightbackground="#d9d9d9")
        self.ÇatıK.configure(highlightcolor="black")
        self.ÇatıK.configure(pady="0")
        self.ÇatıK.configure(text='''Kapat''')
        self.ÇatıK.bind('<Button-1>',Proje_support.catik)
        self.ÇatıText = tk.Label(self.top)
        self.ÇatıText.place(relx=0.735, rely=0.266, height=23, width=84)
        self.ÇatıText.configure(activebackground="#f9f9f9")
        self.ÇatıText.configure(anchor='w')
        self.ÇatıText.configure(background="#d9d9d9")
        self.ÇatıText.configure(compound='left')
        self.ÇatıText.configure(disabledforeground="#a3a3a3")
        self.ÇatıText.configure(font="-family {Arial} -size 11 -weight bold")
        self.ÇatıText.configure(foreground="#000000")
        self.ÇatıText.configure(highlightbackground="#d9d9d9")
        self.ÇatıText.configure(highlightcolor="black")
        self.ÇatıText.configure(text='''Çatı Kapısı''')
        self.SulaText = tk.Label(self.top)
        self.SulaText.place(relx=0.75, rely=0.4, height=22, width=54)
        self.SulaText.configure(activebackground="#f9f9f9")
        self.SulaText.configure(anchor='w')
        self.SulaText.configure(background="#d9d9d9")
        self.SulaText.configure(compound='left')
        self.SulaText.configure(disabledforeground="#a3a3a3")
        self.SulaText.configure(font="-family {Arial} -size 11 -weight bold")
        self.SulaText.configure(foreground="#000000")
        self.SulaText.configure(highlightbackground="#d9d9d9")
        self.SulaText.configure(highlightcolor="black")
        self.SulaText.configure(text='''Sulama''')
        self.SüreText = tk.Label(self.top)
        self.SüreText.place(relx=0.674, rely=0.466, height=23, width=44)
        self.SüreText.configure(activebackground="#f9f9f9")
        self.SüreText.configure(anchor='w')
        self.SüreText.configure(background="#d9d9d9")
        self.SüreText.configure(compound='left')
        self.SüreText.configure(disabledforeground="#a3a3a3")
        self.SüreText.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.SüreText.configure(foreground="#000000")
        self.SüreText.configure(highlightbackground="#d9d9d9")
        self.SüreText.configure(highlightcolor="black")
        self.SüreText.configure(text='''Süre:''')
        self.Süreİnput = ttk.Entry(self.top)
        self.Süreİnput.place(relx=0.735, rely=0.466, relheight=0.045
                , relwidth=0.07)
        self.Süreİnput.configure(takefocus="")
        self.Süreİnput.configure(cursor="ibeam")
        self.SulaBut = tk.Button(self.top)
        self.SulaBut.place(relx=0.75, rely=0.534, height=24, width=47)
        self.SulaBut.configure(activebackground="beige")
        self.SulaBut.configure(activeforeground="black")
        self.SulaBut.configure(background="#d9d9d9")
        self.SulaBut.configure(compound='left')
        self.SulaBut.configure(disabledforeground="#a3a3a3")
        self.SulaBut.configure(foreground="#000000")
        self.SulaBut.configure(highlightbackground="#d9d9d9")
        self.SulaBut.configure(highlightcolor="black")
        self.SulaBut.configure(pady="0")
        self.SulaBut.configure(text='''Sula''')
        self.SulaBut.bind('<Button-1>',Proje_support.sula)
        self.sntext = tk.Label(self.top)
        self.sntext.place(relx=0.812, rely=0.466, height=23, width=44)
        self.sntext.configure(activebackground="#f9f9f9")
        self.sntext.configure(anchor='w')
        self.sntext.configure(background="#d9d9d9")
        self.sntext.configure(compound='left')
        self.sntext.configure(disabledforeground="#a3a3a3")
        self.sntext.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.sntext.configure(foreground="#000000")
        self.sntext.configure(highlightbackground="#d9d9d9")
        self.sntext.configure(highlightcolor="black")
        self.sntext.configure(text='''sn''')
        self.SürebilgiText_1 = tk.Label(self.top)
        self.SürebilgiText_1.place(relx=0.704, rely=0.6, height=22, width=104)
        self.SürebilgiText_1.configure(activebackground="#f9f9f9")
        self.SürebilgiText_1.configure(anchor='w')
        self.SürebilgiText_1.configure(background="#d9d9d9")
        self.SürebilgiText_1.configure(compound='left')
        self.SürebilgiText_1.configure(disabledforeground="#a3a3a3")
        self.SürebilgiText_1.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.SürebilgiText_1.configure(foreground="#000000")
        self.SürebilgiText_1.configure(highlightbackground="#d9d9d9")
        self.SürebilgiText_1.configure(highlightcolor="black")
        self.SürebilgiText_1.configure(text='''Varsıyılan 10sn''')
        self.ProjeText = ttk.Label(self.top)
        self.ProjeText.place(relx=0.398, rely=0.045, height=41, width=117)
        self.ProjeText.configure(background="#d9d9d9")
        self.ProjeText.configure(foreground="#000000")
        self.ProjeText.configure(font="-family {Tw Cen MT Condensed Extra Bold} -size 13")
        self.ProjeText.configure(relief="flat")
        self.ProjeText.configure(anchor='w')
        self.ProjeText.configure(justify='center')
        self.ProjeText.configure(text='''Akıllı Sera Sistemi''')
        self.ProjeText.configure(compound='center')
        self.DeğişSıc = tk.Label(self.top)
        self.DeğişSıc.place(relx=0.123, rely=0.134, height=22, width=55)
        self.DeğişSıc.configure(activebackground="#f9f9f9")
        self.DeğişSıc.configure(anchor='w')
        self.DeğişSıc.configure(background="#d9d9d9")
        self.DeğişSıc.configure(compound='left')
        self.DeğişSıc.configure(disabledforeground="#a3a3a3")
        self.DeğişSıc.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.DeğişSıc.configure(foreground="#000000")
        self.DeğişSıc.configure(highlightbackground="#d9d9d9")
        self.DeğişSıc.configure(highlightcolor="black")
        self.DeğişSıc.configure(text='''10''')
        self.DeğişSeraNem = tk.Label(self.top)
        self.DeğişSeraNem.place(relx=0.153, rely=0.179, height=22, width=55)
        self.DeğişSeraNem.configure(activebackground="#f9f9f9")
        self.DeğişSeraNem.configure(anchor='w')
        self.DeğişSeraNem.configure(background="#d9d9d9")
        self.DeğişSeraNem.configure(compound='left')
        self.DeğişSeraNem.configure(disabledforeground="#a3a3a3")
        self.DeğişSeraNem.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.DeğişSeraNem.configure(foreground="#000000")
        self.DeğişSeraNem.configure(highlightbackground="#d9d9d9")
        self.DeğişSeraNem.configure(highlightcolor="black")
        self.DeğişSeraNem.configure(text='''%70''')
        self.DeğişTopNem = tk.Label(self.top)
        self.DeğişTopNem.place(relx=0.168, rely=0.221, height=22, width=55)
        self.DeğişTopNem.configure(activebackground="#f9f9f9")
        self.DeğişTopNem.configure(anchor='w')
        self.DeğişTopNem.configure(background="#d9d9d9")
        self.DeğişTopNem.configure(compound='left')
        self.DeğişTopNem.configure(disabledforeground="#a3a3a3")
        self.DeğişTopNem.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.DeğişTopNem.configure(foreground="#000000")
        self.DeğişTopNem.configure(highlightbackground="#d9d9d9")
        self.DeğişTopNem.configure(highlightcolor="black")
        self.DeğişTopNem.configure(text='''%70''')
        self.DeğişHava = tk.Label(self.top)
        self.DeğişHava.place(relx=0.184, rely=0.266, height=23, width=104)
        self.DeğişHava.configure(activebackground="#f9f9f9")
        self.DeğişHava.configure(anchor='w')
        self.DeğişHava.configure(background="#d9d9d9")
        self.DeğişHava.configure(compound='left')
        self.DeğişHava.configure(disabledforeground="#a3a3a3")
        self.DeğişHava.configure(font="-family {Sitka Banner} -size 11 -weight bold")
        self.DeğişHava.configure(foreground="#000000")
        self.DeğişHava.configure(highlightbackground="#d9d9d9")
        self.DeğişHava.configure(highlightcolor="black")
        self.DeğişHava.configure(text='''Güneşli''')
        self.Yenile = tk.Button(self.top)
        self.Yenile.place(relx=0.031, rely=0.34, height=24, width=47)
        self.Yenile.configure(activebackground="beige")
        self.Yenile.configure(activeforeground="black")
        self.Yenile.configure(background="#d9d9d9")
        self.Yenile.configure(compound='left')
        self.Yenile.configure(disabledforeground="#a3a3a3")
        self.Yenile.configure(foreground="#000000")
        self.Yenile.configure(highlightbackground="#d9d9d9")
        self.Yenile.configure(highlightcolor="black")
        self.Yenile.configure(pady="0")
        self.Yenile.configure(text='''Yenile''')
        self.Yenile.bind('<Button-1>',Proje_support.degis)


def start_up():
    Proje_support.main()

if __name__ == '__main__':
    Proje_support.main()














