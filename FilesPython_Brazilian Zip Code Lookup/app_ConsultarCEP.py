from interGrafica import *
from consultaCEP import *

homeScreen()
while True:
    window,event,values = sg.read_all_windows()

    if(event== sg.WIN_CLOSED):
        break
    
    
    if(event == 'Consultar'):
        try:
            logradouro = consulta(values['cep'])['logradouro']
            bairro = consulta(values['cep'])['bairro']
            localidade = consulta(values['cep'])['localidade']
            uf = consulta(values['cep'])['uf']
            ibge = consulta(values['cep'])['ibge']
            ddd = consulta(values['cep'])['ddd']

            window['logradouro'].update(logradouro)
            window['bairro'].update(bairro)
            window['localidade'].update(localidade)
            window['uf'].update(uf)
            window['ibge'].update(ibge)
            window['ddd'].update(ddd)

        except:
            sg.Popup('Verifique se o campo "CEP" foi preenchido corretamente.\nEm outros caso, verifique a sua internet, caso haja conexão de forma adequada.', font='arial 15', title='CEP NOT FOUND.')
