from flask import Flask, render_template, request
from prediction_market import PredictionMarket

app = Flask(__name__)
market = PredictionMarket(1000, 0.01)
market.create_market("Rain tomorrow")
market.create_market("Trump will be re-elected")


@app.route("/")
def index():
    return render_template("index.html", outcomes=market.outcomes, funds=market.funds)


@app.route("/make_trade", methods=["POST"])
def make_trade():
    outcome = request.form['outcome']
    shares = int(request.form['shares'])
    user_funds = int(request.form['funds'])
    trade_type = request.form['trade_type']
    if trade_type == 'buy':
        cost = market.buy_shares(outcome, shares, user_funds)
        return render_template('buy.html', outcome=outcome, shares=shares, cost=cost, fund=market.funds)
    elif trade_type == 'sell':
        revenue = market.sell_shares(outcome, shares, user_funds)
        return render_template('sell.html', outcome=outcome, shares=shares, revenue=revenue, fund=market.funds)


@app.route("/buy", methods=["POST"])
def buy():
    outcome = request.form["outcome"]
    shares = int(request.form["shares"])
    user_funds = float(request.form["funds"])
    try:
        cost = market.buy_shares(outcome, shares, user_funds)
        print("Successfully purchased {} shares for ${:.2f}".format(shares, cost))
        return render_template('buy.html', outcome=outcome, shares=shares, cost=cost)
    except ValueError as e:
        return str(e)


@app.route("/sell", methods=["POST"])
def sell():
    outcome = request.form["outcome"]
    shares = int(request.form["shares"])
    user_funds = float(request.form["funds"])
    try:
        revenue = market.sell_shares(outcome, shares, user_funds)
        print("Successfully sold {} shares for ${:.2f}".format(shares, revenue))
        return render_template('sell.html', outcome=outcome, shares=shares, revenue=revenue)
    except ValueError as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
