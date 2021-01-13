# Class-ContentStrucs : modelo de conteudo.
class BodyHtml:
    # class-method : renderizar o content dentro body.
    def writecode(v_appget):
        # convert-variable :
        t_appget = v_appget.capitalize()
        # class-attribute : public.
        v_strucs = '''
# Class Body : Template to content inside tag <main>
class Body:
    # class-method :
    def view():
        # class-attribute :
        v_html5 = """
            Insert Tags Here (inside body)
        """
        return v_html5
        '''
        return v_strucs