from flask import Flask, render_template, request
from prediction_market import PredictionMarket

app = Flask(__name__)
market = PredictionMarket(1000, 0.01)
market.create_market("Rain tomorrow")
market.create_market("Trump will be re-elected")


@app.route("/")
def make_trade():
    return render_template("index.html", outcomes=market.outcomes)


@app.route("/buy", methods=["POST"])
def buy():
    outcome = request.form["outcome"]
    shares = int(request.form["shares"])
    user_funds = float(request.form["funds"])
    try:
        cost = market.buy_shares(outcome, shares, user_funds)
        return "Successfully purchased {} shares for ${:.2f}".format(shares, cost)
    except ValueError as e:
        return str(e)


@app.route("/sell", methods=["POST"])
def sell():
    outcome = request.form["outcome"]
    shares = int(request.form["shares"])
    user_funds = float(request.form["funds"])
    try:
        revenue = market.sell_shares(outcome, shares, user_funds)
        return "Successfully sold {} shares for ${:.2f}".format(shares, revenue)
    except ValueError as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
