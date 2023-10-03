import re

def cpf_valido(cpf):
    return len(cpf) == 11

def nome_valido(nome):
    return not nome.isalpha()

def rg_valido(rg):
    return len(rg) == 9

def celular_valido(celular):
    """ verifica se o celular é válido (00 0000-0000)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo,celular) 
    return resposta
    