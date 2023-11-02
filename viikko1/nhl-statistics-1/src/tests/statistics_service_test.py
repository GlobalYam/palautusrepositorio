import unittest
from statistics_service import StatisticsService
from player_reader_stub import PlayerReaderStub
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.Stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        self.assertAlmostEqual(str(self.Stats.search('Semenko')), 'Semenko EDM 4 + 12 = 16')
    
    def test_search_none(self):
        self.assertAlmostEqual(self.Stats.search('Semenkos'), None)
    
    def test_team(self):
        self.assertAlmostEqual(str(self.Stats.team('PIT')[0]), 'Lemieux PIT 45 + 54 = 99')
    
    def test_top(self):
        self.assertAlmostEqual(str(self.Stats.top(1)[0]), 'Gretzky EDM 35 + 89 = 124')
    
    def test_goals(self):
        self.assertAlmostEqual(str(self.Stats.top(1, SortBy.GOALS)[0]), 'Lemieux PIT 45 + 54 = 99')
    
    def test_assists(self):
        self.assertAlmostEqual(str(self.Stats.top(1, SortBy.ASSISTS)[0]), 'Gretzky EDM 35 + 89 = 124')