from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

co0 = "#f0f3f5" 
co1 = "#f0f3f5"  
co2 = "#feffff" 
co3 = "#38576b"  
co4 = "#403d3d"  
co5 = "#6f9fbd" 
co6 = "#ef5350"  
co7 = "#93cd95"  

janela = Tk()
janela.title("Software Inclusão de idosos")
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
janela.geometry("500x450")
janela.configure(background=co2)
janela.resizable(width=TRUE,height=TRUE)

style = Style(janela)
style.theme_use("clam")

frame_cima = Frame(janela,width=500,height=50,bg=co3,relief="flat")
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)

frame_baixo = Frame(janela,width=500,height=150,bg=co1,relief="flat")
frame_baixo.grid(row=1,column=0,pady=1,padx=0,sticky=NSEW)

frame_tabela = Frame(janela,width=500,height=248,bg=co2,relief="flat")
frame_tabela.grid(row=2,column=0,columnspan=2,padx=10,pady=1,sticky=NW)

#configurando a parte de cima

l_nome = Label(frame_cima,text='Agenda Telefônica',font=('arial 20 bold'),bg=co3,fg=co1)
l_nome.pack(fill=BOTH,expand=TRUE)
l_nome.place(x=5,y=5)


l_linha = Label(frame_cima,text='',width=500,anchor=NE,font=('arial 1'),bg=co2,fg=co1)
l_linha.place(x=0,y=46)

#configurando o formulário
l_nome = Label(frame_baixo,text='Nome *',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_nome.place(x=10,y=15)
en_nome = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_nome.place(x=80,y=20)


l_sexo = Label(frame_baixo,text='Sexo *',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_sexo.place(x=10,y=50)
c_sexo = Combobox(frame_baixo,width=27)
c_sexo['value'] = ('','F','M','gambiarra do kpta')
c_sexo.place(x=80,y=50)

l_Telefone = Label(frame_baixo,text='Telefone*',anchor=NW,font=('ivy 12 bold'),bg=co1,fg=co4)
l_Telefone.place(x=5,y=80)
en_Telefone = Entry(frame_baixo,width=25,justify='left',font=('',10),highlightthickness=1)
en_Telefone.place(x=80,y=80)

l_Email = Label(frame_baixo,text='E-mail*',anchor=NW,font=('ivy 15'),bg=co1,fg=co4)
l_Email.place(x=10,y=110)
en_Email = Entry(frame_baixo,width=25,justify='left',relief="sunken",font=('',10),highlightthickness=1)
en_Email.place(x=80,y=110)

b_procurar = Button(frame_baixo,text='procurar',font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_procurar.place(x=290,y=20)
en_procurar = Entry(frame_baixo,width=16,justify='left',font=('',11),highlightthickness=1)
en_procurar.place(x=350,y=20)

b_Olhar = Button(frame_baixo,text='Ver dados',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Olhar.place(x=290,y=50)

b_Adicionar = Button(frame_baixo,text='Adicionar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Adicionar.place(x=400,y=50)

b_Atualizar = Button(frame_baixo,text='Atualizar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Atualizar.place(x=400,y=80)

b_Deletar = Button(frame_baixo,text='Deletar',width=10,font=('ivy 8 bold'),bg=co1,fg=co4,relief=RAISED,overrelief=RIDGE)
b_Deletar.place(x=400,y=110)

#configurando frame tabela
Cab_lista = ['Nome','Sexo','Telefone','e-mail']
dados = [['joao','Gambiarra do kpta','123456','joaomibba'],
         ['julia','F','123456','gigamibba']]

tree = ttk.Treeview(frame_tabela,selectmode="extended",columns=Cab_lista,show="headings")

#barra de rolagem
vbr = ttk.Scrollbar(frame_tabela,orient="vertical",command=tree.yview)
hbr = ttk.Scrollbar(frame_tabela,orient="horizontal",command=tree.xview)

tree.configure(yscrollcommand=vbr.set,xscrollcommand=hbr.set)

tree.grid(column=0,row=0,sticky='nsew')
vbr.grid(column=1,row=0,sticky='ns')
hbr.grid(column=0,row=1,sticky='ew')

hd = ["nw","nw","nw","nw","nw"]
h=[120,50,80,120,200]
n=0

tree.heading(0,text='Nome',anchor=NW)
tree.heading(1,text='Sexo',anchor=NW)
tree.heading(2,text='Telefone',anchor=NW)
tree.heading(3,text='Email',anchor=NW)

tree.column(0,width=120,anchor='nw')
tree.column(1,width=50,anchor='nw')
tree.column(2,width=100,anchor='nw')
tree.column(0,width=120,anchor=hd[0])

for item in dados:
     tree.insert('','end',values=item)
     


janela.mainloop()
