def initialize(context):
    context.spy = sid(8554)
    context.sh = sid(32268)

def handle_data(context, data):
    mavg1 = data[context.spy].mavg(55)
    mavg2 = data[context.spy].mavg(150)

    if mavg1 > mavg2:
        order_target_percent(context.sh, 0.00)
        order_target_percent(context.spy, 1.00)
    elif mavg1 < mavg2:
        order_target_percent(context.spy, 0.00)
        order_target_percent(context.sh, 1.00)
