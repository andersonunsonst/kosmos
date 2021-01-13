#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective : Direcionar requisições URLS do tipo GET
#  File Name : directuriget.py
#  File Date : 24/09/2020 03:54
#  File Change : 24/09/2020 03:54
#  File Copyright : Webstrucs 2020

# Function ->
from urllib.parse import urlparse
# Function ->
from pathlib import PurePath, PurePosixPath
# Function ->
import os

# Function ->
class DirectUriGet:

    # Function ->
    def spark(v_response, v_uri):

        # Function -> Obtem os componentes
        o_part = urlparse(v_uri)
        # Function -> Obtem valor do componente path
        v_path = o_part.path
        # Function -> Obtem valor do componente query
        v_query = o_part.query
        # Function -> Acessa o valor do componente path
        o_array = PurePath(v_path)
        # Function -> Indexa ("0") para ("/") fazendo reference to domain
        v_domain = o_array.parts[0]

        # URI TYPE : DOMAIN
        # Function -> Compara se o valor fo path são iguais ("/")
        if v_path == v_domain:
            # Function ->
            from cern.flow.get.domaindir import DomainDir
            # Function ->
            return DomainDir.spark(v_response, v_uri)

        # URI TYPE : CLIENT FILES
        # Function ->
        v_appget = o_array.parts[1]
        # Function ->
        o_fame = PurePosixPath(v_path).name
        # Function ->
        v_file, v_ext = os.path.splitext(o_fame)
        # Function ->
        if v_appget != "util" and v_ext != "":
            # Function ->
            from cern.flow.get.clientfiles import ClientFiles
            # Function ->
            return ClientFiles.spark(v_response, v_uri)

        # URI TYPE : SERVER FILES
        # Function ->:
        v_appget = o_array.parts[1]
        # Function ->
        o_fame = PurePosixPath(v_path).name
        # Function ->
        v_file, v_ext = os.path.splitext(o_fame)
        # Function ->
        if v_appget == "util" and v_ext != "":
            # Function ->
            from cern.flow.get.serverfiles import ServerFiles
            # Function ->
            return ServerFiles.spark(v_response, v_uri)

        # URI TYPE : SEGMENT URL
        # Function ->
        if v_path != v_domain and v_query == "":
            # Function ->
            from cern.flow.get.urisegment import UriSegment
            # Function ->
            return UriSegment.spark(v_response, v_uri)

        # URI TYPE : QUERYSTRING
        # Function ->
        if v_path != v_domain and v_query != "":
            # Function ->
            from cern.flow.get.querystring import QueryString
            # Function ->
            return QueryString.spark(v_response, v_uri)