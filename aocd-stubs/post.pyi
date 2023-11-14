from typing import Any
from urllib3 import BaseHTTPResponse

def submit(
    answer: Any, part: str | None =None, day: int | None =None, year: int | None=None,
    session: str | None =None, reopen: bool =True, quiet: bool =False
) -> BaseHTTPResponse | None:...