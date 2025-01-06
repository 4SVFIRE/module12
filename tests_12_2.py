import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name
        return NotImplemented


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            to_remove = []
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    to_remove.append(participant)
            for participant in to_remove:
                self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_result = []

    def setUp(self):
        self.Usain = Runner("Usain", 10)
        self.Andrey = Runner("Andrey", 9)
        self.Nick = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result:
            print(result)

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        TournamentTest.all_result.append([participant.name for participant in results.values()])

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        TournamentTest.all_result.append([participant.name for participant in results.values()])

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        TournamentTest.all_result.append([participant.name for participant in results.values()])


if __name__ == "__main__":
    unittest.main()
