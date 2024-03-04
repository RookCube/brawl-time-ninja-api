from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class Metrics(ABC):
    pass


class MetricsWinRateAdj(Metrics):
    winRateAdj: float
