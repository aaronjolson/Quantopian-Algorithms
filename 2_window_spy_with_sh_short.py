def initialize(context):
    context.spy = sid(8554)
    context.sh = sid(32268)

def handle_data(context, data):
    ma1 = data[context.spy].mavg(33)
    ma2 = data[context.spy].mavg(450)

    if ma1 > ma2:
        order_target_percent(context.sh, 0.00)
        order_target_percent(context.spy, 1.00)
    elif ma1 < ma2:
        order_target_percent(context.spy, 0.00)
        order_target_percent(context.sh, 1.00)
