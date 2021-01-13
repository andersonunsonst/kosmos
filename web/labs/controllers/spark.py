# Custom Module Import : Rules
# from web.labs.models.rules import Rules
# Custom Module Import : Index
from web.labs.views.index import Index
# Custom Module Import : header, body, footer
# from web.labs.views import header, body, footer
# Custom Module Import : json
import json

# Class Function ->
class Spark:

    # Method Function ->
    def render():

        # Return Function ->
        return Index.view()

        # Return Function ->
        # return (
        #    header.Header.view() +
        #    body.Body.view() +
        #    footer.Footer.view()
        # )

    # Method Function ->
    def query(q_string):

        # Function ->
        v_term = q_string["q"]
        # Return Function ->
        return "Termo Pesquisado : " + v_term
        
    # Method Function ->
    def add(a_inp):

        v_nome = a_inp.getvalue("v_name")
        v_snome = a_inp.getvalue("v_sname")

        # Converte para dicionario
        o_data = dict()
        # Pre-estrutura para o formato json
        o_data["nome"] = v_nome
        o_data["snome"] = v_snome
        # Da a saida no formato json
        v_json = json.dumps(o_data)
        # Method Return Instruction :
        return v_json
