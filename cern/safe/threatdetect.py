
# Native Module, Import : re, regex
import re, cgi

# Name Class : ThreatDetect
class ThreatDetect:

    # Class Method : m_get
    def m_get(v_response, v_uri):

        # Regex Condition - exist if check
        if re.search(
                r"=",
                v_uri, re.IGNORECASE
        ):
            # return "Method Type: Get, Request : Query String - Syntax: " + v_uri
            # Custom Module, Import : crositescript
            from cern.safe.crositescript import CrositeScript
            # Module Access, return : CrositeScript
            return CrositeScript.m_get(v_response, v_uri)

        else:
            # return "Method Type: Get, Request : Root, Segments, Statics Files - Syntax: " + v_uri
            # Custom Module, Import : crositescript
            from cern.safe.crositescript import CrositeScript
            # Module Access, return : CrositeScript
            return CrositeScript.m_get(v_response, v_uri)

    # Class Method : m_post
    def m_post(v_response, v_uri, v_inp):

        # Custom Module, Import : crositescript
        from cern.safe.crositescript import CrositeScript
        # Module Access, return : CrositeScript
        return CrositeScript.m_post(v_response, v_uri, v_inp)