# Class-HomeStrucs : modelo de conteudo.
class CustomJquery:
    # class-method : renderizar a page home
    def writecode(v_appget):
        # class-attribute : public.
        v_strucs = '''
$(document).ready(function() {
  // shooting event: form button click
  $(".btn").text("Pesquisar").click(function() {
    // shooting event: get value in variable
    var v_query = $(".v-query").val();
    // shooting event: ajax method
    $.ajax({
      type: "POST",
      url: "'''+ v_appget +'''/spark/query",
      data: { v_query : v_query },
      dataType: "json",
      // shooting event: amostra screen suavimente
      beforeSend : function() {
        // shooting efect: amostra mensagem suavimente
        $(".alert-primary").text("Aguarde...").fadeIn("slow");
      },
      // end callback:
      complete : function() {
      },
      // shoot event moment feedback server:
      success : function(json) {
        // obtem resposta via json e atribuindo valores
        var term = json.term;

        // shooting efect: amostra mensagem suavimente
        $(".alert-primary").html(term).fadeIn("slow");
      },
      error : function(json) {
      },
    });
  });
});
        '''
        return v_strucs