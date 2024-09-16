import logging
import unittest

from lesson12.rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='./runner_tests.log', encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner = Runner('John', -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
        except ValueError as e:
            logging.warning('Wrong speed for Runner', exc_info=True)
        else:
            logging.info('test_walk successfully executed')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner = Runner(2)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError as e:
            logging.warning('Wrong data type for Runner', exc_info=True)
        else:
            logging.info('test_run successfully executed')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = Runner('Spider')
        r2 = Runner('Man')

        for _ in range(10):
            r1.run()
            r2.walk()

        return self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    test_runner = unittest.TextTestRunner()
    test_runner.run(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
