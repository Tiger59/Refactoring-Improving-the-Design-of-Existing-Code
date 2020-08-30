import statement from "../statement.js";

test('test_statement', () => {
  const fs = require("fs");
  const invoice = JSON.parse(fs.readFileSync('./invoices.json', 'utf8'));
  const plays = JSON.parse(fs.readFileSync('./plays.json', 'utf8'));
  expect(statement(invoice, plays)).toBe(
    'Statement for BigCo\n' +
    '  Hamlet: $650.00 (55 seats)\n' +
    '  As You Like It: $580.00 (35 seats)\n' +
    '  Othello: $500.00 (40 seats)\n' +
    'Amount owed is $1,730.00\n' +
    'You earned 47 credits\n'
  );
});