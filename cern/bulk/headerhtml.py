# Class Header : modelo de cabeçalho html.
class HeaderHtml:
    # class-method : renderizar o cabeçalho html.
    def writecode(v_appget):
        # class-attribute : public.
        v_strucs = '''
# Class Header : modelo de cabeçalho html.
class Header:
    # class-method : view
    def view():
        # class-attribute :
        v_html5 = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <meta name="description" content=""/>
        <meta name="keywords" content=""/>

        <!-- Favicon -->
        <link  href="/''' + v_appget + '''/assets/fgs/" rel="shortcut icon"/>
        <!--Import Google Icon -->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <!--Import Material Design Icons-->
        <link href="https://cdn.materialdesignicons.com/5.6.55/css/materialdesignicons.min.css" rel="stylesheet">
        <!--Import Google Font -->
        <link href="https://fonts.googleapis.com/css?family=Catamaran&display=swap" rel="stylesheet">
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

        <!--Custom framework design-->
        <link href="''' + v_appget + '''/assets/css/materialize.ext.css" rel="stylesheet" type="text/css">
        
        <!-- Page Title -->
        <title></title>

    </head>
    <body class="">
        """
        return v_html5
        '''
        return v_strucs