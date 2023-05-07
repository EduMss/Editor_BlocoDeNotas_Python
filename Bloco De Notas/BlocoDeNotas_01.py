import PySimpleGUI as sg
import os

# -------------------------------------------------------
#Procurar Todos Os Blocos De Notas Da Pasta E add no Notas

Notas = []
BlocoSelecionado = ""
NomeBloco = ""
PodeFuncionar = bool(False)

class Procurar_Blocos_De_Notas:
    def __init__(self):
        pass

    def func(self,Notas):
        Notas.clear()
        for file in os.listdir():
            if file.endswith(".txt"):
                Notas.append(file)

Procurar = Procurar_Blocos_De_Notas()
Procurar.func(Notas=Notas)


#---------------------------------------------------------
#Popup para criar um novo bloco de notas

class Popup:
    def __init__(self):
        layout = [
            [sg.Text('Nome:')],
            [sg.Input(key='NomeDoBloco')],
            [sg.Button('Criar', key='CriarBloco'),sg.Button('Cancelar', key='CancelarCriar')]
        ]

        self.window = sg.Window('Novo Bloco de Notas').Layout(layout)

    def func(self):
        while True:
            self.event, self.value = self.window.read()
            if self.event == sg.WIN_CLOSED or self.event == "CancelarCriar":
                self.window.close()
                break

            elif self.event == 'CriarBloco':#fazer uma verificação para ver se ja existe um bloco de notas com esse nome
                open(self.value['NomeDoBloco']+".txt", 'w')
                window.updateBDN()
                self.window.close()
                break
            
PopupNovoBlocoDeNotas = Popup()

#---------------------------------------------------------
#Popup para editar o bloco de notas

class Popup_Nota():
    def __init__(self, BlocoSelecionado, NomeBloco):

        BlocoSelecionado = BlocoSelecionado
        NomeBloco = NomeBloco.replace(".txt","")

        self.Tela(BlocoSelecionado=BlocoSelecionado, NomeBloco = NomeBloco)
        self.func(BlocoSelecionado=BlocoSelecionado, NomeBloco = NomeBloco)


    def Tela(self,BlocoSelecionado,NomeBloco):
        layout = [
            [sg.Text("")],#Colocar o nome do bloco de notas
            [sg.Input(key='EditorNomeBlocoDeNotas', size=(400,400), default_text = NomeBloco)],
            [sg.Button('Salvar', key='SalvarBloco'),sg.Button('Cancelar', key='CancelarEdição')],
            [sg.Multiline(size=(60, 15), key='EditorBlocoDeNotas',  default_text= BlocoSelecionado )]
        ]

        self.window = sg.Window('Editor Bloco de Nota ('+ NomeBloco +')', size=(500,500)).Layout(layout)


    def func(self, BlocoSelecionado, NomeBloco):
        while True:
            self.event, self.value = self.window.read()

            if self.event == sg.WIN_CLOSED or self.event == "CancelarEdição":
                self.window.close()
                break

            elif self.event == 'SalvarBloco':
                self.salvar(BlocoSelecionado=BlocoSelecionado, NomeBloco = NomeBloco)

    def salvar(self,BlocoSelecionado, NomeBloco):
        while True:

            ArquivoNota = open(NomeBloco+".txt","w")

            BlocoSelecionado = self.value['EditorBlocoDeNotas']
            ArquivoNota.write(BlocoSelecionado)

            ArquivoNota.close()


            NomeBlocoNew = self.value['EditorNomeBlocoDeNotas']
            file_oldname = os.path.join("", NomeBloco + ".txt")
            file_newname_newfile = os.path.join("", NomeBlocoNew + ".txt")

            os.rename(file_oldname, file_newname_newfile)

            
            window.updateBDN()
            self.window.close()

            break


#---------------------------------------------------------
#Janela Principal

class Janela:
    def __init__(self):
        layout = [
            [sg.Button('+', key='NovoBloco',size=(2,1),tooltip='Criar Bloco de Nota')],
            [sg.Listbox(values=Notas, size=(30, 6), key='List')],
            [sg.Button('Abrir', key="AbrirBlocoDeNota",size=(3,1))]
        ]

        self.window = sg.Window('Bloco de Notas' ).Layout(layout)

        

    def fazer(self):
        while True:
            self.event, self.value = self.window.read()
            if self.event == sg.WIN_CLOSED:
                break
            
            elif self.event == 'NovoBloco':
                PopupNovoBlocoDeNotas.func()
            
            elif self.event == "AbrirBlocoDeNota":#peguei o nome do arquivo selecionado na listbox
                List = self.window['List']
                List = str(List.get())

                #--------------------------------------------------
                #n sei se vai preicsar quando eu pegar o texto dentro do arquivo, ou eu vou procurar o outro metodo, q so apaga o final e o inicio e eu escolho quantos espaços são apagados
                Bugs = ('[',']',"'")

                for Bug in Bugs:
                    index = Bugs.index(Bug)
                    if Bugs[index] in List:
                        List = List.replace(Bugs[index], '')
                #--------------------------------------------------
                arquivo = open(List,"r", encoding="utf-8")
                arquivo = arquivo.read()
                self.PopupEditorBlocoDeNotas = Popup_Nota(arquivo, List)

    def updateBDN(self):
        Procurar.func(Notas=Notas)
        List = self.window['List']
        List.update(values=Notas)



window = Janela()
window.fazer()

#---------------------------------------------------------