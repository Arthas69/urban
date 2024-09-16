import unittest

from runner import Runner


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


if __name__ == '__main__':
    unittest.main()
