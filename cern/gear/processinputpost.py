#  Project Name : Kosmos
#  Description : Web Framework MVC
#  Language : Python 3.8.5
#  Web Developer : João Carlos
#  File Objective :
#  File Name : processinputpost.py
#  File Date : 25/09/2020 00:48
#  File Change : 25/09/2020 00:48
#  File Copyright : Webstrucs 2020

# Function -> Importa module cgi que trata form request e re (regex)
import re

# Class Function ->
class ProcessInputPost:

    # Method Function ->
    def spark(v_response, v_uri, v_inp):

        # Function -> Convert to tuple
        a_inp = (v_inp,)
        # Function -> Converte tuple to string :
        o_inp = str(a_inp)
        # Function -> Remove parenteses para checagem de dados :
        v_inp = re.sub("[()]", " ", o_inp)
        # Function ->
        from cern.safe.threatdetect import ThreatDetect
        # Function ->
        return ThreatDetect.m_post(v_response, v_uri, v_inp)