#-------------------------------------------------------------------
# A11.py   Interface grafica para a Calculadora de IMC, Parte final
# V48-Curso de python com Interface Gráfica
# @author:  Nivaldo Mattos
# @email:   ulabchannel@gmail.com
# @Data:    13/07/2020
# @Codigo fonte: https://github.com/NivaldoMattos/Curso-de-Python-com-Interface-Grafica.git
#-------------------------------------------------------------------
from tkinter import *
Master = Tk()

#funções
def ClassificacaoIMCAdulto(imc):
    if imc < 18.5:
        LabelIMCClassificacao["text"]="Baixo peso"
    elif imc >= 18.5 and imc <= 24.9:
        LabelIMCClassificacao["text"] = "Peso normal"
    elif imc >= 25.0 and imc <= 29.9:
        LabelIMCClassificacao["text"] = "Excesso de peso"
    elif imc >= 30.0 and imc <= 34.9:
        LabelIMCClassificacao["text"] = "Obesidade classe 1"
    elif imc >= 35.0 and imc <= 39.9:
        LabelIMCClassificacao["text"] = "Obesidade classe 2"
    elif imc >= 40.0:
        LabelIMCClassificacao["text"] = "Obesidade classe 3"

def ClassificacaoIMCIdoso(imc):
    if imc <= 22:
        LabelIMCClassificacao["text"]="Baixo peso"
    elif imc > 22 and imc < 27:
        LabelIMCClassificacao["text"] = "Adequado ou eutrófico"
    else:
        LabelIMCClassificacao["text"] = "Sobrepeso"

def CalculaIMC():
    altura = float(EntryAltura.get())
    peso = float(EntryPeso.get())
    divisor = altura**2
    imc = peso / divisor
    imc = round(imc, 1)
    LabelIMCResultado["text"]=imc

    if FaixaEtaria.get():
        ClassificacaoIMCAdulto(imc)
    else:
        ClassificacaoIMCIdoso(imc)

#Imagens
TitleImg = PhotoImage(file="TitleImg.png")
TableImg = PhotoImage(file="TableImg.png")
BottomImg = PhotoImage(file="BottomImg.png")
Box1Img = PhotoImage(file="Box1Img.png")
Box2Img = PhotoImage(file="Box2Img.png")

#Frames-Containers: Agrupadores de objetos na tela
Topframe = Frame(Master, relief='solid', bd=0, bg="#1c1c1a")  #gray
Topframe.place(width=991, height=407, x=0, y=0)

LabelTitle = Label(Topframe, image=TitleImg, borderwidth=0, compound="center", highlightthickness=0)
LabelTitle.place(x=0, y=0)
LabelTable = Label(Topframe, image=TableImg, borderwidth=0,compound="center", highlightthickness=0)
LabelTable.place(x=0, y=48)

BottomFrame = Frame(Master, relief='solid', bd=0,   bg="#1c1c3a")
BottomFrame.place(width=991, height=232, x=0, y=407)
LabelBottomImg = Label(BottomFrame, image=BottomImg, borderwidth=0,compound="center", highlightthickness=0)
LabelBottomImg.place(x=0, y=0)

Box1Frame = Frame(Master, relief='solid', bd=0,   bg="#B97A57")
Box1Frame.place(width=276, height=200, x=23, y=422)
LabelBox1Img = Label(Box1Frame, image=Box1Img, borderwidth=0, compound="center", highlightthickness=0)
LabelBox1Img.place(x=0, y=0)

Box2Frame = Frame(Master, relief='solid', bd=0,   bg="#7F7F7F")
Box2Frame.place(width=611, height=200, x=318, y=422)
LabelBox2Img = Label(Box2Frame, image=Box2Img, borderwidth=0, compound="center", highlightthickness=0)
LabelBox2Img.place(x=0, y=0)
#-----------------------------------------
EntryAltura = Entry(Box1Frame, font="Arial 15", bg="black", fg="#7ED953")
EntryAltura.place(width=88, height=21, x=123, y=109)
EntryAltura.insert(END, 1.75)

EntryPeso = Entry(Box1Frame, font="Arial 15", bg="black", fg="#7ED953")
EntryPeso.place(width=88, height=21, x=123, y=148)
EntryPeso.insert(END, 75)

LabelIMCResultado = Label(Box2Frame, text="0.00", font="Arial 20", bg="black", fg="#7ED953")
LabelIMCResultado.place(width=102, height=42, x=32, y=56)

LabelIMCClassificacao = Label(Box2Frame, text="Peso normal",font="Arial 20", bg="black", fg="#7ED953")
LabelIMCClassificacao.place(width=395, height=41, x=175, y=56)

ButtonIMC = Button(Box2Frame, text="Show IMC", font="Arial 15 bold", command=CalculaIMC, bg="#0EA5DB")
ButtonIMC.place(width=117, height=41, x=238, y=126)

FaixaEtaria = IntVar()
FaixaEtaria.set(1)
CheckAdulto = Checkbutton(Box1Frame,  variable=FaixaEtaria, onvalue=1, bg="#4472C4")
CheckAdulto.place(x=68, y=53)

CheckIdoso = Checkbutton(Box1Frame,  variable=FaixaEtaria, onvalue=0, bg="#4472C4")
CheckIdoso.place(x=173, y=53)

#Configurações da tela Master
Master.geometry("951x634+50+50")  #951x634+50+50  #"951x634+-900+190"
Master.title("Calculadora de Indice de Massa Corporal-IMC")
Master.iconbitmap(default='ulab.ico')
mainloop()       
#-------------------------------------------------------------------
# E.O.F    
#-------------------------------------------------------------------
                                                                               