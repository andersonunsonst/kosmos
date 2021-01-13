#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective :
#  File Name : querystring.py
#  File Date : 24/09/2020 22:04
#  File Change : 24/09/2020 22:04
#  File Copyright : Webstrucs 2020

# Module Python : urllib.parse - Divide uma string e organiza em cada componente para analise e interações
from urllib.parse import urlparse, unquote, parse_qsl
# Module Python : pathlib - Caminhos do sistema de arquivos orientados a objetos
from pathlib import Path, PurePath
# Module Python : imporlib - permite importar modules de maneira dyanamic :
from importlib import import_module

class QueryString:

    def spark(v_response, v_uri):

        # Function -> Obtem os componentes
        o_part = urlparse(v_uri)
        # Function -> Obtem valor do componente path
        v_path = o_part.path
        # Function -> Obtem valor do componente query
        v_query = o_part.query
        # Function -> Acessa o valor do componente path
        o_array = PurePath(v_path)
        # Function -> Desmembra o path e atribui o indice para identificação
        v_appget = o_array.parts[1]

        # Function -> Faz referência ao caminho da aplicação
        v_appath = "web/" + v_appget
        # Function -> Checa a existência
        o_appexist = Path(v_appath).exists()
        # Function -> Converte app name to path
        v_pathone = "/" + v_appget
        # Function -> Objeto que trata caracteres indesejaveis
        v_charc = unquote(v_query)
        # Function -> Converte querystring para dicionario
        d_query = dict(parse_qsl(v_charc))
        # Function -> Converte querystring para dicionario
        q_string = d_query

        # Function ->
        if o_appexist == True and v_path == v_pathone:
            # Function -> obtem status de resposta para client browser :
            status = "200 OK"
            # Function -> obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function -> Envio de variable para o client browser :
            v_response(status, headers)
            # Function ->
            v_pathmod = "web." + v_appget + ".controllers.spark"
            # Function ->
            v_module = import_module(v_pathmod)
            # Function ->
            v_class = getattr(v_module, "Spark")
            # Function ->
            v_method = getattr(v_class, "query")
            # Function ->
            v_movepar = v_method(q_string)
            # Function ->
            return v_movepar

        if o_appexist == False:
            # Variable : obtem status de resposta para client browser :
            status = "404 Not Found"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output a requisição do client browser:
            return "Error : 404 Not Found<br>O servidor não pode encontrar o recurso solicitado."