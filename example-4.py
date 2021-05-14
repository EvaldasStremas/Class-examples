class Calculator:
    def __init__(self, a_value, b_value, c_value):
        self.a = a_value
        self.b = b_value
        self.c = c_value

    def play(self):
        user_input = input("Enter value of player " + self.mark1)
        print(user_input)

    def add_a_and_b(self):
        a = int(self.a)
        b = int(self.b)
        print(a + b)

    def add_a_and_b_and_c(self):
        a = int(self.a)
        b = int(self.b)
        c = int(self.c)
        print(a + b + c)

game = Calculator(a_value='10', b_value='5', c_value='20')
game.add_a_and_b()
game.add_a_and_b_and_c()