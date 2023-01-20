# LSMR Prediction Market
This is a simple web application that demonstrates the use of Hanson's Logarithmic Market Scoring Rule (LMSR) for a prediction market. Users can make trades on predictions, betting on how likely an event is to occur. Each prediction is an individual market with a market maker system modeled on Robin Hanson's logarithmic market scoring rules.


## Some finance theory before we move ahead!

Prediction markets are a way for people to make bets on what they think will happen in the future, like a game. They use money or pretend money to buy shares that represent different outcomes of an event, like whether it will rain or not. The price of the shares changes depending on how many people believe that outcome will happen. After the event happens, the people who bought the right shares get paid.


*The Logarithmic Market Scoring Rule (LMSR) is a mathematical formula used in prediction markets to determine the prices of different outcomes or "securities" in the market.* The basic formula for LMSR is as follows:

**Price of a security** = exp(B * p - C) / (1 + exp(B * p - C))

Where:

- B is the market maker's "efficiency parameter"
- p is the probability that the security will be true
- C is a normalizing constant that ensures the prices of the securities sum to 1
The LMSR algorithm takes into account the probability of the event, as well as the number of shares of the security that have been purchased. By adjusting the value of B, the market maker can control the degree of "market efficiency" - that is, how quickly the prices of the securities respond to changes in demand.

The main advantage of LMSR is that it is a "market-making" algorithm, which means it automatically creates a market for any event, even if there's no market yet. LMSR is considered more robust than other market making algorithms, such as Vickrey-Clarke-Groves (VCG) or the Quadratic Voting algorithm.


# Prerequisites
- [x] Python 3.x
- [x] Flask
- [x] Jinja2
- [x] prediction_market.py (provided in the repository)

## Running the Application
- Clone the repository to your local machine.
- Navigate to the cloned repository in your command line.
- Run the command pip install -r requirements.txt to install the required dependencies.
- Run the command python app.py to start the application.
- Open your web browser and navigate to http://localhost:5000/ to interact with the application.

## Using the Application
- Select the outcome you want to trade on from the dropdown menu.
- Enter the number of shares you want to trade.
- Select the trade type (buy or sell).
- Enter the funds available for the trade.
- Click on the submit button to make the trade.
- The result of the trade will be displayed on the screen.

Note: This is a simple demonstration application and is not intended for production use.
