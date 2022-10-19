from os import remove
import Player
from desk import Deck
import random
from const import MESSAGES

class Game:

    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    def ask_to_start(self,message):

        print('''WELCOME
        You are in Black Jack Game''')

        while True:
            ask = input(message)
            if ask == 'y':
                return True
                break
            elif ask == 'n':
                exit(1)
            else:
                print ('your answer is not corect, try again')

    def _launching(self):

        while True:

            bots_count = int(input('Please enter the count of bots : '))
            if bots_count <= self.max_pl_count - 1 :
                break

        self.all_players_count = bots_count + 1

        for i in range(bots_count):

            b = Player.Bot()
            self.players.append(b)
            print(f'{b} is created')

        self.player = Player.Player()
        self.player_pos = random.randint(0,bots_count)
        self.players.insert(self.player_pos,self.player) 
        print(f'your position is {self.player_pos}')

    def ask_bet(self):

        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet) 

    def check_stop(self,player):

        if player.full_points >= 21 :
            return True
        else:
            return False

    def first_descr(self):
        for player in self.players:
            for i in range(2):
                card = self.deck.get_card()
                self.player.take_card(card)

        card = self.deck.get_card()
        self.dealer.take_card(card)
        self.dealer.print_cards()
        return None

    def remove_player(self, player):

        player.print_cards()

        if isinstance(player, Player.Player):
            print('You are fall!')

        elif isinstance(player, Player.Bot):
            print(player, 'are fall!')

        self.players.remove(player)

    def ask_card(self):
        for player in self.players:

            card = self.deck.get_card()
            player.take_card(card) 

            is_stop = self.check_stop(player)

            if is_stop:
                if player.full_points > 21 or isinstance(player, Player.Player):
                        self.remove_player(player)
                break
            
            if isinstance(player, Player.Player):
                player.print_cards()

    def check_win(self):

        if self.dealer.full_points > 21: #all win
            print('Dealer are fall! All players in game are win!')

            for winner in self.players:
                winner.money += winner.bet * 2

        else:
            for player in self.players:

                if player.full_points == self.dealer.full_points:
                    player.money += player.bet
                    print(MESSAGES.get('eq').format(player=player,points=player.full_points))

                elif player.full_points > self.dealer.full_points:
                    player.money += player.bet * 2

                    if isinstance(player, Player.Bot):
                        print(MESSAGES.get('win').format(player))

                    elif isinstance(player, Player.Player):
                        print('You are win!')

                elif player.full_points < self.dealer.full_points:

                    if isinstance(player, Player.Bot):
                        print(MESSAGES.get('lose').format(player))

                    elif isinstance(player, Player.Player):
                        print('You are lose!')


    def play_with_dealer(self):
        
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
            self.check_win()
            
        self.dealer.print_cards()

    def start_game(self):
        
        message = MESSAGES.get('ask_start')
        # todo: max players count?
        if not self.ask_to_start(message=message):
            exit(1)

        self._launching()

        while True:
            if self.check_len() :

                self.ask_bet()

                self.first_descr()

                self.player.print_cards()

                self.ask_card() #ask player about one more card

                self.play_with_dealer()

                self.check_win()

                if not self.ask_to_start(MESSAGES.get('rerun')):
                    break
        