from dataclasses import dataclass

from classes.etc.metrics import MetricsWinRateAdj


@dataclass(frozen=True)
class Brawler:
    id: int


class MainBrawlerNow(Brawler):
    name: str
    metrics: MetricsWinRateAdj
