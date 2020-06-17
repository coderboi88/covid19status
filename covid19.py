# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from Tkinter import *
import requests
import json

root = Tk()
root.title("Covid 19 Status")
root.geometry("500x400")
root.config(bg="#5c2a9d")##7CEC9F
frame = LabelFrame(root,text="State Status",padx=20,pady=30,width=300,height=300,bg="#BFDADD")
frame.grid(row=1,column=0,columnspan=3,padx=10,pady=10)

frame1 = LabelFrame(root,text="Current Situation Of India",padx=20,pady=30,width=300,height=100,bg="#BFDADD")
frame1.grid(row=2,column=0,columnspan=3,padx=10,pady=10)

options=[]

covid_status = requests.get("https://api.rootnet.in/covid19-in/stats/latest")
covid_result= json.loads(covid_status.content)
data = covid_result["data"]["regional"]
for d in range(len(data)):
    options.append(data[d]['loc'])

#print(covid_result)

def status(e):  
    result=''
    for d in range(len(data)):
        if var1.get()== data[d]['loc']:
            result = result+"State: "+data[d]['loc']+"\n"+"Confirmed Cases: "+str(data[d]['confirmedCasesIndian'])+"\n"+"Deaths: "+str(data[d]['deaths'])+"\n"
        #print(data[0]['loc'])
    label1.config(text=result,bg="Red")
    
def india_status():
    a=0
    for d in range(len(data)):
       a +=  data[d]['confirmedCasesIndian']
    a = "Total Cases: " + str(a)
    label2.config(text=a)

#covid_entry = Entry(root)
#covid_entry.grid(row=0,column=1,padx=20,pady=10)

covid_button = Button(frame1,text = "Get Status",command=india_status)
covid_button.grid(row=0,column=1,padx=20,pady=10)

label = Label(frame,text="Select State :",font=("Helvetica",15),fg="blue")
label.grid(row=0,column=0,padx=5,pady=10)

label1 = Label(frame,text='')
label1.grid(row=1,column=0,columnspan=2,pady=10)

var1= StringVar()
var1.set(options[0])
menu = OptionMenu(frame,var1,*options,command=status)
menu.grid(row=0,column=1,padx=20)

label3 = Label(frame1,text="If You Want To know Total Cases Of India :",font=("Helvetica",10),fg="blue")
label3.grid(row=0,column=0)

label2 = Label(frame1,text='',font=("Helvetica",15))
label2.grid(row=2,column=0,columnspan=2)
root.mainloop()
