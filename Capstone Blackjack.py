import random

cards = {
    "Diamond": {
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        "joker": False,
        "queen": False,
        "king": False,
        "ace": False,
    },
    "Spade": {
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        "joker": False,
        "queen": False,
        "king": False,
        "ace": False,
    },
    "Club": {
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        "joker": False,
        "queen": False,
        "king": False,
        "ace": False,
    },
    "Heart": {
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False,
        10: False,
        "joker": False,
        "queen": False,
        "king": False,
        "ace": False,
    }
}

player_cards = []
dealer_cards = []


def begin_game():
    for i in range(2):
        player_cards.append(get_random_card())
        dealer_cards.append(get_random_card())


def get_random_card():
    chosen_suit = random.randrange(1, 5)

    match chosen_suit:
        # Diamond suit
        case 1:
            while True:
                chosen_card = random.choice(list(cards["Diamond"].keys()))
                if cards["Diamond"][chosen_card] == False:
                    cards["Diamond"][chosen_card] = True
                    return [chosen_card, "Diamond"]
        # Spade suit
        case 2:
            while True:
                chosen_card = random.choice(list(cards["Spade"].keys()))
                if cards["Spade"][chosen_card] == False:
                    cards["Spade"][chosen_card] = True
                    return [chosen_card, "Spade"]
        # Club suit
        case 3:
            while True:
                chosen_card = random.choice(list(cards["Club"].keys()))
                if cards["Club"][chosen_card] == False:
                    cards["Club"][chosen_card] = True
                    return [chosen_card, "Club"]
        # Heart suit
        case 4:
            while True:
                chosen_card = random.choice(list(cards["Heart"].keys()))
                if cards["Heart"][chosen_card] == False:
                    cards["Heart"][chosen_card] = True
                    return [chosen_card, "Heart"]


def setup_game():
    while True:
        print("Welcome to black jack")
        player_decision = input("Would you like to play? (Y) to play")
        if str.lower(player_decision) == "y":
            print(f"Thanks for playing. Lets get started!")
            play_game()
            break


def get_total_points(is_player):
    total_card_count = 0

    if is_player:
        for card in player_cards:
            if isinstance(card[0], int):
                total_card_count += card[0]
            else:
                if card[0] == "joker" or card[0] == "queen" or card[0] == "king":
                    total_card_count += 10
    else:
        for card in dealer_cards:
            if isinstance(card[0], int):
                total_card_count += card[0]
            elif card[0] == "ace":
                total_card_count += 11
            else:
                if card[0] == "joker" or card[0] == "queen" or card[0] == "king":
                    total_card_count += 10

    return total_card_count



def play_game():
    # Initial Setup
    global player_cards
    global dealer_cards

    while True:
        begin_game()
        print(f"Your cards are {player_cards[0][0]} of {player_cards[0][1]}s and {player_cards[1][0]} of {player_cards[1][1]}s")
        player_points = get_total_points(True)
        print(f"You have a total score of {player_points}")

        print(f"Dealer cards are {dealer_cards[0][0]} of {dealer_cards[0][1]}s and {dealer_cards[1][0]} of {dealer_cards[1][1]}s")
        dealer_points = get_total_points(False)
        print(f"Dealer has a total score of {dealer_points}")

        while True:
            dealer_points = get_total_points(False)
            player_points = get_total_points(True)
            print(f"You have a total score of {player_points}")
            print(f"Dealer has a total score of {dealer_points}")
            if player_points == 21:
                player_won()
                player_cards = []
                dealer_cards = []
                setup_game()
                return
            elif dealer_points == 21:
                print("DEALER WON")
                player_cards = []
                dealer_cards = []
                setup_game()
                return
            elif player_points < 21 and dealer_points >= player_points and dealer_points <= 21:
                force_player_hit()
                continue
            elif player_points > dealer_points:
                player_decision = input("Do you want to hit? (Y) Yes")
                if str.lower(player_decision) == "y":
                    new_card = get_random_card()
                    player_cards.append(new_card)
                    continue
                else:
                    new_card = get_random_card()
                    dealer_cards.append(new_card)
            elif player_points > 21:
                print("YOU BUST")
                player_cards = []
                dealer_cards = []
                setup_game()
                return
            elif dealer_points > 21:
                print("DEALER BUST. YOU WIN")
                player_cards = []
                dealer_cards = []
                setup_game()
                return







def force_player_hit():
    new_card = get_random_card()
    player_cards.append(new_card)


def player_won():
    print("You won")


setup_game()
