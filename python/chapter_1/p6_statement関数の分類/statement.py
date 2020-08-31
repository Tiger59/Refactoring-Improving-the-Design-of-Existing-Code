import math
def statement(invoice, plays):
    def amount_for(a_performance):
        result = 0
        if play_for(a_performance)['type'] == 'tragedy':
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance['audience'] - 30)
        elif play_for(a_performance)['type'] == 'comedy':
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance['audience'] - 20)
            result += 300 * a_performance['audience']
        else:
            raise Exception('unknown type: {}'.format(play_for(a_performance)["type"]))
        return result
    
    def play_for(a_performance):
        return plays[a_performance['playID']]
    
    def volume_credits_for(a_performance):
        result = 0
        # ボリューム特典のポイントを加算
        result += max(a_performance['audience'] - 30, 0)
        # 喜劇の時は10人につき、さらにポイントを加算
        if 'comedy' == play_for(a_performance)['type']:
            result += math.floor(a_performance['audience'] / 5)
        return result
    
    def total_volume_credits():
        result = 0
        for perf in invoice['performances']:
            result += volume_credits_for(perf)
        return result

    def total_amount():
        result = 0
        for perf in invoice['performances']:
            result += amount_for(perf)
        return result
    
    result = 'Statement for {}\n'.format(invoice["customer"])
    for perf in invoice['performances']:
        result += '  {}: ${:.2f} ({} seats)\n'.format(play_for(perf)["name"],amount_for(perf) / 100, perf["audience"])
    result += 'Amount owed is ${:,.2f}\n'.format(total_amount() / 100)
    result += 'You earned {} credits\n'.format(total_volume_credits())
    return result