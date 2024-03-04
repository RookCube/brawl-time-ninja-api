from abc import ABC
from dataclasses import dataclass
from typing import List

from classes.etc.brawler import MainBrawlerNow
from classes.etc.event import Event


@dataclass(frozen=True)
class Data(ABC):
    pass


@dataclass(frozen=True)
class DataEvents(Data):
    """Some data"""
    current: List[Event]
    upcoming: List[Event]


class DataMainBrawlersNow(Data):
    """Some data"""
    brawlers: List[MainBrawlerNow]


class DataMainBrawlersNowUnion(Data):
    """Some data"""
    # TODO: add query from json
    data: DataMainBrawlersNow
