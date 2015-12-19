def initialize(context):
    context.spy = sid(8554)
    context.sso = sid(32270)

def handle_data(context, data):
    mavg1 = data[context.spy].mavg(75)
    mavg2 = data[context.spy].mavg(425)

    if mavg1 > mavg2:
        order_target_percent(context.sso, 1.00)
    elif mavg1 < mavg2:
        order_target_percent(context.sso, 0.00)
