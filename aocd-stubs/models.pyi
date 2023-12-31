import os
from datetime import datetime
from datetime import timedelta
from functools import cache
from functools import cached_property
from importlib.metadata import EntryPoint
from pathlib import Path
from typing import Callable, Any
from urllib3 import BaseHTTPResponse
from .examples import Example

import bs4


AOCD_DATA_DIR = Path(os.environ.get("AOCD_DIR", Path("~", ".config", "aocd")))
AOCD_DATA_DIR = AOCD_DATA_DIR.expanduser()
AOCD_CONFIG_DIR = Path(os.environ.get("AOCD_CONFIG_DIR", AOCD_DATA_DIR)).expanduser()
URL = "https://adventofcode.com/{year}/day/{day}"


class User:
    _token2id: dict[str, str] | None = None

    def __init__(self, token: str):...

    @classmethod
    def from_id(cls, id: str):...

    @property
    def id(self) -> str:...

    def __str__(self) -> str:...

    @property
    def memo_dir(self) -> Path:...

    def get_stats(self, years: list[int] | tuple[int] | int | range | None=None) -> dict[str, dict[str, dict[str, timedelta | int]]]:...

def default_user() -> User:...

class Puzzle:
    def __init__(self, year: int, day: int, user: User | None =None) -> None:...

    @property
    def user(self) -> User:...

    @property
    def input_data(self) -> bytes | str:...

    @property
    def examples(self) -> list[Example]:...

    def _get_examples(self, parser_name: str ="reference") -> list[Example]:...

    @cached_property
    def title(self) -> str:...

    def _repr_pretty_(self, p: Any, cycle: bool) -> None:...

    def _coerce_val(self, val: Any) -> str:...

    @property
    def answer_a(self) -> str:...

    @answer_a.setter
    def answer_a(self, val: Any) -> None:...

    @property
    def answered_a(self) -> bool:...

    @property
    def answer_b(self) -> str:...

    @answer_b.setter
    def answer_b(self, val: Any) -> None:...

    @property
    def answered_b(self) -> bool:...

    def answered(self, part: str) -> bool:...

    @property
    def answers(self) -> tuple[str, str]:...

    @answers.setter
    def answers(self, val: tuple[str, str]) -> None:...

    @property
    def submit_results(self) -> Any:...

    def _submit(self, value: str, part: str, reopen: bool=True, quiet: bool=False) -> BaseHTTPResponse:...

    def _check_already_solved(self, guess: str, part: str) -> str:...

    def _save_correct_answer(self, value: str, part: str) -> None:...

    def _save_submit_result(self, value: str, part: str, message: str, when: Any) -> None:...

    def _get_answer(self, part: str) -> str:...

    def solve(self) -> tuple[str, str]:...

    def solve_for(self, plugin: EntryPoint) -> tuple[str, str]:...

    @property
    def url(self) -> str:...

    def view(self) -> None:...

    @property
    def my_stats(self) -> dict[str, dict[str, timedelta | int]]:...

    def _request_puzzle_page(self) -> None:...

    def _get_prose(self) -> str:...

    @property
    def easter_eggs(self) -> bs4.element.ResultSet[Any]:...

    def unlock_time(self, local: bool=True) -> datetime:...

    @staticmethod
    def all(user: User | None=None) -> 'Puzzle':...


def _parse_duration(s: str) -> timedelta:...


def _load_users() -> dict[str, str]:...


@cache
def _load_example_parser(group: str="adventofcode.examples", name: str="reference") -> Callable[..., list[Example]]:...
