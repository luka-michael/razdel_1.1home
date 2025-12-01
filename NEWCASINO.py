import random


class Player:


    def __init__(self, name, money=1000):
        self.name = name
        self.money = money
        self.in_casino = True
        self.games_played = 0

    def place_bet(self, amount):

        if amount <= 0:
            print("Ставка должна быть положительной!")
            return False
        elif amount > self.money:
            print(f"У вас недостаточно денег! У вас только {self.money}$")
            return False
        else:
            self.money -= amount
            print(f"Ставка {amount}$ принята. Осталось: {self.money}$")
            return amount

    def win_money(self, amount):

        if amount > 0:
            self.money += amount
            print(f"Вы выиграли {amount}$! Теперь у вас: {self.money}$")

    def is_broke(self):

        if self.money <= 0:
            self.money = 0
            self.in_casino = False
            return True
        return False

    def show_status(self):

        print(f"\n=== Статус игрока {self.name} ===")
        print(f"Деньги: {self.money}$")
        print(f"Сыграно игр: {self.games_played}")
        print("=" * 30)


class CasinoGame:


    def __init__(self, name, min_bet=10):
        self.name = name
        self.min_bet = min_bet

    def can_play(self, player):

        if not player.in_casino:
            print("Игрок не в казино!")
            return False
        if player.money < self.min_bet:
            print(f"Минимальная ставка {self.min_bet}$, а у вас только {player.money}$")
            return False
        return True


class RouletteGame(CasinoGame):


    def __init__(self):
        super().__init__("Рулетка", min_bet=20)
        self.max_number = 32

    def play(self, player):
        if not self.can_play(player):
            return False

        print("\n" + "=" * 50)
        print(f"Добро пожаловать в {self.name}!")

        print("Правила игры:")
        print(f"1. Загадайте число от 0 до {self.max_number}")
        print("2. Сделайте ставку")
        print("3. Если угадаете число - выигрыш 10x ставки!")
        print("4. Если угадаете четность - выигрыш 2x ставки!")
        print(f"Минимальная ставка: {self.min_bet}$")
        player.show_status()

        try:

            while True:
                try:
                    bet_amount = int(input(f"\nВведите сумму ставки (минимум {self.min_bet}$): "))
                    bet = player.place_bet(bet_amount)
                    if bet and bet >= self.min_bet:
                        break
                    elif bet and bet < self.min_bet:
                        print(f"Минимальная ставка {self.min_bet}$!")
                except ValueError:
                    print("Пожалуйста, введите число!")


            while True:
                try:
                    player_number = int(input(f"\nЗагадайте число от 0 до {self.max_number}: "))
                    if 0 <= player_number <= self.max_number:
                        break
                    else:
                        print(f"Число должно быть от 0 до {self.max_number}")
                except ValueError:
                    print("Пожалуйста, введите корректное число")

            print(f"\nВы загадали число: {player_number}")
            input("Нажмите Enter, чтобы крутить рулетку...")


            roulette_number = random.randint(0, self.max_number)
            print(f"\n Рулетка крутится... ")
            print(f"Выпало число: {roulette_number}!")


            if player_number == roulette_number:
                win_amount = bet * 10
                print(f"\n НЕВЕРОЯТНО! ВЫ УГАДАЛИ ТОЧНО! ")
                print(f"Выигрыш: {win_amount}$!")
                player.win_money(win_amount)
            elif (player_number % 2) == (roulette_number % 2):
                win_amount = bet * 2
                print(f"\n УГАДАЛИ ЧЕТНОСТЬ! ")
                print(f"Выигрыш: {win_amount}$!")
                player.win_money(win_amount)
            else:
                print(f"\nК сожалению, вы не угадали.")
                print(f"Ваше число {player_number}, а выпало {roulette_number}")

            player.games_played += 1


            if player.is_broke():
                print(f"\n У вас закончились деньги! ")
                print("Охранники вежливо провожают вас до выхода(((...")
                return False

            return True

        except ValueError:
            print("Пожалуйста, вводите корректные значения!")
            return True


