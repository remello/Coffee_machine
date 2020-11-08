class CoffeeMachine:

    # remaining
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    # coffee recipes
    espresso = [250, 0, 16, 1, 4]
    latte = [350, 75, 20, 1, 7]
    cappuccino = [200, 100, 12, 1, 6]

    # there are 3 places where we need some inputs: main_menu, coffee_menu and fill
    machine_state = "main_menu"
    fill_state = "water"

    # changing remainings
    def change_value(self, recipe):
        self.water -= recipe[0]
        self.milk -= recipe[1]
        self.beans -= recipe[2]
        self.cups -= recipe[3]
        self.money += recipe[4]

    def print_remaining(self):
        print("\nThe coffee machine has:")
        print("{} of water".format(self.water))
        print("{} of milk".format(self.milk))
        print("{} of coffee beans".format(self.beans))
        print("{} of disposable cups".format(self.cups))
        print("{} of money\n".format(self.money))

    def needs(self, ingredient):
        print("Sorry, not enough {}!\n".format(ingredient))

    # checks if its possible to make a coffe
    def coffee_check(self, recipe):
        if self.water < recipe[0]:
            self.needs("water")
        elif self.milk < recipe[1]:
            self.needs("milk")
        elif self.beans < recipe[2]:
            self.needs("coffee beans")
        elif self.cups < 1:
            self.needs("disposable cups")
        else:
            self.change_value(recipe)
            print("I have enough resources, making you a coffee!\n")
        self.machine_state = "main_menu"

    def purchase(self, coffee_type):
        if coffee_type == "1":
            self.coffee_check(self.espresso)
        if coffee_type == "2":
            self.coffee_check(self.latte)
        if coffee_type == "3":
            self.coffee_check(self.cappuccino)
        if coffee_type == "back":
            self.machine_state = "main_menu"

    # fills machine with ingredients
    def fill(self, data):
        data = int(data)
        if self.fill_state == "water":
            self.water += data
            self.fill_state = "milk"
        elif self.fill_state == "milk":
            self.milk += data
            self.fill_state = "beans"
        elif self.fill_state == "beans":
            self.beans += data
            self.fill_state = "cups"
        elif self.fill_state == "cups":
            self.cups += data
            self.fill_state = "water"
            self.machine_state = "main_menu"

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    # prints texts to user
    def main_menu(self):
        if self.machine_state == "main_menu":
            print("Write action (buy, fill, take, remaining, exit): \n")
        elif self.machine_state == "coffee_menu":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        elif self.machine_state == "fill":
            if self.fill_state == "water":
                print("Write how many ml of water do you want to add:\n")
            elif self.fill_state == "milk":
                print("Write how many ml of milk do you want to add:\n")
            elif self.fill_state == "beans":
                print("Write how many grams of coffee beans do you want to add:\n")
            elif self.fill_state == "cups":
                print("Write how many disposable cups of coffee do you want to add:\n")

    # listens to user input
    def listener(self, data):
        if self.machine_state == "main_menu":
            if data == "buy":
                self.machine_state = "coffee_menu"
            elif data == "fill":
                self.machine_state = "fill"
            elif data == "take":
                self.take()
            elif data == "remaining":
                self.print_remaining()
            elif data == "exit":
                return 1

        elif self.machine_state == "coffee_menu":
            self.purchase(data)

        elif self.machine_state == "fill":
            self.fill(data)


my_machine = CoffeeMachine()

while True:
    my_machine.main_menu()
    if my_machine.listener(input()) == 1:
        break
