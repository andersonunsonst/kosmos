#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective : Define o directory principal para o dominio do projeto
#  File Name : domaindir.py
#  File Date : 24/09/2020 14:42
#  File Change : 24/09/2020 14:27
#  File Copyright : Webstrucs 2020

# Native Module Import : urllib.parse - Divide uma string e organiza em cada componente para analise e interações
from urllib.parse import urlparse
# Native Module Import : pathlib - Caminhos do sistema de arquivos orientados a objetos
from pathlib import PurePath

class DomainDir:

    def spark(v_response, v_url):

        # objeto part, objetivo : tratar os schemas da url :
        o_part = urlparse(v_url)
        # Acessar a tupla (path), memorizar path na variavel :
        v_path = o_part.path
        # Inserir o path no array, memrizar array na variavel :
        o_array = PurePath(v_path)

        # Memorizar o nome do controller, acessar pelo index dentro do array :
        v_appget = o_array.parts[0]
        # Compara se a variaveis são iguais ?
        if v_path == v_appget:
            # DEFINE MAIN APP TO DOMAIN : IMPORT CUSTOM MODULE
            from web.labs.controllers.spark import Spark
            # Variable : obtem status de resposta para client browser :
            status = "200 OK"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Module-Method Access, return : Runcode
            return Spark.render()

        else:
            # Variable : obtem status de resposta para client browser :
            status = "500 Internal Server Error"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Method Return Instruction :
            return "Error : 500 Internal Server Error"