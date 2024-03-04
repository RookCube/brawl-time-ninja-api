from dataclasses import dataclass
from datetime import datetime

from classes.etc.data import Data, DataEvents, DataMainBrawlersNowUnion


@dataclass(frozen=True)
class State:
    # TODO: add more fields from json
    data: Data
    dateUpdatedAt: datetime
    dataUpdateCount: int


class StateEvents(State):
    data: DataEvents


class StateMainBrawlersNow(State):
    data: DataMainBrawlersNowUnion
