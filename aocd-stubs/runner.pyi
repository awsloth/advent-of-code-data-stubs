from typing import Any, Callable, TypeAlias
from importlib.metadata import EntryPoint

RunnerOut: TypeAlias = int
Runner :TypeAlias = Callable[..., RunnerOut]

DEFAULT_TIMEOUT = 60

def main() -> None:...

def _timeout_wrapper(f: Runner, capture: bool=False,
                     timeout: float=DEFAULT_TIMEOUT, **kwargs: Any) -> Runner:...

def _process_wrapper(f: Runner, capture: bool=False, **kwargs: Any) -> RunnerOut | None:...

def run_with_timeout(entry_point: EntryPoint, timeout: float, progress: str | None , dt: float=0.1, capture: bool=False, **kwargs: dict[str, Any]) -> tuple[str, str, float, str]:...

def format_time(t: float, timeout: float=DEFAULT_TIMEOUT) -> str:...

def run_one(
    year: int, day: int, data: str, entry_point: EntryPoint, timeout: float=DEFAULT_TIMEOUT, progress: str | None =None, capture: bool=False
) -> tuple[str, str, float, str]:...

def run_for(
    plugs: list[str],
    years: list[int],
    days: list[int],
    datasets: list[str],
    example: bool=False,
    timeout: float=DEFAULT_TIMEOUT,
    autosubmitbool: bool=True,
    reopen: bool =False,
    capture: bool=False,
) -> int:...
