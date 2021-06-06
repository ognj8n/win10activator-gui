import os
import subprocess
import time
import tempfile
import sys
from clint.textui import colored
import smtplib
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkinter import * 




def activate():
    if messagebox.askyesno("by ogi#0001", "Da li ste spremni da aktivirate vas Windows 10?") == True:
        pass
    else:
        exit()
    temp_folder=tempfile.gettempdir()
    os.chdir(temp_folder)
    with open("process.bat","w",encoding="utf-8") as process:
        process.write("""
:: Q:\Test\2019\04\07\SU_1422368.cmd
@Echo off&SetLocal EnableExtensions EnableDelayedExpansion
Set "WinVerAct="
For /f "tokens=*" %%W in ('
    cscript /Nologo "C:\Windows\System32\slmgr.vbs" /xpr
') Do Set "WinVerAct=!WinVerAct! %%W"
if Not defined WinVerAct ( 
    Echo:No response from slmgr.vbs
    Exit /B 1
)
Echo Windows Version Activation Status:
Echo:"%WinVerAct:~1%"
        """)
            
    os.system("process.bat > process.txt")
    with open ("process.txt","r",encoding="utf-8") as file:
        file=file.read()
    if "will expire" in file:
        messagebox.showinfo("Cekaj malo...", "Izgleda kao da je Windows vec aktiviran!")
        messagebox.showinfo("Cekaj malo...", "Hvala na koriscenju!")
        sys.exit()
    else:
        messagebox.showinfo("Good", "Aktiviram Windows...")
        search=subprocess.check_output(["systeminfo"])
        search=str(search)
        if "Professional Education" in search:
            key="6TP4R-GNPTD-KYYHQ-7B7DP-J447Y"
        elif "Home" in search or "home" in search or "HOME" in search:
            key="TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
        elif "Education" in search:
            key="NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
        elif "Enterprise" in search:
            key="NPPR9-FWDCX-D2C8J-H872K-2YT43"
        elif "Core" in search:
            key="33QT6-RCNYF-DXB4F-DGP7B-7MHX9"
        elif "build" in search:
            key="VK7JG-NPHTM-C97JM-9MPGT-3V66T"
        elif "Pro" in search or "pro" in search or "PRO" and not "Professional" in search:
            if "Professional Workstations" in search:
                key="NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84J"
            key="W269N-WFGWX-YVC9B-4J6C9-T83GX"

        os.system("slmgr /ipk "+str(key))
        os.system("slmgr /skms kms8.msguides.com")
        os.system("slmgr /ato")
        messagebox.showinfo("Good", "Pricekaj...")
        with open("process.bat","w",encoding="utf-8") as process:
            process.write("""
:: Q:\Test\2019\04\07\SU_1422368.cmd
@Echo off&SetLocal EnableExtensions EnableDelayedExpansion
Set "WinVerAct="
For /f "tokens=*" %%W in ('
    cscript /Nologo "C:\Windows\System32\slmgr.vbs" /xpr
') Do Set "WinVerAct=!WinVerAct! %%W"
if Not defined WinVerAct ( 
    Echo:No response from slmgr.vbs
    Exit /B 1
)
Echo Windows Version Activation Status:
Echo:"%WinVerAct:~1%"
""")
        os.system("process.bat > gotovo.txt")
        with open ("gotovo.txt","r",encoding="utf-8") as file:
            file=file.read()
        if "will expire" in file:
            messagebox.showinfo("Good", "Windows Uspesno Aktiviran!")
            time.sleep(4)
            sys.exit()
        else:
            messagebox.showerror("Bad", "Nisam uspeo aktivirati Windows na tvom racunaru/laptopu")
            time.sleep(2)
            sys.exit()


def start():
    activate()






root = Tk()


root.geometry('350x330')
root.configure(background='#212121')
root.title('Windows Activator')





Label(root, text='Windows', bg='#FFFFFF', font=('helvetica', 12, 'bold')).place(x=77, y=11)



Label(root, text='Activator', bg='#FFFFFF', font=('helvetica', 18, 'bold')).place(x=117, y=31)



Button(root, text='Aktiviraj!', bg='#FFFFFF', font=('verdana', 18, 'italic'), command=start).place(x=107, y=181)



root.mainloop()
