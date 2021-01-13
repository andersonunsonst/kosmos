
# Class Navbar : modelo de barra de navegation.
class Topbar:
    # class-method : view
    def view():
        # class-attribute :
        v_html5 = """
        <div class="navbar-fixed">
            <nav class="white navbar">
                <div class="nav-wrapper">
                    <a href="#" data-target="slide-out" class="i-menu sidenav-trigger">
                        <i class="orange-text text-darken-4 material-icons">menu</i>
                    </a>
                    <a href="#!" class="tooltipped brand-logo" data-position="right" data-tooltip="One Page Enterprise">
                    </a>
                    <ul class="right hide-on-med-and-down">
                        <li><a href="#" class="grey-text text-darken-2"><span class="mdi mdi-apps"></span></a></li>   
                    </ul>
                </div>
            </nav>
        </div>
        """
        return v_html5
        