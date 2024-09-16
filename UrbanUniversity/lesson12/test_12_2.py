import unittest

from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_result = []

    def setUp(self):
        self.r1 = Runner('Usain', 10)
        self.r2 = Runner('Andrew', 9)
        self.r3 = Runner('Nik', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result:
            print(result)

    def test_usain_andrew(self):
        t = Tournament(90, self.r1, self.r2)
        self.all_result.append(t.start())

        return self.assertTrue(self.all_result[-1][2] == 'Andrew')

    def test_andrew_nik(self):
        t = Tournament(90, self.r2, self.r3)
        self.all_result.append(t.start())

        return self.assertTrue(self.all_result[-1][2] == 'Nik')

    def test_usain_andrew_nik(self):
        t = Tournament(90,  self.r3, self.r2, self.r1)
        self.all_result.append(t.start())

        return self.assertTrue(self.all_result[-1][3] == 'Nik')


if __name__ == '__main__':
    unittest.main()
