
from structure_builder import *


def loadgame(save_directory, command_parser):
    # Update worlds/rooms
    updated_worlds = construct_worlds(save_directory + "/worlds/")
    command_parser.worlds = updated_worlds

    # Update Player
    updated_player = build_player(save_directory + "/player.json", updated_worlds)
    command_parser.player = updated_player

    # Update Current World and Room of parser
    command_parser.current_world = updated_player.current_world
    command_parser.current_room = updated_player.current_room

