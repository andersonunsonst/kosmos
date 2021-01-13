#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective :
#  File Name : inputforms.py
#  File Date : 25/09/2020 00:28
#  File Change : 25/09/2020 00:28
#  File Copyright : Webstrucs 2020

# Native Module Import : urllib.parse - Divide uma string e organiza em cada componente para analise e interações
from urllib.parse import urlparse
# Native Module Import : pathlib - caminhos do sistema de arquivos orientados a objetos
from pathlib import PurePath, Path
# Native Module Import : import_module - tem como função importar dynamic module
from importlib import import_module
# Custom Module Import : pathlib
import cgi, json

# Custom Class : DatasInput
class InputForms:

    # Custom Class Method : m_parser
    def spark(environ, v_response, v_uri):

        # objeto part, objetivo : tratar os schemas da url :
        o_part = urlparse(v_uri)
        # Acessar a tupla (path), memorizar path na variavel :
        v_path = o_part.path
        # Inserir o path no array, memorizar array na variavel :
        o_array = PurePath(v_path)

        # Memorizar o nome do controller, acessar pelo index dentro do array :
        v_appget = o_array.parts[1]
        # Memorizar o nome do controller, acessar pelo index dentro do array :
        v_conget = o_array.parts[2]
        # Memorizar o nome do method, acessar pelo index dentro do array :
        v_metget = o_array.parts[3]

        # Percorrer ao diretorio da aplicação, atribui path na variavel :
        v_appath = "web/" + v_appget + "/controllers/" + v_conget + ".py"
        # Checar a existência do diretorio comparando com o path requisitado :
        o_appexist = Path(v_appath).exists()
        # Declare variable, title : atribui conversão do texto da primeira letra em maiusculo :
        t_conget = v_conget.title()

        # Condição Se : Compara valores das variaveis :
        if o_appexist == True:
            # Variable : obtem status de resposta para client browser :
            status = "200 OK"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "application/json; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Import dynamic module : acionando o controller and pattern method :
            v_pathmod = "web." + v_appget + ".controllers." + v_conget
            # Import dynamic module : passando como parameter o path atribuido na variable :
            o_module = import_module(v_pathmod)
            # Recupe a class : passada como parameter atruida na variavel class-controller :
            o_class = getattr(o_module, t_conget)
            # Recupe o method : passado como parameter atruido na variavel method-controller :
            o_method = getattr(o_class, v_metget)
            # Function -> Recupera as entradas dos inputs forms
            a_inp = cgi.FieldStorage(environ["wsgi.input"], environ=environ)
            # Instancia o objeto : relacionado como o metodo da classe :
            o_return = o_method(a_inp)
            # Return, dispara o evento de acesso ao method da class importada :
            return o_return

        if o_appexist == False:
            # Variable : obtem status de resposta para client browser :
            status = "404 Not Found"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "application/json; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Converte para dicionario
            o_data = dict()
            # Pre-estrutura para o formato json
            o_data["term"] = "Error : 404 Not Found<br>O servidor não pode encontrar o recurso solicitado."
            # Da a saida no formato json
            v_json = json.dumps(o_data)
            # Output a requisição do client browser:
            return v_json