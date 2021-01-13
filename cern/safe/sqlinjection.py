# Native Module, Import : re, regex
import re

# Name Class : SqlInjection
class SqlInjection:

    # Class Method : m_get
    def m_get(v_response, v_uri):

        # Regex Condition - exist if check
        if re.search(
            r"admin' --|admin' #|admin'/[*]|' or 1=1--|' or 1=1#|' or 1=1/[*]|'[)] or '1'='1--|;|"
            r"'[)] or [(]'1'='1--|and|alter table|between|create|create database|create table|"
            r"create index|create view|delete|grant|revoke|commit|rollback|savepoint|drop database|"
            r"drop index|drop table|exists|group by|having|insert|insert into|inner join|left join|"
            r"right join|full jon|like|order by|select|select[*]|select distinct|select into|select top|"
            r"truncate table|union|union all|update|where",
            v_uri, re.IGNORECASE
        ):
            # Variable : obtem status de resposta para client browser :
            status = "400 Bad Request"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "application/json; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # any words end with ing?
            return "Hacker Attempt: True, Threat : Sql Injection, Syntax :" + v_uri

        else: # return "Hancking: False, Threat : Not Found, Syntax: No threats detected in the string : " + v_uri
            # Import custom module-class ( DirectUrlGet )
            from cern.gear.directuriget import DirectUriGet
            # Function : Processar a requisição enviando pelo parâmetro
            return DirectUriGet.spark(v_response, v_uri)

    def m_post(v_response, v_uri, v_inp):

        # Regex Condition - exist if check
        if re.search(
            r"admin' --|admin' #|admin'/[*]|' or 1=1--|' or 1=1#|' or 1=1/[*]|'[)] or '1'='1--|;|"
            r"'[)] or [(]'1'='1--|and|alter table|between|create|create database|create table|"
            r"create index|create view|delete|grant|revoke|commit|rollback|savepoint|drop database|"
            r"drop index|drop table|exists|group by|having|insert|insert into|inner join|left join|"
            r"right join|full jon|like|order by|select|select[*]|select distinct|select into|select top|"
            r"truncate table|union|union all|update|where",
            v_uri, re.IGNORECASE
        ):
            # Variable : obtem status de resposta para client browser :
            status = "400 Bad Request"
            # Variable : obtem cabeçalho http para o browser do client
            headers = [("Content-type", "application/json; charset=utf-8")]
            # Function : Envio de variable para o client browser :
            v_response(status, headers)
            # Output :
            return "Hacker Attempt: True, Threat : Sql Injection, Syntax :" + v_uri

        else:
            # Regex Condition - exist if check
            if re.search(
                r"admin' --|admin' #|admin'/[*]|' or 1=1--|' or 1=1#|' or 1=1/[*]|'[)] or '1'='1--|;|"
                r"'[)] or [(]'1'='1--|and|alter table|between|create|create database|create table|"
                r"create index|create view|delete|grant|revoke|commit|rollback|savepoint|drop database|"
                r"drop index|drop table|exists|group by|having|insert|insert into|inner join|left join|"
                r"right join|full jon|like|order by|select|select[*]|select distinct|select into|select top|"
                r"truncate table|union|union all|update|where",
                str(v_inp), re.IGNORECASE
            ):
                # Variable : obtem status de resposta para client browser :
                status = "400 Bad Request"
                # Variable : obtem cabeçalho http para o browser do client
                headers = [("Content-type", "application/json; charset=utf-8")]
                # Function : Envio de variable para o client browser :
                v_response(status, headers)
                # Output :
                return "Hacker Attempt: True, Threat : Sql Injection, Syntax :" + v_inp

            else:
                # Custom Module, Import : postexit
                from cern.gear.directinputpost import DirectInputPost
                # Module Access, return : SqlInjection
                return DirectInputPost.spark(v_response, v_uri, v_inp)