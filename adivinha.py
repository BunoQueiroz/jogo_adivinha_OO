from random import randrange

class SecretNumber():
    def __init__(self):
        self.openning_game()
        self._secret_number = self.generate_number()
        self.attempts = self.user_attempts()
        self.guess = self.user_guess()
        self.winner()
        self.game_over()

    @property
    def secret_number(self):
        return self._secret_number

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

            if self.guess == self.secret_number:
                print("Parabéns, Você realmente é bom :)")
                break

            elif self.guess < self.secret_number:
                print("Tente um número MAIOR dessa vez ;)")

            elif self.guess > self.secret_number:
                print("Tente um número MENOR dessa vez ;)")

            self.guess = self.user_guess()

    def user_guess(self):
        try:
            guess = int(input(f"Você tem {self.attempts} chances\n"
                              f"Tente um número de 1 a 100:\n"))
        except ValueError:
            guess = 0

        return guess

    def user_attempts(self):
        def invalid_value():
            message = print("Essa opção é inválida, por isso a sua dificuldade vai ser EXTREMA, boa sorte :)\n")
            return message

        try:
            difficulty = int(input("Escolha a dificuldade do seu desafio:"
                             "\n(1) - Fácil"
                             "\n(2) - Médio"
                             "\n(3) - Difícil\n"
                               "->"))

            if difficulty == 0:
                difficulty = "error"

            if difficulty == 1 or 2 or 3:
                chances = [18, 10, 7]
                attempts = chances[difficulty - 1]

        except (ValueError, IndexError, TypeError):
                invalid_value()
                attempts = 4

        return attempts

    def game_over(self):
        if self.attempts <= 1:
            print(f"Você não é tão bom assim afinal, mais sorte na próxima ;)\n"
                  f"Por sinal, o número secreto era: {self.secret_number}")

if __name__ == "__main__":
    SecretNumber()