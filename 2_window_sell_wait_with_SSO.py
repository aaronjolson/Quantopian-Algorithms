def initialize(context):
    context.spy = sid(8554)
    context.sso = sid(32270)

def handle_data(context, data):
    ma1 = data[context.spy].mavg(75)
    ma2 = data[context.spy].mavg(425)

    if ma1 > ma2:
        order_target_percent(context.sso, 1.00)
    elif ma1 < ma2:
        order_target_percent(context.sso, 0.00)
