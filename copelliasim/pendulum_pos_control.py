import math

def sysCall_init():
    sim = require('sim')

    global joint1
    global joint2
    global end_effect
    global end_effect_trace

    joint1 = sim.getObject("/Joint1")
    joint2 = sim.getObject("/Joint2")
    
    end_effect_trace = sim.addDrawingObject(sim.drawing_linestrip, 5, 0, -1, 100_000, [1,0,0])
    
    end_effect = sim.getObject("/EndEff")

def sysCall_actuation():
    
    theta1 = sim.getJointPosition(joint1)
    theta2 = sim.getJointPosition(joint2)
    print(f"join1: {theta1}, joint2: {theta2}")
    
    # sim.setJointTargetPosition(joint1, math.pi/4)
    # sim.setJointTargetPosition(joint2, math.pi/2)
    
    t = sim.getSimulationTime()
    theta1 = math.pi*t/6
    theta2 = math.pi*t/3
    
    sim.setJointTargetPosition(joint1, theta1)
    sim.setJointTargetPosition(joint2, theta2)

def sysCall_sensing():
    
    end_effect_pos = sim.getObjectPosition(end_effect, sim.handle_world)
    sim.addDrawingObjectItem(end_effect_trace, end_effect_pos)

def sysCall_cleanup():
    # do some clean-up here
    pass
