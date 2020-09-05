
from createStatementData import create_statement_data
def statement(invoice, plays):
    return render_plain_text(create_statement_data(invoice,plays))

def render_plain_text(data):
    result = 'Statement for {}\n'.format(data["customer"])
    for perf in data['performances']:
        result += '  {}: ${:.2f} ({} seats)\n'.format(perf["play"]["name"],perf["amount"] / 100, perf["audience"])
    result += 'Amount owed is ${:,.2f}\n'.format(data["total_amount"] / 100)
    result += 'You earned {} credits\n'.format(data["total_volume_credits"])
    return result

def html_statement(invoice,plays):
    return render_html(create_statement_data(invoice,plays))

def render_html(data):
    result = '<h1>Statement for {}</h1>\n'.format(data["customer"])
    result += '<table>\n'
    result += '<tr><th>play</th><th>seats</th><th>cost</th></tr>\n'
    for perf in data['performances']:
        result += '<tr><td>{}</td><td> ${:.2f} </td><td>{}</td></tr>\n'.format(perf["play"]["name"],perf["amount"] / 100, perf["audience"])
    result += '</table>\n'
    result += '<p>Amount owed is <em>${:,.2f}<\em></p>\n'.format(data["total_amount"] / 100)
    result += '<p>You earned <em>{}<\em> credits</p>\n'.format(data["total_volume_credits"])
    return result