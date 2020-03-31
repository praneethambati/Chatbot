from tkinter import *
root=Tk()

def chatbot():
    send="you -> "+e.get()
    txt.insert(END,"\n"+send)
    j=send.split()
    k=len(j)
    #print(j)

    for l in range(0,k):
        if(j[l]=="hi" or j[l]=="hello"):
            txt.insert(END,"\n"+"BOT ->Hello!, I am LPU chatbot")
            #txt.insert(END,"\n"+"BOT ->\n")
            #chatbot()
    
    for l in range(0,k):
        if(j[l]=="college"):
            for m in range(0,k):
                if(j[m]=="name"or j[m]=="What is your college name"):
                    txt.insert(END,"\n"+"BOT ->Our college name is LOVELY PROFESSIONAL UNIVERSITY - PUNJAB ")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()
    for l in range(0,k):
        if(j[l]=="college"):
            for m in range(0,k):
                if(j[m]=="accredited"or j[m]=="Is your college is accreited or not"):
                    txt.insert(END,"\n"+"BOT ->Yes this is an accredited college")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()
    for l in range(0,k):
        if(j[l]=="college"):
            for m in range(0,k):
                if(j[m]=="fees"):
                    txt.insert(END,"\n"+"BOT ->It is 90000 per semester but we provide scholarship ")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()

    for l in range(0,k):
        if(j[l]=="scholarship"):
            txt.insert(END,"\n"+"BOT ->It depends on the marks obtained in LPUNEST or Jeemains score or board exams ")
            #txt.insert(END,"\n"+"BOT ->\n")
            #chatbot()

    for l in range(0,k):
        if(j[l]=="lpunest"):
            txt.insert(END,"\n"+"BOT ->It is an entrance exam conducted by LPU")
            #txt.insert(END,"\n"+"BOT ->\n")
            #chatbot()
    for l in range(0,k):
        if(j[l]=="lpunest"):
            for m in range(0,k):
                if(j[m]=="score" and j[m+1]=="required"):
                    txt.insert(END,"\n"+"BOT ->90% above for getting good scholarship!")
            #txt.insert(END,"\n"+"BOT ->\n")
            #chatbot()

    for l in range(0,k):
        if(j[l]=="college"):
            for m in range(0,k):
                if(j[m]=="acredited"):
                    txt.insert(END,"\n"+"BOT ->Yes this is an accredited college")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()

    for l in range(0,k):
        if(j[l]=="college"):
            for m in range(0,k):
                if(j[m]=="hours"):
                    txt.insert(END,"\n"+"BOT ->We are open 9 am - 5 pm Monday-saturday!")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()

    for l in range(0,k):
        if(j[l]=="5th"):
            for m in range(0,k):
                if(j[m]=="computer" and j[m+1]=="science"):
                    txt.insert(END,"\n"+"BOT ->subjects in 5th sem are:\nTheory of computation\nMicroprocessor and Interface\nprograming in java\nAnalysis and Design of Algorithm\nDatabase management system\nUnix and Shell Programing")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()

    for l in range(0,k):
        if(j[l]=="paymentmode"):
            txt.insert(END,"\n"+"BOT ->cheque,debit card,netbanking, PAYTM and cash are acceptable")
            #txt.insert(END,"\n"+"BOT ->\n")
            #chatbot()

    for l in range(0,k):
        if(j[l]=="hostel"):
            for m in range(0,k):
                if(j[m]=="facility"):
                    txt.insert(END,"\n"+"BOT ->Yes hostel facility is available within the campus")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()


    for l in range(0,k):
        if(j[l]=="hostel"):
            for m in range(0,k):
                if(j[m]=="facilities"):
                    txt.insert(END,"\n"+"BOT ->Telephone\nInternet access\nIndoor games\nFirst– Aid.\nReading materials\nTelevision\nDining Hall\nVehicle parking\nRound the-clock security, etc ")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()


    for l in range(0,k):
        if(j[l]=="hostel"):
            for m in range(0,k):
                if(j[m]=="fees"or j[m]=="How much hostel fees"):
                    txt.insert(END,"\n"+"BOT ->It depends on the room which you opt")
                    #txt.insert(END,"\n"+"BOT ->\n")
                    #chatbot()

    for l in range(0,k):
        if(j[l]=="Placements"or j[l]=="placements"):
            txt.insert(END,"\n"+"BOT ->Here at LPU we provide 100 percent placement assistance")
            #txt.insert(END,"\n"+"BOT ->\n")
            #chatbot()

                    
    #if(e.get()=="hello"):
        #txt.insert(END,"\n"+"Bot -> hi")
    e.delete(0,END)
    


txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
chatbot=Button(root,text="SEND",command=chatbot).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()
