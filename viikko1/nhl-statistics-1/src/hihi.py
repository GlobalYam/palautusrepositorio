import unittest
from statistics_service import StatisticsService
from player_reader_stub import PlayerReaderStub
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
Stats = StatisticsService(PlayerReaderStub())
print(Stats.top(1, SortBy.ASSISTS)[0])