from gamer import Gamer
import random


class Game:
    def start(self):
        print(f"How many players will play (2-8)?")
        while True:
            __pl_num = int(input())
            if 2 <= __pl_num <= 8:
                break
            else:
                print("Wrong number")
        for i in range(__pl_num):
            print(f"Player {i + 1}, enter your name")
            name = str(input())
            if name == "stop":
                raise ValueError
            self.__players.append(Gamer(name))

    def game(self):
        for i in range(len(self.__players)):
            player = self.__players[i]
            print(f"{player.get_name()}, choose your number from 1 to 100")
            while True:
                n = random.randint(1, 100)
                if 1 <= n <= 100:
                    player.set_number(n)
                    break
                else:
                    print("Wrong number")

        self.__pl_num = len(self.__players)
        players = self.__players
        random.shuffle(players)
        self.status = True
        r = 1
        while self.status and len(players) > 1:
            print(f"Tournament stage {r}")
            self.competition(players)
            players = self.__players
            if len(players) > 1:
                print("Continue (y/n)?")
                s = str(input())
                match s:
                    case "y":
                        pass
                    case _:
                        raise ValueError
            r += 1
        self.__comps.append(self.__players[0])
        print(f"{self.__players[0].get_name()} won tournament")

    def competition(self, players):
        losers = []
        self.__pl_num = len(players)
        for i in range(0, self.__pl_num, 2):
            if i < self.__pl_num - 1:
                print(
                    f"{players[i].get_name()} -> {players[i + 1].get_name()} ")
            else:
                print(f"{players[i].get_name()} will play in the final")

        for i in range(0, self.__pl_num, 2):
            if i < self.__pl_num - 1:
                numb = random.randint(1, 100)
                print(f"Round {self.__rounds}")
                if abs(players[i].get_number() - numb) > abs(players[i + 1].get_number() - numb):
                    winner = players[i + 1]
                    wn = abs(players[i + 1].get_number() - numb)
                    loser = players[i]
                    ln = abs(players[i].get_number() - numb)
                else:
                    winner = players[i]
                    wn = abs(players[i].get_number() - numb)
                    loser = players[i + 1]
                    ln = abs(players[i + 1].get_number() - numb)
                winner.set_score(winner.get_score() + 1)
                losers.append(loser)
                self.__rounds += 1
            if i == self.__pl_num - 1:
                break

            print(f"Number is {numb}")
            print(f"{winner.get_name()} chose {winner.get_number()} / {loser.get_name()} chose {loser.get_number()}")
            print(f"Winner {winner.get_name()} ({wn}) closer to {numb} than {loser.get_name()} ({ln})\n")

        for i in losers:
            self.__players.remove(i)
            self.__comps.append(i)

    def finish(self):
        print("\nParticipants:")
        self.__comps.reverse()
        for i in self.__comps:
            print(f"{i.get_name()} (won {i.get_score()} time(s))")

    def __init__(self):
        print("Tournament \"Random luck\"")
        self.__pl_num = 0
        self.__players = []
        self.status = False
        self.__rounds = 1
        self.__comps = []
