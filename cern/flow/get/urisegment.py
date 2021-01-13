#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective : Dinamiza o roteamento http dos projetos
#  File Name : urisegment.py
#  File Date : 24/09/2020 19:30
#  File Change : 24/09/2020 19:30
#  File Copyright : Webstrucs 2020

# Native Module Import : urllib.parse - Divide uma string e organiza em cada componente para analise e interações
from urllib.parse import urlparse
# Native Module Import : pathlib - caminhos do sistema de arquivos orientados a objetos
from pathlib import PurePath, Path
# Native Module Import : import_module - tem como função importar dynamic module
from importlib import import_module

# Class DynamicPath, objetivo : estabelecer path de acesso dinâmico :
class UriSegment:

    # Method Class, objetivo : analisar dados no parametro recebido :
    def spark(v_response, v_uri):
        # objeto part, objetivo : tratar os schemas da url :
        o_part = urlparse(v_uri)
        # Acessar a tupla (path), memoriza path na variavel :
        v_path = o_part.path
        # Inserir o path no array, memoriza array na variavel :
        o_array = PurePath(v_path)

        # Memorizar o nome do controller, acessar pelo index dentro do array :
        v_appget = o_array.parts[1]
        # Percorrer ao diretorio da aplicação, atribui path na variavel :
        v_appath = "web/" + v_appget
        # Checar a existência do diretorio comparando com o path requisitado :
        o_appexist = Path(v_appath).exists()
        # Monta a rota dois da aplicação, atribui valor na variavel :
        v_pathone = "/" + v_appget

        # Condição Se : Compara valores das variaveis :
        if o_appexist == True and v_path == v_pathone:
            # Variable : obtem status de resposta para client browser :
            status = "200 OK"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Import dynamic module : acionando o controller and pattern method :
            v_pathmod = "web." + v_appget + ".controllers.spark"
            # Import dynamic module : passando como parameter o path atribuido na variable :
            o_module = import_module(v_pathmod)
            # Recupera a class : passada como parameter atruida na variavel class-controller :
            o_class = getattr(o_module, "Spark")
            # Recupera o methodo : passado como parameter atruido na variavel method-controller :
            o_method = getattr(o_class, "render")
            # Instancia o objeto : relacionado como o metodo da classe :
            o_return = o_method()
            # Retorna o resultado do method of class :
            return o_return

        # Condição Se : Compara valor da variavel :
        if o_appexist == False:
            # Variable : obtem status de resposta para client browser :
            status = "404 Not Found"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output a requisição do client browser:
            return "Error : 404 Not Found<br>O servidor não pode encontrar o recurso solicitado."

        # Memorizar o nome do controller, acessar pelo index dentro do array :
        v_conget = o_array.parts[2]
        # Percorrer ao diretorio do controller, atribui path na variavel :
        v_conpath = "web/" + v_appget + "/controllers/" + v_conget + ".py"
        # Checar a existência do diretorio comparando com o path requisitado :
        o_conexist = Path(v_conpath).exists()
        # Declare variable, .capitalize : atribui conversão do texto da primeira letra em maiusculo :
        t_conget = v_conget.capitalize()
        # Declare variable, path : monta rota do controlador da aplicação :
        v_pathtwo = "/" + v_appget + "/" + v_conget

        # Condição (Se), compara valores de variaveis :
        if o_conexist == True and v_path == v_pathtwo:
            # Variable : obtem status de resposta para client browser :
            status = "400 Bad Request"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output a requisição do client browser:
            return "Error : 400 Bad Request<br>O servidor não entendeu a requisição pois está com uma sintaxe inválida"

        # Condição (Se), compara valores de variaveis :
        if o_conexist == False:
            # Variable : obtem status de resposta para client browser :
            status = "404 Not Found"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output a requisição do client browser:
            return "Error : 404 Not Found<br>O servidor não pode encontrar o recurso solicitado."

        # Memorizar o nome do method, acessar pelo index dentro do array :
        v_metget = o_array.parts[3]
        # Declare variable, path : monta rota do controlador da aplicação :
        v_pathtre = "/" + v_appget + "/" + v_conget + "/" + v_metget

        # Condição (Se), compara valores de variaveis :
        if v_path == v_pathtre:
            # Import dynamic module : acionando o controller and pattern method :
            v_pathmod = "web." + v_appget + ".controllers." + v_conget
            # Import dynamic module : passando como parameter o path atribuido na variable :
            o_module = import_module(v_pathmod)
            # Recupe a class : passada como parameter atruida na variavel class-controller :
            o_class = getattr(o_module, t_conget)
            # Acessar a classe controller e checa a existencia do method :
            o_metexist = hasattr(o_class, v_metget)
            # Condiciona a existencia do metodo, caso exista :
            if o_metexist == True:
                # Variable : obtem status de resposta para client browser :
                status = "200 OK"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/html; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Recupe o method : passado como parameter atruido na variavel method-controller :
                o_method = getattr(o_class, v_metget)
                # Instantiate the object: related to the class method:
                o_return = o_method()
                # Output a requisição do client browser:
                return o_return

            if o_metexist == False:
                # Variable : obtem status de resposta para client browser :
                status = "404 Not Found"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "text/html; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output a requisição do client browser:
                return "Error : 404 Not Found<br>O servidor não pode encontrar o recurso solicitado."

        # Memorizar o nome do method, acessar pelo index dentro do array :
        v_parone = o_array.parts[4]
        # Declare variable, path : monta rota do controlador da aplicação :
        v_pathfor = "/" + v_appget + "/" + v_conget + "/" + v_metget + "/" + v_parone

        # Condição (Se), compara valores de variaveis :
        if v_path == v_pathfor:
            # Variable : obtem status de resposta para client browser :
            status = "200 OK"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "text/html; charset=utf-8")]
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
            # Instancia o objeto : relacionado como o metodo da classe :
            o_return = o_method(v_parone)
            # Return, dispara o evento de acesso ao method da class importada :
            return o_return
