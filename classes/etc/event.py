from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Event:
    id: int
    map: str
    mode: str
    start: datetime
    end: datetime
