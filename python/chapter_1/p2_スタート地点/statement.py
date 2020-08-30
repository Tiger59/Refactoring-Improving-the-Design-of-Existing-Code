import math
def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = 'Statement for {}\n'.format(invoice["customer"])

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        this_amount = 0
        if play['type'] == 'tragedy':
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == 'comedy':
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)
            this_amount += 300 * perf['audience']
        else:
            raise Exception('unknown type: {}'.format(play["type"]))

        # ボリューム特典のポイントを加算
        volume_credits += max(perf['audience'] - 30, 0)
        # 喜劇の時は10人につき、さらにポイントを加算
        if 'comedy' == play['type']:
            volume_credits += math.floor(perf['audience'] / 5)
        # 注文の内訳を出力
        result += '  {}: ${:.2f} ({} seats)\n'.format(play["name"],this_amount / 100, perf["audience"])
        total_amount += this_amount

    result += 'Amount owed is ${:,.2f}\n'.format(total_amount / 100)
    result += 'You earned {} credits\n'.format(volume_credits)

    return result