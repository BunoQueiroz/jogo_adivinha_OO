from random import randrange

class SecretNumber():
    def __init__(self):
        self.openning_game()
        self.secret_number = self.generate_number()
        self.attempts = self.user_attempts()
        self.guess = self.user_guess()
        self.winner()
        self.game_over()

    def openning_game(self):
        open = print("***********************************************************"
                     "\n***************Bem Vindo ao Jogo de Adivinha***************"
                     "\n***********************************************************"
                     "\n\nVamos ver se você é bom como dizem :-)")
        return open

    def generate_number(self):
        secret = int(randrange(1, 101, 1))
        return secret

    def winner(self):
        while self.attempts > 1:

            self.attempts -= 1

            if self.secret_number == self.guess:
                print("Parabéns, Você realmente é bom :)")
                break

            elif self.guess < self.secret_number:
                print("Tente um número MAIOR dessa vez ;)")

            elif self.guess > self.secret_number:
                print("Tente um número MENOR dessa vez ;)")

            self.guess = self.user_guess()

    def game_over(self):
        if self.attempts <= 1:
            print("Você não é tão bom assim afinal, mais sorte na próxima ;)")

    def user_guess(self):
        guess = int(input(f"Você tem {self.attempts} chances\n"
                          f"Chuta aí vai:\n"))
        return guess

    def user_attempts(self):
        def invalid_value():
            message = print("Essa opção é inválida, por isso a sau dificulda vai ser EXTREMA, boa sorte :)\n")
            return message

        try:
            difficulty = int(input("Escolha a dificuldade do seu desafio:"
                             "\n(1) - Fácil"
                             "\n(2) - Médio"
                             "\n(3) - Difícil\n"
                               "->"))

            if difficulty == 1:
                attempts = 18

            elif difficulty == 2:
                attempts = 10

            elif difficulty == 3:
                attempts = 7

            else:
                invalid_value()
                attempts = 4

        except ValueError:
                invalid_value()
                attempts = 4

        return attempts

if (__name__ == "__main__"):
    SecretNumber()