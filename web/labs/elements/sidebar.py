
# Class Navbar : modelo de barra de navegation.
class Toobar:
    # class-method : view
    def view():
        # class-attribute :
        v_html5 = """
        <nav id="slide-out" class="toolbar sidenav-fixed">
            <a class="btn waves-effect transparent lighten-2"></a>
            <a href="" class="i-btn waves-effect transparent lighten-2 tooltipped" data-position="right" data-tooltip=". . .">
                <span class="mdi-24px mdi mdi-view-dashboard-outline" style="color:#757575;"></span>
            </a>
        </nav>
        """
        return v_html5