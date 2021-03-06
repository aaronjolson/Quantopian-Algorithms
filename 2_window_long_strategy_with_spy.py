def initialize(context):
    context.spy = sid(8554)


# Will be called on every trade event for the securities you specify.
def handle_data(context, data):
    mavg1 = data[context.spy].mavg(55)
    mavg2 = data[context.spy].mavg(200)

    print "The value of mavg 1 is " + str(mavg1)
    print "The value of mavg 2 is " + str(mavg2)

    if mavg1 > mavg2:
        order_target_percent(context.spy, 1.0)
    elif mavg1 < mavg2:
        order_target_percent(context.spy, 0.00)

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