import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math as m
font=('arial',16,'bold')
#creating an window

#important function

def clear(event=None):
    ex=input_text.get()
    ex=ex[0:len(ex)-1]
    input_text.delete(0,tk.END)
    input_text.insert(0,ex)
    
def all_clear(event=None):
    input_text.delete(0,tk.END)

def click_btn_function(event):
    b=event.widget
    text=b['text']
    #print(text)
    
    if text=='x':
        input_text.insert(tk.END,'*')
        return
    if text=='=':
        try :
            ex=input_text.get()
            answer=eval(ex)
            input_text.delete(0,tk.END)
            input_text.insert(0,answer)
        except Exception as e:
            messagebox.showerror('Error',e)
        return
    input_text.insert(tk.END,text)

window=tk.Tk()
window.title('Calculator')
window.geometry('340x370')
window.resizable(0,0)
img=tk.PhotoImage(file='icon.ico')
window.iconphoto(True,img)


##picture label
pic=tk.PhotoImage(file='image/ calc.png')
heading_lebel=ttk.Label(window,image=pic)
heading_lebel.pack(side=tk.TOP)

#heading label
heading_lebel=ttk.Label(window,text='My Calculator',font=font,underline=0,)
heading_lebel.pack(side=tk.TOP)

#textfield
input_text = tk.Entry(window,font=font,justify=tk.CENTER) 
input_text.pack(side=tk.TOP,fill=tk.X)

#button
button_frame = ttk.Frame(window)
button_frame.pack(side=tk.TOP,pady=10)

