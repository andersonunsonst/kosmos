from cgi import FieldStorage

# Class CamelCase
# Class EntryStorage herda FieldStorage :
class EntryStorage(FieldStorage):

    # Atributos de Instância: São atributos declarados dentro do method construtor.
    # Atributo de Classe : São atributos que são declarados diretamente na classe ou seja fora do construtor

    # Atributo privado somente posso acessar dentro da classe que foi editado e usa Name Mangling: (self.__atributo)
    # Atributo Publico por convenção pode ser acessado de qualquer lugar: (self.atributo)

    # Method Construtor # self (convenção) = se refere ao objeto que esta executando o method.
    # O methodo construtor se refere ao method especial utilizado para a construção do objeto.

    def __init__(self, v_inp):
