import json
import unittest

from statement import statement


class TestStatement(unittest.TestCase):
    def test_statement(self):
        with open('plays.json') as f:
            plays = json.load(f)

        with open('invoices.json') as f:
            invoices = json.load(f)

        invoice = invoices[0]
        actual = statement(invoice, plays)

        expected = 'Statement for BigCo\n' \
                   '  Hamlet: $650.00 (55 seats)\n' \
                   '  As You Like It: $580.00 (35 seats)\n' \
                   '  Othello: $500.00 (40 seats)\n' \
                   'Amount owed is $1,730.00\n' \
                   'You earned 47 credits\n'

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()