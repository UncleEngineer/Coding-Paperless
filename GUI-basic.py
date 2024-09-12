from tkinter import *
from tkinter import ttk #พิมพ์ด้านบน

GUI = Tk()
GUI.geometry('500x500')
GUI.title('โปรแกรมสมัครงาน by ลุง')

L = Label(GUI,text='กรอกใบสมัครที่นี่',font=('Angsana New',25))
L.pack()

L = Label(GUI,text='คุณสมบัติ\n-ต้องอายุมากกว่า 20 ปี\n-วุฒิ ม.6',font=('Angsana New',15))
L.pack()
#-------------------------
v_fullname = StringVar()
L = Label(GUI,text='ชื่อ-สกุล',font=('Angsana New',20))
L.pack()
E1 = ttk.Entry(GUI,textvariable=v_fullname,font=('Angsana New',20))
E1.pack()
#-------------------------
v_tel = StringVar()
L = Label(GUI,text='เบอร์โทร',font=('Angsana New',20))
L.pack()
E2 = ttk.Entry(GUI,textvariable=v_tel,font=('Angsana New',20))
E2.pack()
#-------------------------
v_position = StringVar()
L = Label(GUI,text='ตำแหน่ง',font=('Angsana New',20))
L.pack()
E3 = ttk.Entry(GUI, textvariable=v_position, font=('Angsana New',20), width=30)
E3.pack()

import csv

def writetocsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
        

def Save():
    fullname = v_fullname.get()
    tel = v_tel.get()
    position = v_position.get()
    print(fullname,tel,position)
    data = [fullname,tel,position]
    writetocsv(data)
    v_fullname.set('')
    v_tel.set('')
    v_position.set('')


B1 = ttk.Button(GUI,text='บันทึก',command=Save)
B1.pack(pady=30,ipadx=30,ipady=20)

GUI.mainloop()