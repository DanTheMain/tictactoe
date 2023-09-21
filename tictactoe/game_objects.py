from enum import StrEnum
from copy import deepcopy
from random import choice
from typing import Any
from typing_extensions import Protocol


DEFAULT_GRID = {str(s): str(s) for s in range(1, 10)}


# class Moves:
#     def __init__(self) -> None:
#         self._moves: set[str] = deepcopy(DEFAULT_CHOICES)
#
#     def __str__(self) -> str:
#         return ", ".join([c for c in self._moves])
#
#     def get(self) -> set[str]:
#         return self._moves
#
#     def is_empty(self) -> bool:
#         return bool(self._moves)
#
#     def is_valid_move(self, p_move: str) -> bool:
#         return p_move in self._moves
#
#     def remove(self, move: str) -> bool:
#         if not self.is_empty() and self.is_valid_move(move):
#             self._moves.remove(move)
#             return True
#         return False


class GameGrid:
    def __init__(self) -> None:
        self._grid_contents: dict[str, str] = deepcopy(DEFAULT_GRID)

    def __str__(self) -> str:
        grid = ""
        for cell_number, cell_content in self._grid_contents.items():
            grid = " | ".join(
                [grid, str(cell_content), "\n" if int(cell_number) % 3 == 0 else ""]
            )
        return grid

    def __repr__(self) -> str:
        return str(self._grid_contents.items())

    @property
    def grid_contents(self) -> dict[str, str]:
        return self._grid_contents

    def update(self, cell_number: str, new_value: str) -> None:
        if cell_number not in self._grid_contents or new_value is None:
            raise ValueError
        self._grid_contents[cell_number] = new_value


class PlayerMark(StrEnum):
    X = "X"
    O = "0"


class PlayerType(StrEnum):
    USER = "user"
    BOT = "bot"


class Player(Protocol):
    mark: PlayerMark

    def make_move(self, valid_moves: set[str]) -> str: ...


def get_input(prompt):
    return str(input(prompt).lower().strip())


class User(Player):
    ptype = PlayerType.USER

    def __str__(self) -> str:
        return f"Player '{self.ptype.value}' ({self.mark.value})"

    def make_move(self, valid_moves: set[str]) -> str:
        move = get_input("Enter your choice: ")
        while move not in valid_moves:
            move = get_input(f"Invalid choice '{move}' - please make another: ")
        return move


class Bot(Player):
    ptype = PlayerType.BOT

    def __str__(self) -> str:
        return f"Player '{self.ptype.value}' ({self.mark.value})"

    def make_move(self, valid_moves: set[str]) -> str:
        return choice(list(valid_moves))
