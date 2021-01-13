#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective :
#  File Name : structure.py
#  File Date : 24/09/2020 23:03
#  File Change : 24/09/2020 23:03
#  File Copyright : Webstrucs 2020

# Native Module Import : argparse
import argparse
# Native Module Import : os, subprocess
import os, subprocess
# Custom Module Import : CustomJquery
from cern.bulk.customjquery import CustomJquery
# Custom Module Import : StylesCss
from cern.bulk.stylescss import StylesCss
# Custom Module Import : TopbarHtml
from cern.bulk.topbarhtml import TopbarHtml
# Custom Module Import : SidebarHtml
from cern.bulk.sidebarhtml import SidebarHtml
# Custom Module Import : MvcStrucs
from cern.bulk.mvcstrucs import MvcStrucs
# Custom Module Import : HeaderHtml
from cern.bulk.headerhtml import HeaderHtml
# Custom Module Import : BodyHtml
from cern.bulk.bodyhtml import BodyHtml
# Custom Module Import : FooterHtml
from cern.bulk.footerhtml import FooterHtml

v_parse = argparse.ArgumentParser(description='Command to call structural function, "app"')
v_parse.add_argument('parone', action='store', type=str, help='Define o argumento "app"')
v_parse.add_argument('partwo', action='store', type=str, help='Define o nome para o app')

v_args = v_parse.parse_args()

v_appcom = v_args.parone
v_appget = v_args.partwo

if v_appcom == "app" and v_appget != "":

    # Adiciona o diretorio root da aplicação recebendo o nome pela linha de comando :
    os.mkdir("web/" + v_appget +"")
    # Acessar o path da aplicação :
    os.chdir("web/" + v_appget +"")
    # Retornar o diretório de trabalho atual de um processo :
    os.getcwd()

    # Estrutura diretorios para organizar codigos da aplicação :
    os.mkdir("assets")      # pasta para arquivos subdiretorios e arquivos assistentes ...
    os.mkdir("assets/cod")  # pasta para arquivos tipo codigo (.js, .json, .xml ...)
    # Adicina arquivo de estilos css no diretorio relacionado :
    subprocess.run(["touch", "assets/cod/jquery.ext.js"])
    # Abre e lê arquivo js :
    with open("assets/cod/jquery.ext.js", "w") as v_file:
        # Obter estilo css por meio da class, escrever codigo no arquivo css
        v_file.write(CustomJquery.writecode(v_appget))

    os.mkdir("assets/cmp")  # pasta para arquivos tipo compactados...
    os.mkdir("assets/css")  # para para arquivos cascating style sheet (.css)
    # Adicina arquivo de estilos css no diretorio relacionado :
    subprocess.run(["touch", "assets/css/materialize.ext.css"])
    # Abre e lê arquivo css :
    with open("assets/css/materialize.ext.css", "w") as v_file:
        # Obter estilo css por meio da class, escrever codigo no arquivo css
        v_file.write(StylesCss.writecode())

    os.mkdir("assets/dcm")  # pasta para arquivos do tipo documentos
    os.mkdir("assets/fgs")  # pasta para arquivos de tipo imagens, vetores, gifs etc...
    os.mkdir("assets/fts")  # pasta para arquivos de tipo fontes...
    os.mkdir("assets/ist")  # pasta para arquivos tipo instalaveis
    os.mkdir("assets/med")  # pasta para arquivos de tipo media
    os.mkdir("assets/sty")  # pasta para arquivos de style ( .sass, .scss )

    os.mkdir("elements")       # pasta para arquivos de classes customizadas
    subprocess.run(["touch", "elements/topbar.py"])
    with open("elements/topbar.py", "w") as v_file:
        v_file.write(TopbarHtml.writecode())

    subprocess.run(["touch", "elements/sidebar.py"])
    with open("elements/sidebar.py", "w") as v_file:
        v_file.write(SidebarHtml.writecode())

    os.mkdir("controllers") # pasta para arquivos controllers
    # Adicina arquivo class-controller no diretorio relacionado :
    subprocess.run(["touch", "controllers/spark.py"])
    # Abre e lê arquivo class-controller :
    with open("controllers/spark.py", "w") as v_file:
        # Atribui parameter ao method da class :
        v_file.write(MvcStrucs.m_controller(v_appget))

    os.mkdir("helpes") # pasta para funções customizadas :
    os.mkdir("language") # pasta para arquivos de traduções :

    os.mkdir("models")  # pasta para arquivos que trata regras de database python (.py)
    subprocess.run(["touch", "models/rules.py"])
    with open("models/rules.py", "w") as v_file:
        v_file.write(MvcStrucs.m_model())

    os.mkdir("views")   # pasta para aquivos python que redenriza html por meio de extensão (.py)
    subprocess.run(["touch", "views/index.py"])
    with open("views/index.py", "w") as v_file:
        v_file.write(MvcStrucs.m_views(v_appget))

    subprocess.run(["touch", "views/header.py"])
    with open("views/header.py", "w") as v_file:
        v_file.write(HeaderHtml.writecode(v_appget))

    subprocess.run(["touch", "views/body.py"])
    with open("views/body.py", "w") as v_file:
        v_file.write(BodyHtml.writecode(v_appget))

    subprocess.run(["touch", "views/footer.py"])
    with open("views/footer.py", "w") as v_file:
        v_file.write(FooterHtml.writecode(v_appget))