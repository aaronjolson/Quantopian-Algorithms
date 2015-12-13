# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    context.stocks = symbols('SPY')

# Will be called on every trade event for the securities you specify.
def handle_data(context, data):
    for stock in context.stocks:
        ma1 = data[stock].mavg(43)
        ma2 = data[stock].mavg(180)

        # price = data[stock].price

        if ma1 > ma2:
            order_target_percent(stock, 0.99)

        elif ma1 < ma2:
            order_target_percent(stock, 0.00)
