from dataclasses import dataclass
from typing import TypeVar


@dataclass
class CommonComponents:
    ...


@dataclass
class CommonPages:
    ...


CommonComponentsT = TypeVar("CommonComponentsT", bound=CommonComponents)
CommonPagesT = TypeVar("CommonPagesT", bound=CommonPages)
