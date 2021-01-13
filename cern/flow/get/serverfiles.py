#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective : Responde as requisições server files
#  File Name : serverfiles.py
#  File Date : 24/09/2020 14:52
#  File Change : 24/09/2020 14:52
#  File Copyright : Webstrucs 2020

# Native Module Import : urllib.parse
from urllib.parse import urlparse
# Native Module Import : pathlib
from pathlib import PurePath, PurePosixPath
# Native Module Import : os
import os

class ServerFiles:

    # Class-method : analizador de parameter :
    def spark(v_response, v_uri):
        # objeto part, objetivo : tratar os schemas da url :
        o_part = urlparse(v_uri)
        # Acessar a tupla (path), memorizar path na variavel :
        v_path = o_part.path
        # Inserir o path no array, memorizar array na variavel :
        o_array = PurePath(v_path)
        # Memorizar o nome do controller, acessar pelo index dentro do array :
        v_appget = o_array.parts[1]

        # Obtem o arquivo no final do path :
        o_fame = PurePosixPath(v_path).name
        # Separa o nome da extensão do arquivo atribuindo cada valor numa variavel isolada :
        v_file, v_ext = os.path.splitext(o_fame)
        # Array - extensões de arquivos :
        a_ext = [
            ".acc", ".abw", ".arc", ".avi", ".azw", ".bin", ".bmp", ".bz", ".bz2", ".csh", ".css", ".csv", ".doc",
            ".docx", ".eot", ".epub", ".gz", ".gif", ".htm", ".html", ".ico", ".ics", ".jar", ".jpeg", ".jpg",
            ".js", ".json", ".jsonld", ".less", ".mid", ".midi", ".mjs", ".mp3", ".mpeg", ".mpkg",
            ".odp", ".ods", ".odt", ".oga", ".ogv", ".ogx", ".opus", ".otf", ".png", ".pdf", ".php", ".ppt",
            ".pptx", ".rar", ".rtf", ".sass", ".scss", ".sh", ".svg", ".swf", ".tar", ".tif", ".tiff", ".ts",
            ".ttf", ".txt", ".vsd", ".wav", ".weba", ".webm", ".webp", ".woff", ".woff2", ".xhtml", ".xls",
            ".xlsx", ".xml", ".xul", ".yml", ".zip", ".3gp", ".3g2", ".7z"
        ]
        # faz o loop no array comparando as extensões :
        while v_ext in a_ext:
            # Atribui path ao diretorio de arquivos estaticos, memoriza path na variable :
            v_filedir = "cern/" + v_appget + "/"

            # Compara se extensões são as mesmas :
            if v_ext == ".aac":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/aac; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".abw":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-abiword; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".arc":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/octet-stream; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".avi":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/x-msvideo; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".azw":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.amazon.ebook; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".bin":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/octet-stream; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".bmp":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/bmp; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".bz":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cmp/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-bzip; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".bz2":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cmp/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-bzip2; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".csh ":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-csh; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".css":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "css/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/css; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".csv":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/csv; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".doc":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/msword; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".docx":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type",
                            "application/vnd.openxmlformats-officedocument.wordprocessingml.document; charset=utf-8")]
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".eot":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fts/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.ms-fontobject; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".epub":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/epub+zip; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".gz":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-compressed; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".gif":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/gif; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".htm":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/html; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".html":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/html; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ico":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/x-icon; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ics":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/calendar; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".jar":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/java-archive; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".jpeg":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/jpeg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".jpg":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/jpeg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".js":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/javascript; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".json":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/json; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".jsonld":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/ld+json; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".less":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "css/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "plain/text; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".mid":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/midi; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".midi":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/midi; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".mjs":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/javascript; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".mp3":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/mpeg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".mpeg":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/mpeg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".mpkg":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "ist/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.apple.installer+xml; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".odp":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.oasis.opendocument.presentation; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ods":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.oasis.opendocument.spreadsheet; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".odt":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.oasis.opendocument.text; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".oga":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/ogg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ogv":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/ogg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ogx":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/ogg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".opus":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/ogg; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".otf":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fts/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/font-sfnt; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".png":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/png; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".pdf":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/pdf; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ppt":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.ms-powerpoint; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".pptx":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [
                    ("Content-type", "application/vnd.openxmlformats-officedocument.presentationml.presentation; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".rar":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cmp/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/rar; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".rtf":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/rtf; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".sass":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "sty/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/plain; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".scss":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "sty/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/plain; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".sh":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cod/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/x-sh; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".svg":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/svg+xml; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".tar":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cmp/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-tar; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".tif":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/tiff; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".tiff":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fgs/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/tiff; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ts":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/typescript; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".ttf":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fts/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "font/ttf; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".txt":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/plain; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".vsd":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.visio; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".wav":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/x-wav; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".weba":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "audio/webm; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".webm":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/webm; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".webp":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "image/webp; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".woff":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fts/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "font/woff; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".woff2":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "fts/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "font/woff; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".xhtml":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/xhtml+xml; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".xls":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.ms-excel; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".xlsx":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".xml":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/xml; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".xul":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "dcm/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/vnd.mozilla.xul+xml; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".zip":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cmp/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/zip; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".3gp":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/3gpp; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".3gp2":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "med/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "video/3gpp2; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            # Compara se extensões são as mesmas :
            elif v_ext == ".7z":
                # Acessa o arquivo static requisitado :
                o_file = open(v_filedir + "cmp/" + o_fame, "r")
                # Faz a leitura do arquivo :
                s_file = o_file.read()
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/x-7z-compressed; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return s_file

            else:
                # Variable : obtem status de resposta para client browser :
                status = "500 Internal Server Error"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/html; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Method Return Instruction :
                return "Error : 500 Internal Server Error"

            # para a repetição :
            break