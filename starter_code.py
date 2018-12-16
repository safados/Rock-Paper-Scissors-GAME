# Refrences https://www.youtube.com/watch?v=Q5cewb4_epM
# Refrences https://www.geeksforgeeks.org/class-method-vs-static-method-python/
# Refrences https://github.com/eduardoportilho/rock-paper-scissor
# Refrences  https://www.youtube.com/watch?v=9Kdn9uIYhKw
import random
m = ['r', 'p', 's']


class Player:
    def __init__(self):
        self.score = 0

    def play(self):
        return m[0]

    def learn(self, their_move):
        pass


class RandomPlayer(Player):
    def play(self):
        index = random.randint(0, 2)
        return m[index]


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.their_move = None

    def play(self):
        if self.their_move is None:
            return Player.play(self)
        return self.their_move

    def learn(self, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.last_move = None

    def play(self):
        move = None
        if self.last_move is None:
            move = Player.play(self)
        else:
            index = m.index(self.last_move) + 1
            if index >= len(m):
                index = 0
            move = m[index]
        self.last_move = move
        return move


class HumanPlayer(Player):

    def play(self):
        player_move = input('\nSelect your move (' +
                            ', '.join(m) + '):\n')
        while player_move not in m:
            player_move = input('its not valid move,choose again\n')
        return player_move


class Game:

    def __init__(self):
        self.p1 = HumanPlayer()
        self.p2 = RandomPlayer()

    def play_match(self):
        print('Play Rock, Paper, Scissors GAME')
        while True:
                self.play_round()
                print('SCORE : ' + str(self.p1.score) + '  ||  ' +
                      str(self.p2.score) + '\n')

                if self.p1.score > self.p2.score:
                    print('* Player 1 won! *')
                    print('FINAL SCORE ' + str(self.p1.score) + '  ||  ' +
                          str(self.p2.score))
                elif self.p1.score < self.p2.score:
                    print('* Player 2 won! *')
                    print('FINAL SCORE  ' + str(self.p1.score) + '  ||  ' +
                          str(self.p2.score))
                else:
                    print('* The game was a draw! *')
                    print('FINAL SCORE ' + str(self.p1.score) + '  ||  ' +
                          str(self.p2.score))

    def play_round(self):
        p1mv = self.p1.play()
        p2mv = self.p2.play()
        rslt = Game.chk_rslt(p1mv, p2mv)
        self.p1.learn(p2mv)
        self.p2.learn(p1mv)
        print('You choose "' + p1mv + '" and Player 2 choose "' +
              p2mv + '"')
        if rslt == 1:
            self.p1.score += 1
            print('\n You won :D \n')
        elif rslt == 2:
            self.p2.score += 1
            print('\n Player 2 won ): \n')
        else:
            print('\n Draw :s \n')

    @classmethod
    def beats(self, move1, move2):
        if (move1 == 'r' and move2 == 's'):
            return True
        elif (move1 == 's' and move2 == 'p'):
            return True
        elif (move1 == 'p' and move2 == 'r'):
            return True
        return False

    @classmethod
    def chk_rslt(self, move1, move2):
        if Game.beats(move1, move2):
            return 1
        elif Game.beats(move2, move1):
            return 2
        else:
            return 0


game = Game()
game.play_match()
