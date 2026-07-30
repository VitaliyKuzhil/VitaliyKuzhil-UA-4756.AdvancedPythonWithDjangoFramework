import unittest
from abc import ABC, abstractmethod

class TaxStrategy(ABC):

    @abstractmethod
    def get_tax_percent(self, amount):
        pass


class ZeroTaxPercent(TaxStrategy):
    def get_tax_percent(self, amount):
        return 0.0

class TenTaxPercent(TaxStrategy):

    def get_tax_percent(self, amount):

        return amount * 0.10

class FifteenTaxPercent(TaxStrategy):

    def get_tax_percent(self, amount):

        return amount * 0.15

class TwentyOneTaxPercent(TaxStrategy):

    def get_tax_percent(self, amount):

        return amount * 0.21

class ThirtyTaxPercent(TaxStrategy):

    def get_tax_percent(self, amount):

        return amount  * 0.30

class FortyTaxPercent(TaxStrategy):

    def get_tax_percent(self, amount):

        return amount * 0.40

class FortySevenTaxPercent(TaxStrategy):

    def get_tax_percent(self, amount):

        return amount * 0.47



class Worker:
    def __init__(self, name, salary=0):
        if salary < 0:
            raise ValueError()

        self.name = name
        self.salary = salary


    def get_tax_value(self):
        worker_salary = self.salary
        total_tax = 0.0

        slots = [
            (1000, 1000, ZeroTaxPercent()),
            (3000, 2000, TenTaxPercent()),
            (5000, 2000, FifteenTaxPercent()),
            (10000, 5000, TwentyOneTaxPercent()),
            (20000, 10000, ThirtyTaxPercent()),
            (50000, 30000, FortyTaxPercent()),
        ]

        prev_limit = 0
        for limit, slot_size, strategy in slots:
            if worker_salary > prev_limit:
                taxable_value = min(worker_salary - prev_limit, slot_size)
                total_tax += strategy.get_tax_percent(taxable_value)
                prev_limit = limit
            else:
                break

        if worker_salary > 50000:
            taxable_value = worker_salary - 50000
            total_tax += FortySevenTaxPercent().get_tax_percent(taxable_value)

        return total_tax


class WorkerTest(unittest.TestCase):

    def setUp(self):
        self.worker = Worker('Bob', 100000)

    def tearDown(self):
        self.worker = None

    def test_get_worker_tax_value(self):
        self.assertAlmostEqual(self.worker.get_tax_value(),40050.0, places=1)

    @unittest.expectedFailure
    def test_negative_salary_of_worker(self):
        Worker('Sally', -1300)
        