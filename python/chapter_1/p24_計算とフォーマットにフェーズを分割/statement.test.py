import json
import unittest

from statement import *


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
    
    def test_html_statement(self):
        with open('plays.json') as f:
            plays = json.load(f)

        with open('invoices.json') as f:
            invoices = json.load(f)

        invoice = invoices[0]
        actual = html_statement(invoice, plays)

        expected = '<h1>Statement for BigCo</h1>\n' \
                   '<table>\n' \
                   '<tr><th>play</th><th>seats</th><th>cost</th></tr>\n' \
                   '<tr><td>Hamlet</td><td> $650.00 </td><td>55</td></tr>\n' \
                   '<tr><td>As You Like It</td><td> $580.00 </td><td>35</td></tr>\n' \
                   '<tr><td>Othello</td><td> $500.00 </td><td>40</td></tr>\n' \
                   '</table>\n' \
                   '<p>Amount owed is <em>$1,730.00<\em></p>\n' \
                   '<p>You earned <em>47<\em> credits</p>\n'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()