#adding button
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=tk.Button(button_frame,text=str(temp),font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
        btn.grid(row=i,column=j,padx=3,pady=3)
        temp=temp+1
        btn.bind('<Button-1>',click_btn_function)

zero_btn=tk.Button(button_frame,text='0',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
zero_btn.grid(row=3,column=0,padx=3,pady=3)

dot_btn=tk.Button(button_frame,text='.',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
dot_btn.grid(row=3,column=1,padx=3,pady=3)

equal_btn=tk.Button(button_frame,text='=',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
equal_btn.grid(row=3,column=2,padx=3,pady=3)

plus_btn=tk.Button(button_frame,text='+',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
plus_btn.grid(row=0,column=3,padx=3,pady=3)

minus_btn=tk.Button(button_frame,text='-',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
minus_btn.grid(row=1,column=3,padx=3,pady=3)

mult_btn=tk.Button(button_frame,text='x',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
mult_btn.grid(row=2,column=3,padx=3,pady=3)

devide_btn=tk.Button(button_frame,text='/',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
devide_btn.grid(row=3,column=3,padx=3,pady=3)

clear_btn=tk.Button(button_frame,text='<--',font=font,width=11,relief='ridge',activebackground='blue',activeforeground='white',command=clear)
clear_btn.grid(row=4,column=0,columnspan=2,padx=3,pady=3)

allclear_btn=tk.Button(button_frame,text='AC',font=font,width=11,relief='ridge',activebackground='blue',activeforeground='white',command=all_clear)
allclear_btn.grid(row=4,column=2,columnspan=2,padx=3,pady=3)

#binding all button
zero_btn.bind('<Button-1>',click_btn_function)
dot_btn.bind('<Button-1>',click_btn_function)
equal_btn.bind('<Button-1>',click_btn_function)
plus_btn.bind('<Button-1>',click_btn_function)
minus_btn.bind('<Button-1>',click_btn_function)
mult_btn.bind('<Button-1>',click_btn_function)
devide_btn.bind('<Button-1>',click_btn_function)
#clear_btn.bind('<Button-1>',clear)
#allclear_btn.bind('<Button-1>',all_clear)

def enter_click(event):
    e = tk.Event()
    e.widget = equal_btn
    click_btn_function(e)

input_text.bind('<Return>', enter_click)

######################################code for scientific calculator######################

#function for scientific calculator
sc_frame=ttk.Frame(window)

sqrt_btn=tk.Button(sc_frame,text='√',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
sqrt_btn.grid(row=0,column=0,padx=3,pady=3)

pow_btn=tk.Button(sc_frame,text='^',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
pow_btn.grid(row=0,column=1,padx=3,pady=3)

fact_btn=tk.Button(sc_frame,text='x!',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
fact_btn.grid(row=0,column=2,padx=3,pady=3)

rad_btn=tk.Button(sc_frame,text='toRad',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
rad_btn.grid(row=0,column=3,padx=3,pady=3)

sin_btn=tk.Button(sc_frame,text='sinθ',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
sin_btn.grid(row=1,column=0,padx=3,pady=3)

cos_btn=tk.Button(sc_frame,text='cosθ',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
cos_btn.grid(row=1,column=1,padx=3,pady=3)

tan_btn=tk.Button(sc_frame,text='tanθ',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
tan_btn.grid(row=1,column=2,padx=3,pady=3)

comma_btn=tk.Button(sc_frame,text=',',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
comma_btn.grid(row=1,column=3,padx=3,pady=3)

deg_btn=tk.Button(sc_frame,text='toDeg',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
deg_btn.grid(row=2,column=0,padx=3,pady=3)

log_btn=tk.Button(sc_frame,text='log',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
log_btn.grid(row=2,column=1,padx=3,pady=3)

onebyx_btn=tk.Button(sc_frame,text='1/x',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
onebyx_btn.grid(row=2,column=2,padx=3,pady=3)

rem_btn=tk.Button(sc_frame,text='rem',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
rem_btn.grid(row=2,column=3,padx=3,pady=3)

gcd_btn=tk.Button(sc_frame,text='gcd',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
gcd_btn.grid(row=3,column=0,padx=3,pady=3)

pi_btn=tk.Button(sc_frame,text='pi',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
pi_btn.grid(row=3,column=1,padx=3,pady=3)

ln_btn=tk.Button(sc_frame,text='ln',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
ln_btn.grid(row=3,column=2,padx=3,pady=3)

e_btn=tk.Button(sc_frame,text='e',font=font,width=5,relief='ridge',activebackground='blue',activeforeground='white')
e_btn.grid(row=3,column=3,padx=3,pady=3)

normalcalc=True

def calculator_sc(event):
    btn=event.widget
    text=btn['text']
    #print(text)
    ex=input_text.get()
    answer=''
    if text=='toDeg':
        answer=str(m.degrees(float(ex)))
    elif text=='toRad':
        answer=str(m.radians(float(ex)))
    elif text=='x!':
        answer=str(m.factorial(int(ex)))
    elif text=='sinθ':
        answer=str(m.sin(m.radians(float(ex))))
    elif text=='cosθ':
         answer=str(m.sin(m.radians(float(ex))))
    elif text=='tanθ':
         answer=str(m.tan(m.radians(float(ex))))
    elif text=='log':
         answer=str(m.log10(float(ex)))
    elif text=='1/x':
         answer=str(1/(float(ex)))
    elif text=='rem':
        num1,num2=ex.split(",")
        answer=str(m.remainder(float(num1),float(num2)))
    elif text=='√':
         answer=str(m.sqrt(int(ex)))
    elif text=='^':
        base,pow=ex.split(",")
        answer=m.pow(int(base),int(pow))
    elif text=='gcd':
        num1,num2=ex.split(",")
        answer=str(m.gcd(int(num1),int(num2)))

    elif text=='pi':
        if ex=='':
            answer=str(m.pi)
        else:
            answer=str(float(ex) * m.pi)
    
    elif text=='ln':
         answer=str(m.log(float(ex)))

    elif text=='e':
        if ex=='':
            answer=str(m.e)
        else:
            answer=str(m.e**float(ex))
    
    input_text.delete(0,tk.END)
    input_text.insert(0,answer)

    
def sc_click():
    global normalcalc
    if normalcalc:
        button_frame.pack_forget()
        #add sc frame
        sc_frame.pack(side=tk.TOP)
        button_frame.pack(side=tk.TOP)
        window.geometry('350x520')
        normalcalc=False
    else:
        sc_frame.pack_forget()
        window.geometry('340x370')
        normalcalc=True


# end function
# binding sc button
comma_btn.bind('<Button-1>',click_btn_function)
sqrt_btn.bind("<Button-1>",calculator_sc)
pow_btn.bind("<Button-1>",calculator_sc)
fact_btn.bind("<Button-1>",calculator_sc)
rad_btn.bind("<Button-1>",calculator_sc)
deg_btn.bind("<Button-1>",calculator_sc)
sin_btn.bind("<Button-1>",calculator_sc)
cos_btn.bind("<Button-1>",calculator_sc)
tan_btn.bind("<Button-1>",calculator_sc)
log_btn.bind("<Button-1>",calculator_sc)
onebyx_btn.bind("<Button-1>",calculator_sc)
rem_btn.bind("<Button-1>",calculator_sc)
gcd_btn.bind("<Button-1>",calculator_sc)
pi_btn.bind("<Button-1>",calculator_sc)
ln_btn.bind("<Button-1>",calculator_sc)
e_btn.bind("<Button-1>",calculator_sc)

font_menu=('arial',12,'bold')
menubar=tk.Menu(window)
mode=tk.Menu(menubar,font=font_menu,tearoff=0)
mode.add_checkbutton(label='Scientific Calculator',command=sc_click)
menubar.add_cascade(label='Mode',menu=mode)
window.config(menu=menubar)

window.mainloop()

