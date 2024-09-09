from game import Game

if __name__ == '__main__':
    game = Game()
    try:
        game.start()
        game.game()
        game.finish()
    except ValueError:
        print("Closing game... (you did something wrong)")
        exit()
