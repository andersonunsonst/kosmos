#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective :
#  File Name : directinputpost.py
#  File Date : 25/09/2020 01:11
#  File Change : 25/09/2020 01:11
#  File Copyright : Webstrucs 2020

import cgi

# Name Class : DirectInputPost
class DirectInputPost:

    # Class Method : m_parser
    def spark(v_response, v_uri, v_inp):

        # Variable : obtem status de resposta para client browser :
        status = "200 OK"
        # Variable : obtem cabeçalho http para o browser do client
        headers = [("Content-type", "audio/aac; charset=utf-8")]
        # Function : Envio de variable para o client browser :
        v_response(status, headers)

        v_entry = cgi.FieldStorage()

        v_nome = v_entry.getvalue("v_name")
        # v_snome = a_inp.getvalue("v_sname")

        return v_nome

'''

        # Converte para dicionario
        o_data = dict()
        # Pre-estrutura para o formato json
        o_data["nome"] = v_nome
        o_data["snome"] = v_snome
        # Output no formato json
        v_json = json.dumps(o_data)
        # Method Return Instruction :
        return v_json
        
        # 1. Monta a string :
        v_build_one = "FieldStorage(None, None, [MiniFieldStorage("
        v_build_two = "), MiniFieldStorage('"
        v_build_tre = ")])"
        v_build_for = "[MiniFieldStorage("

        v_str_one = re.sub(r"FieldStorage None, None, \[MiniFieldStorage", v_build_one, v_inp)
        v_str_two = re.sub(r" , MiniFieldStorage '", v_build_two, v_str_one)
        v_str_tre = re.sub(r" ]", v_build_tre, v_str_two)
        v_str_for = re.sub(r"\[MiniFieldStorage\( ", v_build_for, v_str_tre)

        # Import custom module-class ( InputForms )
        from cern.flow.post.inputforms import InputForms
        # Function : Processar a requisição enviando pelo parâmetro
        return InputForms.spark(v_response, v_uri, v_inp)
'''