class SlotMachine(CasinoGame):


    def __init__(self):
        super().__init__("Однорукий бандит", min_bet=10)
        self.symbols = ["🍒", "🍋", "🍊", "⭐", "🔔", "7️⃣"]

    def play(self, player):
        if not self.can_play(player):
            return False


        print(f"Добро пожаловать в {self.name}!")

        print("Правила игры:")
        print("1. Сделайте ставку")
        print("2. Если выпадут 3 одинаковых символа - выигрыш 50x ставки!")
        print("3. Если выпадут 2 одинаковых символа - выигрыш 5x ставки!")
        print("4. Если выпадет 7️⃣7️⃣7️⃣ - ДЖЕКПОТ 200x!")
        print(f"Минимальная ставка: {self.min_bet}$")
        player.show_status()

        try:

            while True:
                try:
                    bet_amount = int(input(f"\nВведите сумму ставки (минимум {self.min_bet}$): "))
                    bet = player.place_bet(bet_amount)
                    if bet and bet >= self.min_bet:
                        break
                    elif bet and bet < self.min_bet:
                        print(f"Минимальная ставка {self.min_bet}$!")
                except ValueError:
                    print("Пожалуйста, введите число!")

            input("\nНажмите Enter, чтобы дернуть за рычаг...")


            print("\n Слоты крутятся... ")
            results = [random.choice(self.symbols) for _ in range(3)]
            print(f"\n{' | '.join(results)}")


            if results[0] == results[1] == results[2]:
                if results[0] == "7️⃣":
                    win_amount = bet * 200
                    print(f"\n ДЖЕКПОТ! 777! ")
                    print(f"ВЫ ВЫИГРАЛИ {win_amount}$!!!")
                else:
                    win_amount = bet * 50
                    print(f"\n ТРИ ОДИНАКОВЫХ! ")
                    print(f"Выигрыш: {win_amount}$!")
                player.win_money(win_amount)
            elif results[0] == results[1] or results[1] == results[2] or results[0] == results[2]:
                win_amount = bet * 5
                print(f"\n ДВА ОДИНАКОВЫХ! ")
                print(f"Выигрыш: {win_amount}$!")
                player.win_money(win_amount)
            else:
                print(f"\nПовезет в следующий раз!")

            player.games_played += 1


            if player.is_broke():
                print(f"\n У вас закончились деньги! ")
                print("Охранники вежливо провожают вас до выхода(((...")
                return False

            return True

        except ValueError:
            print("Пожалуйста, вводите корректные значения!")
            return True


class PokerGame(CasinoGame):


    def __init__(self):
        super().__init__("Покер", min_bet=100)
        self.opponents = ["Мистер Биг", "Акула", "Улыбка", "Профессор"]

    def play(self, player):
        if not self.can_play(player):
            return False

        print("\n" + "=" * 50)
        print(f"Добро пожаловать в {self.name}!")
        print("=" * 50)
        print("Правила игры:")
        print("1. Игра против дилера")
        print("2. Угадайте, чья карта старше")
        print("3. Можно удвоить ставку в процессе игры")
        print(f"Минимальная ставка: {self.min_bet}$")
        player.show_status()

        try:

            while True:
                try:
                    bet_amount = int(input(f"\nВведите сумму ставки (минимум {self.min_bet}$): "))
                    bet = player.place_bet(bet_amount)
                    if bet and bet >= self.min_bet:
                        break
                    elif bet and bet < self.min_bet:
                        print(f"Минимальная ставка {self.min_bet}$!")
                except ValueError:
                    print("Пожалуйста, введите число!")

            opponent = random.choice(self.opponents)
            print(f"\nВаш противник: {opponent}")


            cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
            suits = ["♠", "♥", "♦", "♣"]

            player_card_value = random.randint(0, 12)
            dealer_card_value = random.randint(0, 12)

            player_card = f"{cards[player_card_value]}{random.choice(suits)}"
            dealer_card = f"{cards[dealer_card_value]}{random.choice(suits)}"

            print(f"\nВаша карта: {player_card}")


            double_down = input("\nХотите удвоить ставку? (да/нет): ").lower()
            if double_down in ['да', 'yes', 'y', 'д']:
                if player.place_bet(bet):
                    bet *= 2
                    print(f"Ставка удвоена! Теперь ставка: {bet}$")
                else:
                    print("Недостаточно денег для удвоения")

            print(f"\nКарта дилера: {dealer_card}")


            if player_card_value > dealer_card_value:
                win_amount = bet * 2
                print(f"\n ВЫ ВЫИГРАЛИ! ")
                print(f"Ваша карта {player_card} старше {dealer_card}")
                print(f"Выигрыш: {win_amount}$!")
                player.win_money(win_amount)
            elif player_card_value < dealer_card_value:
                print(f"\nВы проиграли...")
                print(f"Карта дилера {dealer_card} старше вашей {player_card}")
            else:
                win_amount = bet
                print(f"\nНичья!")
                player.win_money(win_amount)

            player.games_played += 1


            if player.is_broke():
                print(f"\n У вас закончились деньги! ")
                print("Охранники вежливо провожают вас до выхода...")
                return False

            return True

        except ValueError:
            print("Пожалуйста, вводите корректные значения!")
            return True


