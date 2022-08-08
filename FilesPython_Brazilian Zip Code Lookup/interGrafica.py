import PySimpleGUI as sg # pip install PySimpleGUI

def homeScreen():
    sg.theme('Dark2')

    cep = [
        [sg.Text('Informe um CEP: ', font='arial 14', pad =(0, 0))],
        [sg.Input(size=(20, 0), font='arial 14', pad = (0, 0), key = 'cep')]
    ]


    colun1 = [ # First column, in which the texts that the user will be asked to write are stored./# Primeira coluna, em que possuira os textos que serão pedidos ao usuário.
        [sg.Text('Logradouro: ', font = 'arial 15')],
        [sg.Text('Bairro: ', font = 'arial 15')],
        [sg.Text('Localidade: ', font = 'arial 15')],
        [sg.Text('UF: ', font = 'arial 15')],
        [sg.Text('IBGE: ', font = 'arial 15')],
        [sg.Text('DDD: ', font = 'arial 15')]
    ]
    
    colun2 = [# Second column, in which the inputs will be placed by the user./Segunda coluna, em que possuira os inputs que serão colocados pelo usuário.
        [sg.Input(font ='arial 15 bold', key = 'logradouro', size =(35, 1))],
        [sg.Input(font ='arial 15 bold', key = 'bairro', size =(30, 1))],
        [sg.Input(font ='arial 15 bold', key = 'localidade', size =(30, 1))],
        [sg.Input(font ='arial 15 bold', key = 'uf', size =(8, 1))],
        [sg.Input(font ='arial 15 bold', key = 'ibge', size =(18, 1))],
        [sg.Input(font ='arial 15 bold', key = 'ddd', size =(10, 1))],
    ]

    botoes = [ #Botões do GUI/GUI Buttons
        [sg.Button('Consultar', font='arial 15', size=(10, 1), pad = ((0, 15), 0)),
        sg.CButton('Sair', font='arial 15', size=(10, 1))]
    ]

    layout = [ # Layout do GUI/Layout GUI
        [sg.Text('Consultar CEP', font='arial 18 bold', justification='center', pad =(0, 0))],
        [sg.Column(cep, justification='center', element_justification='center')],
        [sg.Column(colun1, pad=((0,20),0)), 
        sg.Column(colun2)],
        [sg.Column(botoes, justification='center')]
    ]

    impimir = sg.Window('ConsultarCEP', element_padding=(0,10), layout = layout, size=(600,500), finalize=True)