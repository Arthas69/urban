import unittest

from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('John')
        for _ in range(10):
            runner.walk()
        return self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Doe')
        for _ in range(10):
            runner.run()
        return self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Spider')
        r2 = Runner('Man')

        for _ in range(10):
            r1.run()
            r2.walk()

        return self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = []

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_result:
            print(result)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.r1 = Runner('Usain', 10)
        self.r2 = Runner('Andrew', 9)
        self.r3 = Runner('Nik', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrew(self):
        t = Tournament(90, self.r1, self.r2)
        self.all_result.append(t.start())

        return self.assertTrue(self.all_result[-1][2] == 'Andrew')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrew_nik(self):
        t = Tournament(90, self.r2, self.r3)
        self.all_result.append(t.start())

        return self.assertTrue(self.all_result[-1][2] == 'Nik')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrew_nik(self):
        t = Tournament(90,  self.r3, self.r2, self.r1)
        self.all_result.append(t.start())

        return self.assertTrue(self.all_result[-1][3] == 'Nik')


if __name__ == '__main__':
    unittest.main()
