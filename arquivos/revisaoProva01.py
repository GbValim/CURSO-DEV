class Usuario:
    caracterMin = 6

    def __init__(self,username,senha):
        self.username = username
        self._senha = ''
        self._tentativasFalhas = 0
        self.senha = senha
       
        

    

# Crie um @property para senha que
# não revele o texto original,retornando uma
# máscara de asteriscos do mesmo
#  tamanho da senha armazenada ("*" *len(self._senha)).

    @property
    def senha(self):
        return "*" *len(self._senha)


# Crie um @senha.setter que aceite a alteração apenas se a nova senha tiver pelo
# menos 6 caracteres e não contiver espaços em branco. Caso contrário, exiba uma
# mensagem de erro e mantenha a senha anterior.
    @senha.setter
    def senha(self, novaSenha):
        # Primeiro, confira se a senha tem o tamanho mínimo.
        if len(novaSenha) < self.caracterMin:
            print("Erro: a senha deve ter pelo menos 6 caracteres.")
            return

        # Depois, confira se há algum espaço em branco.
        for caractere in novaSenha:
            if caractere.isspace():
                print("Erro: a senha não pode conter espaços.")
                return

        # Só atualize a senha se as duas verificações passarem.
        self._senha = novaSenha
# No __init__, atribua self.senha = senha (sem underline)
#  para que a senha inicial já
# passe pelo verificador (Concluído)



# Crie uma propriedade somente-leitura chamada bloqueado (apenas @property, sem
# setter) que retorne True se self._tentativas_falhas >= 3, e False caso contrário.


# Crie o método autenticar(senha_digitada):

# a. Se a conta já estiver bloqueada (self.bloqueado), exiba uma mensagem de
# bloqueio e retorne False.


# b. Se a senha_digitada for igual à self._senha, zere self._tentativas_falhas e retorne
# True.


# c. Se estiver incorreta, some 1 em self._tentativas_falhas e retorne False.


    
        



