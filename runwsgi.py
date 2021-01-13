#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective : Estabelecer comunicação entre o servidor web e applicação web
#  File Name : runwsgi.py
#  File Date : 24/09/2020 03:04
#  File Change : 24/09/2020 03:04
#  File Copyright : Webstrucs 2020

# Function -> Importa o module que gera o servidor de teste
from wsgiref.simple_server import make_server
# Function -> Importa a função que gerencia client request
from wsgiref.util import request_uri
# Function -> Importa module cgi que trata form request
import cgi

# Function -> Principal metodo que recebe parametros que trata request e response
def application(environ, v_response):

    # Function -> Recupera o metodo da requisição
    v_mtd = environ["REQUEST_METHOD"]
    # Function -> Recupera a requisição da uri
    v_uri = request_uri(environ, include_query=True)
    # Function -> Recupera as entradas dos inputs forms
    v_inp = cgi.FieldStorage(environ["wsgi.input"], environ=environ)

    # Function -> Compara o tipo de metodo da requisição
    if v_mtd == "GET":
        # Function -> Importar classe para processar dados
        from cern.gear.processuriget import ProcessUriGet
        # Function -> Passando parametros para o metodo da classe
        return [str(ProcessUriGet.spark(v_response, v_uri)).encode("utf-8")]
    
    # Function -> Compara o tipo de metodo da requisição
    if v_mtd == "POST":
        # Function -> Importar classe para processar dados
        from cern.gear.processinputpost import ProcessInputPost
        # Function -> Passando parametros para o metodo da classe
        return [str(ProcessInputPost.spark(v_response, v_uri, v_inp)).encode("utf-8")]

with make_server('', 8000, application) as httpd:
    # Function -> Imprime no terminal reference
    print(
        'Running Kosmos Application\n'
        'Browser Access - http://127.0.0.1:8000\n'
        'Crl+c for exit command or Crl+z for stop'
    )
    # Function -> Sirva até que o processo seja encerrado
    httpd.serve_forever()