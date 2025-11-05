from monopoly.player import Player
from monopoly.board import Board
from monopoly.tile.propertyTile import PropertTile

class Game:

    player_1 = Player("moti", 0, 1500)
    player_2_computer = Player("AI", 0, 1500)
    sum_turn = 0
    make_the_board = Board()

    while sum_turn < 21:
        player_1_move = player_1.movement()
        print(player_1_move)
        if player_1_move > 39:
            player_1_move -= 39
            print(player_1_move)
        get_player_tile = make_the_board.get_location_info(player_1_move)
        match get_player_tile["type"]:
            case "property":
                PropertTile(get_player_tile["name"], get_player_tile["type"], get_player_tile["price"], get_player_tile["rent"], get_player_tile["city"])
            case "rail":
                pass
            case "bonus":
                pass
            case "tax":
                pass
            case "jail":
                pass
            case "go to jail":
                pass
            case "start":
                pass

        sum_turn += 1
