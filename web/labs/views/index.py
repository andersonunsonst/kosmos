# Class Index : modelo controller.
class Index:
    # class-method : screen
    def view():
        # class-attribute : public.
        v_html5 = '''
<!DOCTYPE html>
<html lang="pt" dir="ltr">
    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <meta name="description" content=""/>
        <meta name="keywords" content=""/>

        <!-- Favicon -->
        <link  href="/util/fgs/ksm.svg" rel="shortcut icon"/>
        <!--Import Google Icon -->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <!--Import Material Design Icons-->
        <link href="https://cdn.materialdesignicons.com/5.6.55/css/materialdesignicons.min.css" rel="stylesheet">
        <!--Import Google Font -->
        <link href="https://fonts.googleapis.com/css?family=Catamaran&display=swap" rel="stylesheet">
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        <!--Custom framework design-->
        <link href="/util/css/materialize.ext.css" rel="stylesheet" type="text/css">
        
        <!-- Page Title -->
        <title>Kosmos - Aplicação (Labs) em Funcionamento.</title>

    </head>
    <body class="">

        <!-- sidenav content -->
        <ul id="slide-out" class="sidenav">
            <li>
                <div class="user-view">
                    <div class="background">
                    <img src="#">
                </div>
                <a href="#user"><img class="circle" src="#"></a>
                <a href="#name"><span class="white-text name">Kosmos</span></a>
                <a href="#email"><span class="white-text email">@</span></a>
            </li>
                <!--<a href="#!"><i class="material-icons">cloud</i>First Link With Icon</a></li>-->
                <li><a href="#!">Second Link</a></li>
                <li><div class="divider"></div></li>
                <li><a class="subheader">Subheader</a></li>
                <li><a class="waves-effect" href="#!">Third Link With Waves</a></li>
        </ul>
    
        <!-- navbar content -->
        <header class="navbar-fixed">
            <nav class="navbar-1">
            <div class="nav-wrapper">
                <a href="#" data-target="slide-out" class="menu-1 sidenav-trigger"><i class="orange-text text-darken-4 material-icons">menu</i></a>
                <a href="#!" class="tooltipped brand-logo" data-position="right" data-tooltip="One Page Enterprise">
                    <h1 class="title-1 purple-text text-darken-4">Kosmos</h1>
                </a>
                <ul class="right hide-on-med-and-down">
                    <li><a href="#" class="purple-text text-darken-4">Documentação</a></li>
                    <li><a href="#" class="purple-text text-darken-4">Tutoriais</a></li>
                    <li><a href="#" class="purple-text text-darken-4">Issues</a></li>
                </ul>
            </div>
            </nav>
        </header>


        <!-- main content -->
        <main>
            <!-- section content : -->
            <section class="grid-desc-2 row" id="">
                <div class="block-left-2 col s12 m12 l6 xl6">
                    <img src="/util/fgs/build.svg" class="util-zoom-1">
                </div>
                <div class="block-right-2 col s12 m12 l6 xl6">
                    <h2 class="subtitle-4 purple-text text-darken-4">Projeto Labs</h2>
                    <p class="paragraph-4 grey-text text-darken-2">
                        Estruturas, funcionalidades e recursos foram implementados, consulte 
                        a documentação, aprenda com os tutoriais, relate issues, aperfeiçoe 
                        o seu aprendizado e desenvolva qualquer tipo de solução web.
                    </p>
                    <div style="width: 200px; height: auto; margin-left: 80px;"><br>
                        <!---->
                        <input id="v-name" type="text" placeholder="Nome">
                        <input id="v-sname" type="text" placeholder="Sobre Nome">
                        <a class="purple darken-4 waves-effect waves-light btn-large"></a><br>
                        <span class="alert-primary"></span>
                    </div>
                </div>
            </section>
        </main>
        
        <footer class="page-footer grey lighten-5">
            <div class="footer-copyright">
                <div class="container purple-text text-darken-4">
                    © Webstrucs 2020 
                    <a class="purple-text text-darken-4 right" href="#!"></a>
                </div>
            </div>
        </footer>
        <!-- Compiled and minified JavaScript -->
        <script src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>
        <!-- Load custom jquery -->
        <script src="/labs/assets/cod/jquery.ext.js"></script>
        <!--Custom framework design-->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <!--Custom framework design-->
        <script>$(document).ready(function(){ });</script>
    </body>
</html>
        '''
        return v_html5