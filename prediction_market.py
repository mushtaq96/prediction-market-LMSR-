import math


class PredictionMarket:

    def __init__(self, initial_funds, market_maker_fee):
        self.funds = initial_funds
        self.market_maker_fee = market_maker_fee
        self.outcomes = {}

    def create_market(self, outcome):
        self.outcomes[outcome] = {
            'outcome': outcome,
            'shares': 0,
            'price': 0
        }

    def get_market(self, outcome):
        return self.outcomes[outcome]

    def buy_shares(self, outcome, shares, user_funds):
        market = self.get_market(outcome)
        price = self.calculate_share_price(shares, market['shares'])
        cost = price * shares
        if cost > user_funds:
            raise ValueError('Not enough funds')
        market['shares'] += shares
        market['price'] = price
        self.funds += cost
        return cost

    def sell_shares(self, outcome, shares, user_funds):
        market = self.get_market(outcome)
        if shares > market['shares']:
            raise ValueError('Not enough shares')
        price = self.calculate_share_price(shares, market['shares'] - shares)
        revenue = price * shares
        market['shares'] -= shares
        market['price'] = price
        self.funds -= revenue
        return revenue

    def calculate_share_price(self, shares, current_shares):
        return self.calculate_market_price(current_shares + shares) - self.calculate_market_price(current_shares)

    def calculate_market_price(self, shares):
        return self.funds * math.log(1 + (shares * self.market_maker_fee) / self.funds)


# Example usage
market = PredictionMarket(1000, 0.01)
market.create_market('Rain tomorrow')
market.create_market('Trump will be re-elected')

market.buy_shares("Rain tomorrow", 10, 100)
market.buy_shares("Trump will be re-elected", 20, 200)

print(market.get_market("Rain tomorrow"))
print(market.get_market("Trump will be re-elected"))

market.sell_shares("Rain tomorrow", 5, 50)
market.sell_shares("Trump will be re-elected", 10, 100)

print(market.get_market("Rain tomorrow"))
print(market.get_market("Trump will be re-elected"))

print(market.funds)
