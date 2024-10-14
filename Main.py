from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

co0 = "#f0f3f5" 
co1 = "#f0f3f5"  
co2 = "#feffff" 
co3 = "#38576b"  
co4 = "#403d3d"  
co5 = "#6f9fbd" 
co6 = "#ef5350"  
co7 = "#93cd95"  

janela = Tk()
janela.title("Nibba Software")
janela.geometry('500x450')
janela.configure(background=co2)
janela.resizable(width=FALSE,height=FALSE)

style = Style(janela)
style.theme_use("clam")

frame_cima = Frame(janela,width=500,height=50,bg=co3,relief="flat")
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=150,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=248,bg=co2,relief="flat")
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)

#configurando a parte de cima

l_nome = Label(frame_cima,text='Agenta Telefónica',anchor=NE,font=('arial 20 bold'),bg=co3,fg=co1)
l_nome.place(x=5,y=5)

l_linha = Label(frame_cima,text='',width=500,anchor=NE,font=('arial 1'),bg=co2,fg=co1)
l_linha.place(x=0,y=46)

#configurando o formulário
l_nome = Label(frame_baixo,text='Nome *',anchor=NW,font=('ivy 10'),bg=co1,fg=co4)
l_nome.place(x=10,y=20)
en_nome = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_nome.place(x=80,y=20)


l_sexo = Label(frame_baixo,text='Sexo *',anchor=NW,font=('ivy 10'),bg=co1,fg=co4)
l_sexo.place(x=10,y=50)
c_sexo = Combobox(frame_baixo,width=27)
c_sexo['value'] = ('','F','M')
c_sexo.place(x=80,y=50)

l_Telefone = Label(frame_baixo,text='Telefone*',anchor=NW,font=('ivy 10'),bg=co1,fg=co4)
l_Telefone.place(x=10,y=80)
en_Telefone = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_Telefone.place(x=80,y=80)

l_Email = Label(frame_baixo,text='E-mail*',anchor=NW,font=('ivy 10'),bg=co1,fg=co4)
l_Email.place(x=10,y=110)
en_Email = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_Email.place(x=80,y=110)

b_procurar = Button(frame_baixo,text='procurar',font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_procurar.place(x=290,y=20)
en_procurar = Entry(frame_baixo,width=16,justify='left',font=('',11),highlightthickness=1)
en_Email.place(x=347,y=20)

b_Olhar = Button(frame_baixo,text='Ver dados',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Olhar.place(x=290,y=50)

b_Adicionar = Button(frame_baixo,text='Adicionar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Adicionar.place(x=400,y=50)

b_Atualizar = Button(frame_baixo,text='Atualizar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Atualizar.place(x=400,y=80)

b_Deletar = Button(frame_baixo,text='Deletar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Deletar.place(x=400,y=110)

janela.mainloop()
