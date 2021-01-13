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