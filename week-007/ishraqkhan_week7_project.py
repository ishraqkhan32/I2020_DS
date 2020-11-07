import random

class RockPaperScissor:
    def __init__(self, rounds=3):
        self.rounds = rounds
        self.user_wins = 0
        self.computer_wins = 0
        self.ties = 0

    def computers_turn(self):
        choices = {
            0: 'rock',
            1: 'paper',
            2: 'scissors',
        }
        
        turn = random.randint(0,2)
        return (turn, choices[turn])

    # input: 'R', 'P', 'S' (strings) to represent rock, paper, scissors 
    def your_turn(self):  
        choices = {
            'R': 'rock',
            'P': 'paper',
            'S': 'scissors',
        }
        your_choice = input('Please enter your choice (R, P, S): ')

        return (your_choice, choices[your_choice])
    
    def compare_turns(self, user, computer):
        user_choice = user[1]
        comp_hand = computer[1]

        print(f"\nPlayer: {user_choice} \nComputer: {comp_hand}\n")

        # if both hands are the same, you did not beat the computer, therefore return False
        if user_choice == comp_hand:
            return 'Tie'

        # if player chooses rock
        if user_choice == 'rock':
            if comp_hand == 'scissors':
                return 'User Won'
            elif comp_hand == 'paper':
                return 'Computer Won'

        # if player chooses scissor
        if user_choice == 'scissors':
            if comp_hand == 'paper':
                return 'User Won'
            elif comp_hand == 'rock':
                return 'Computer Won'

        # if player chooses paper
        if user_choice == 'paper':
            if comp_hand == 'rock':
                return 'User Won'
            elif comp_hand == 'scissors':
                return 'Computer Won'
    
    def won_round(self):
        comp_tuple = self.computers_turn()
        your_tuple = self.your_turn()

        result = self.compare_turns(your_tuple, comp_tuple)
    
        # update win/loss/tie count
        if result == 'User Won':
            self.user_wins += 1
        elif result == 'Computer Won':
            self.computer_wins += 1
        else:
            self.ties += 1
        print(result)
        print('---------------------------------')
           
    # run game while rounds still available
    def run(self):
        while self.rounds > 0:
            self.won_round()
            self.rounds -= 1
        self.declare_results()
        
    # print results
    def declare_results(self):
        print(f'User wins: {self.user_wins}')
        print(f'Computer wins: {self.computer_wins}')
        print(f'Ties: {self.ties}')
        
if __name__ == '__main__':
    rps = RockPaperScissor()
    rps.run()