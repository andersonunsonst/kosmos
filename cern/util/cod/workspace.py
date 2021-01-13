'''
Ref. O Senhor é a minha luz e a minha salvação; a quem temerei? O Senhor é a força da minha vida; de quem me recearei ?
Salmos 27:1 - Toda Glória e Honra sejam sua Senhor

# Native Module Import : shutil
from shutil import copy2

class HandleFile:

    def m_copy(v_appget):

        v_src = "cern/util/fgs/build.svg"
        v_dst = "web/" + v_appget + "/assets/fgs"

        return copy2(v_src, v_dst)

#result = re.sub('abc',  '',    input)           # Delete pattern abc
#result = re.sub('abc',  'def', input)           # Substituir pattern abc -> def
#result = re.sub(r'\s+', ' ',   input)           # Eliminate duplicate whitespaces using wildcards
#result = re.sub('abc(def)ghi', r'\1', input)    # Substituir a string with a part of itself

        n_nome = a_inp.getvalue("v_name")
        n_snome = a_inp.getvalue("v_sname")

        # Converte para dicionario
        o_data = dict()
        # Pre-estrutura para o formato json
        o_data["nome"] = n_nome
        o_data["snome"] = n_snome
        # Da a saida no formato json
        v_json = json.dumps(o_data)
        # Method Return Instruction :
        return v_json

str_valid = FieldStorage(None, None, [MiniFieldStorage('v_name', 'João'), MiniFieldStorage('v_sname', 'Aguiar')])
v_erroroo = FieldStorage None, None, [MiniFieldStorage 'v_name', 'João' , MiniFieldStorage 'v_sname', 'Aguiar' ]

# 1. Desmonta a string :
v_part_one = "FieldStorage None, None, [MiniFieldStorage"
v_part_two = " , MiniFieldStorage "
v_part_tre = "' ]"

# 2. Monta a string :
v_build_one = "FieldStorage(None, None, [MiniFieldStorage("
v_build_two = "), MiniFieldStorage("
v_build_tre = ")])"
v_build_for = "[MiniFieldStorage("

v_str_one = re.sub(r"FieldStorage None, None, \[MiniFieldStorage", v_build_one, v_error)
v_str_two = re.sub(r" , MiniFieldStorage '", v_build_two, v_str_one)
v_str_tre = re.sub(r" ]", v_build_tre, v_str_two)
v_str_for = re.sub(r"\[MiniFieldStorage\( ", v_build_for, v_str_tre)

print(v_str_for)

# method of class FieldStorage
def __init__(self, fp=None, headers=None, outerboundary=b'',
                 environ=os.environ, keep_blank_values=0, strict_parsing=0,
                 limit=None, encoding='utf-8', errors='replace',
                 max_num_fields=None):
'''

import re

# Recebo a string desmontada :
v_inp = "FieldStorage None, None, [MiniFieldStorage 'v_name', 'João' , MiniFieldStorage 'v_sname', 'Aguiar' ]"

# Preparo a montagem dos objetos FieldStorage and MiniFieldStorage :
v_build_one = "FieldStorage(None, None, [MiniFieldStorage("
v_build_two = "), MiniFieldStorage('"
v_build_tre = ")])"
v_build_for = "[MiniFieldStorage("

# Use expressões regulares para montar o dado como se fosse original }:
v_str_one = re.sub(r"FieldStorage None, None, \[MiniFieldStorage", v_build_one, v_inp)
v_str_two = re.sub(r" , MiniFieldStorage '", v_build_two, v_str_one)
v_str_tre = re.sub(r" ]", v_build_tre, v_str_two)
v_str_for = re.sub(r"\[MiniFieldStorage\( ", v_build_for, v_str_tre)
v_str_fiv = re.sub(r"FieldStorage\(None, None, ", "", v_str_for)
v_str_six = re.sub(r"\]\)", "", v_str_fiv)
v_str_sev = re.sub(r"\[", "", v_str_six)

# Importo o modulo cgi para instanciar a classe FieldStorage :
from cgi import FieldStorage

v_field = FieldStorage()
v_field.list = [v_str_sev]
print(v_field)