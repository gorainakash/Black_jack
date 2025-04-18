import random
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_title():
    print(r"""
  ____  _            _    _            _    
 |  _ \| |          | |  | |          | |   
 | |_) | | __ _  ___| | _| | __ _  ___| | __
 |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 | |_) | | (_| | (__|   <| | (_| | (__|   < 
 |____/|_|\__,_|\___|_|\_\_|\__,_|\___|_|\_\
                                            
       🂡 Welcome to Blackjack 🃏          
    Try to get as close to 21 as possible!
""")
    time.sleep(2)

def deal_card():
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(computer_score, user_score):
    if user_score > 21 and computer_score > 21:
        if user_score > computer_score:
            return "💥 You both went over, but you had the higher score. You win! 🎉"
        elif computer_score > user_score:
            return "💥 You both went over, but the computer had the higher score. Computer wins! 🤖"
        else:
            return "😅 You both went over with the same score. It's a draw!"
    elif user_score > 21:
        return "🚨 You went over. You lose!"
    elif computer_score > 21:
        return "🎯 Computer went over. You win!"
    elif user_score == computer_score:
        return "⚖️ It's a draw!"
    elif user_score == 0:
        return "🃏 Blackjack! You win! 🏆"
    elif computer_score == 0:
        return "🤖 Computer got Blackjack! You lose!"
    elif user_score > computer_score:
        return "🎉 You win!"
    else:
        return "😢 Computer wins!"

def display_cards(player, cards):
    card_art = " ".join([f"[{c}]" for c in cards])
    return f"{player} Cards: {card_art} | Score: {calculate_score(cards)}"

def play_game():
    clear()
    ascii_title()

    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(dealer_cards)

        print("\n" + display_cards("🧑 You", user_cards))
        print(f"🤖 Dealer's First Card: [{dealer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("👉 Type 'y' to draw another card or 'n' to pass: ").lower()
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(dealer_cards)

    print("\n🔚 Final Results:")
    print(display_cards("🧑 You", user_cards))
    print(display_cards("🤖 Dealer", dealer_cards))
    print("\n" + compare(computer_score, user_score))

    play_again = input("\n🔁 Want to play again? (y/n): ").lower()
    if play_again == 'y':
        play_game()
    else:
        print("\n👋 Thanks for playing Blackjack! See you next time!\n")

play_game()
