# Class-Header : modelo de cabeçalho html.
class FooterHtml:
    # class-method : renderizar o cabeçalho html.
    def writecode(v_appget):
        # class-attribute : public.
        v_strucs = '''
# Class Header : modelo de cabeçalho html.
class Footer:
    # class-method :
    def view():
        # class-attribute :
        v_html5 = """
        <!-- Compiled and minified JavaScript -->
        <script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
        <!-- Load custom jquery -->
        <script src="/''' + v_appget + '''/assets/cod/jquery.ext.js"></script>
        <!--Custom framework design-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <!--Custom framework design-->
        <script>$(document).ready(function(){ });</script>
    </body>
</html>
        """
        return v_html5
        '''
        return v_strucs