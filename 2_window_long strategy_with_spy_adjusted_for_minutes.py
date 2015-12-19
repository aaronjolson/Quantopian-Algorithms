def initialize(context):
    context.spy = sid(8554)

    schedule_function(rebalance,
                      date_rule = date_rules.every_day(),
                      time_rule = time_rules.market_open())
def rebalance(context, data):
    mavg1 = data[context.spy].mavg(75)
    mavg2 = data[context.spy].mavg(450)

    if mavg1 > mavg2:
        order_target_percent(context.spy, 1.0)
    elif mavg1 < mavg2:
        order_target_percent(context.spy, 0.00)

def handle_data(context, data):
    pass
"""
some other numbers to try
33, 205
55, 205
55, 195
60, 450
75, 425 //This is the highest result I have been able to find
75, 430
75, 440
75, 450
75, 455
75, 465
"""