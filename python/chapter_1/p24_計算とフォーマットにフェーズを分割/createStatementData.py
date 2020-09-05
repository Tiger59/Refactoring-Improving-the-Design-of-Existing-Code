import math
def create_statement_data(invoice,plays):
    def play_for(a_performance):
        return plays[a_performance['playID']]
    
    def amount_for(a_performance):
        result = 0
        if a_performance['play']['type'] == 'tragedy':
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance['audience'] - 30)
        elif a_performance['play']['type'] == 'comedy':
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance['audience'] - 20)
            result += 300 * a_performance['audience']
        else:
            raise Exception('unknown type: {}'.format(play_for(a_performance)["type"]))
        return result
    
    def volume_credits_for(a_performance):
        result = 0
        # ボリューム特典のポイントを加算
        result += max(a_performance['audience'] - 30, 0)
        # 喜劇の時は10人につき、さらにポイントを加算
        if 'comedy' == play_for(a_performance)['type']:
            result += math.floor(a_performance['audience'] / 5)
        return result
    
    def enrich_performance(a_performance):
        result = a_performance.copy()
        result["play"] = play_for(result)
        result["amount"] = amount_for(result)
        result["volume_credits"] = volume_credits_for(result)
        return result

    def total_volume_credits(data):
        result = 0
        for perf in data['performances']:
            result += perf["volume_credits"]
        return result

    def total_amount(data):
        result = 0
        for perf in data['performances']:
            result += perf["amount"]
        return result
    
    result = {}
    result["customer"] = invoice["customer"]
    result["performances"] = list(map(enrich_performance,invoice["performances"]))
    result["total_amount"] = total_amount(result)
    result["total_volume_credits"] = total_volume_credits(result)
    return result