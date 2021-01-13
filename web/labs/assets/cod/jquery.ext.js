
$(document).ready(function() {
  // shooting event: form button click
  $(".btn-large").text("Submit").click(function() {
    // shooting event: get value in variable
    var v_name = $("#v-name").val();
    var v_sname = $("#v-sname").val();
    // shooting event: ajax method
    $.ajax({
      type: "POST",
      url: "labs/spark/add",
      data: { v_name : v_name, v_sname : v_sname },
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
        var nome = json.nome;
        var snome = json.snome;
        var pessoa = nome + " " + snome;
        // shooting efect: amostra mensagem suavimente
        $(".alert-primary").html(pessoa).fadeIn("slow");
      },
      error : function(json) {
      },
    });
  });
});
        