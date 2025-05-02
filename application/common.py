from dataclasses import dataclass
from typing import TypeVar


@dataclass
class CommonPages:
    ...


CommonPagesT = TypeVar("CommonPagesT", bound=CommonPages)
