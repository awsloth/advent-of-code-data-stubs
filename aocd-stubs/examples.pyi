from dataclasses import dataclass
from typing import NamedTuple

import bs4


@dataclass
class Page:
    raw_html: str  # String of the puzzle page html. May or may not have part b unlocked
    soup: bs4.BeautifulSoup  # The raw_html string parsed into a bs4.BeautifulSoup instance
    year: int  # AoC puzzle year (2015+) parsed from html title
    day: int  # AoC puzzle day (1-25) parsed from html title
    article_a: bs4.element.Tag  # The bs4 tag for the first <article> in the page, i.e. part a
    article_b: bs4.element.Tag  # The bs4 tag for the second <article> in the page, i.e. part b. It will be `None` if part b locked
    a_raw: str  # The first <article> html as a string
    b_raw: str  # The second <article> html as a string. Will be `None` if part b locked

    def __repr__(self) -> str:...

    @classmethod
    def from_raw(cls, html: str) -> 'Page':...

    def __getattr__(self, name: str) -> str:...

class Example(NamedTuple):
    input_data: str
    answer_a: str | None = None
    answer_b: str | None = None
    extra: str | None = None

    @property
    def answers(self) -> tuple[str | None, str | None]:...

def _trunc(s: str, maxlen: int=50) -> str:...

def _get_unique_real_inputs(year: int, day: int) -> list[str]:...

def main() -> None:...