def choose_game(player):


    games = {
        "1": RouletteGame(),
        "2": PokerGame(),
        "3": SlotMachine()
    }

    while player.in_casino:
        print("\n" + "=" * 50)
        print("  МЕНЮ КАЗИНО ")
        print("=" * 50)
        player.show_status()
        print("\nВыберите игру:")
        print("1 - Рулетка (ставка от 20$)")
        print("2 - Покер (ставка от 100$)")
        print("3 - Однорукий бандит (ставка от 10$)")
        print("4 - Показать статус")
        print("5 - Выйти из казино")

        choice = input("\nВведите номер: ").strip()

        if choice == "1":
            game = games["1"]
            while game.play(player):
                play_again = input("\nХотите сыграть еще раз в рулетку? (да/нет): ").lower()
                if play_again not in ['да', 'yes', 'y', 'д']:
                    break
        elif choice == "2":
            game = games["2"]
            while game.play(player):
                play_again = input("\nХотите сыграть еще раз в покер? (да/нет): ").lower()
                if play_again not in ['да', 'yes', 'y', 'д']:
                    break
        elif choice == "3":
            game = games["3"]
            while game.play(player):
                play_again = input("\nХотите сыграть еще раз в автоматы? (да/нет): ").lower()
                if play_again not in ['да', 'yes', 'y', 'д']:
                    break
        elif choice == "4":
            player.show_status()
        elif choice == "5":
            print(f"\n{player.name}, вы выходите из казино с {player.money}$")
            player.in_casino = False
        else:
            print("Неверный выбор! Пожалуйста, выберите 1-5")

    return player


def main():



    print("ДОБРО ПОЖАЛОВАТЬ В КАЗИНО  ")



    name = input("\nКак вас зовут? ").strip() or "Игрок"
    player = Player(name)

    print(f"\nПриветствуем, {player.name}!")
    print(f"На вашем счету {player.money}$. Удачи!")


    while True:
        enter_answer = input("\nЖелаете ли вы войти в казино? (да/нет): ").lower()

        if enter_answer in ['да', 'yes', 'y', 'д']:
            print(f"\nОтлично, {player.name}! Добро пожаловать в казино!")
            print("Наши игры ждут вас!")
            break
        elif enter_answer in ['нет', 'no', 'n', 'н']:
            print(f"\nКак жаль, {player.name}! Надеемся увидеть вас снова!")
            return
        else:
            print("Пожалуйста, ответьте 'да' или 'нет'")


    player = choose_game(player)



    print("СПАСИБО ЗА ВИЗИТ!")

    print(f"\nИтоговый результат {player.name}:")
    print(f"Осталось денег: {player.money}$")
    print(f"Сыграно игр: {player.games_played}")

    if player.money > 1000:
        print(" Вы ушли в плюсе! Отличная работа!")
    elif player.money == 0:
        print(" К сожалению, вы все проиграли...")
    else:
        print(" Неплохой результат!")

    print("\nНадеемся увидеть вас снова!")


if __name__ == "__main__":
    main()