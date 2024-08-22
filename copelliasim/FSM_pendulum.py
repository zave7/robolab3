import math

FSM_velocity = 0
FSM_position = 1
FSM_damping = 2

def sysCall_init():
    sim = require('sim')

    global joint
    global FSM
    global t_position
    global t_damping

    joint = sim.getObject("/Joint")
    
    FSM = FSM_velocity
    t_position = 0
    t_damping = 0
    
def sysCall_actuation():
    
    # sim.jointdynctrl_free
    # sim.jointdynctrl_force
    # sim.jointdynctrl_velocity
    # sim.jointdynctrl_position
    # sim.jointdynctrl_spring
    # sim.jointdynctrl_callback
    
    # control velocity
    # sim.setObjectInt32Param(joint, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
    # sim.setJointTargetVelocity(joint, 0.5)
    
    # control position
    # sim.setObjectInt32Param(joint, sim.jointintparam_dynctrlmode, sim.jointdynctrl_position)
    # sim.setJointTargetPosition(joint, math.pi/2)
    
    # control force
    # sim.setObjectInt32Param(joint, sim.jointintparam_dynctrlmode, sim.jointdynctrl_force)
    # Force = 10
    # thetadot = sim.getJointVelocity(joint)
    # Force = -0.5 * thetadot
    # sim.setJointTargetForce(joint, Force)
    
    global FSM
    global t_position
    global t_damping
    
    # FSM coding
    t = sim.getSimulationTime()
    theta = sim.getJointPosition(joint)
    thetadot = sim.getJointVelocity(joint)
    
    # all transitions
    if(FSM==FSM_velocity and theta>-0.5 and theta<0.5):
        FSM = FSM_position
        t_position = t
        print("transitioning to FSM_position")
        
    if(FSM==FSM_position and t-t_position > 3):
        FSM = FSM_damping
        t_damping = t
        print("transitioning to FSM_damping")
        
    if(FSM==FSM_damping and t-t_damping > 4):
        FSM = FSM_velocity
        sim.setJointTargetForce(joint, 10_000)
        print("transitioning to FSM_velocity")
    
    # all control action
    if(FSM==FSM_velocity):
        sim.setObjectInt32Param(joint, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
        sim.setJointTargetVelocity(joint, 0.5)
    
    if(FSM==FSM_position):
        sim.setObjectInt32Param(joint, sim.jointintparam_dynctrlmode, sim.jointdynctrl_position)
        sim.setJointTargetPosition(joint, 0.1)
        
    if(FSM==FSM_damping):
        sim.setObjectInt32Param(joint, sim.jointintparam_dynctrlmode, sim.jointdynctrl_force)
        Force = -0.5 * thetadot
        sim.setJointTargetForce(joint, Force)
    

def sysCall_sensing():
    # put your sensing code here
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
