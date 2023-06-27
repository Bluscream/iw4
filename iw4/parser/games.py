from typing import Any
from dataclasses import dataclass
from .map import Map

@dataclass
class Game:

    @staticmethod
    def from_dict(obj: dict) -> 'Games':
        pass

@dataclass
class Games:
    games: dict[str,dict[str,Map]]

    @staticmethod
    def from_dict(obj: dict) -> 'Games':
        games = {}
        for name, game in obj.items():
            games[name] = Game.from_dict(game)
        return Games(games)