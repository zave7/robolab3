def sysCall_init():
    sim = require('sim')

    ball = sim.getObject("/ball")
    
    sim.setObjectFloatParam(ball, sim.shapefloatparam_init_velocity_y, 2)
    sim.setObjectFloatParam(ball, sim.shapefloatparam_init_velocity_z, 2)

def sysCall_actuation():
    # put your actuation code here
    pass

def sysCall_sensing():
    # put your sensing code here
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
