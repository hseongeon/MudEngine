#!/usr/bin/env python3
"""
Author : seong-eon Hwang (hseongeon@gmail.com)
Date   : 2025-08-22

Purpose:
    MudEngine is a text-based command-line tool that serves as the foundation
    for a single-player exploration game. It allows users to navigate a 3D
    coordinate-based world, inspect rooms, and interact with game elements.
    It is designed for building and testing game logic and world layouts
    without graphical assets. Once the world is defined, users can explore
    rooms, check descriptions, and manage game data efficiently, making
    it easier to expand into a full 3D RPG in the future.
"""

__version__ = "unreleased"

import argparse
import logging


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="MudEngine is a text-based MUD game engine that allows "
        "creating, editing, and exploring game worlds, quests, and characters "
        "via command-line interface."
    )

    subparsers = parser.add_subparsers(
        title="commands",
        dest="command",
        required=True,
        help="Available commands",
    )

    # ---- game subcommand ----
    subparsers.add_parser(
        "game",
        help="Launch the MUD game to explore the world, "
        "interact with rooms, and progress through quests.",
    )

    # ---- map editor subcommand ----
    subparsers.add_parser(
        "map_editor",
        help="Open the map editor to create and "
        "modify game world layouts and room details.",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    args = get_args()
    if args.command == "game":
        pass
    elif args.command == "map_editor":
        pass


# --------------------------------------------------
if __name__ == "__main__":
    main()
