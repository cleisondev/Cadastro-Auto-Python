from PySimpleGUI import PySimpleGUI as sg
import pyautogui
from time import sleep 
from threading import Timer



#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha  '),sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]

]

layoutDois = [
    [sg.Text('Produto'), sg.Input(key='produto', size=(20,1))],
    [sg.Text('Qtd      '),sg.Input(key='quantidade', size=(20,1))],
    [sg.Text('Preco   '),sg.Input(key='preco', size=(20,1))],
    [sg.Multiline( enable_events=True,size=(60,30), key='Input', expand_x=True, expand_y=True, justification='left')],
    [sg.Button('Reg')]

]
#Nome da tela
janela = sg.Window('Tela de login', layout)


#FUNCOES

def login(): 
    pyautogui.click(929,529,duration=2)
    pyautogui.write('c')


    pyautogui.click(928,556,duration=2)
    pyautogui.write('1')
    
    pyautogui.click(875,620,duration=2) 

    with open('produtos.txt','r') as file:
        for linha in file:
            produto = linha.split(',')[0]
            quantidade = linha.split(',')[1]
            preco = linha.split(',')[2]

            pyautogui.click(845,510,duration=2)
            pyautogui.write(produto)

            pyautogui.click(851,540,duration=2)
            pyautogui.write(quantidade)

            pyautogui.click(848,568,duration=2)
            pyautogui.write(preco)

            pyautogui.click(776,636,duration=2)



    



def limpar():
    jan['produto'].update('')
    jan['quantidade'].update('')
    jan['preco'].update('')



#Lendo as infos do layout e criando a interface

while True:
    # t = Timer(2.0, login)
    # t.start()

    eventos, valores = janela.read()
    
    
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':      
        if valores['usuario'] == 'c' and valores['senha'] == '1':
              jan = sg.Window('Tela de cadastro', layoutDois)
              ev, values = jan.read()
        if ev == 'Reg':
            prod = values['produto']
            qtd = values['quantidade']
            preco = values['preco']
            saida = f'Produto: {prod}, Quantidade: {qtd}, Preco: {preco}'
            jan['Input'].update(saida)
            
            limpar()
            jan.read()
    
    







 