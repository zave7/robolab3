import math

def sysCall_init():

    # define global variable
    global sphere
    global graph
    global graph_x
    global graph_z
        
    sim = require('sim')
    sphere = sim.getObject("/Sphere") # get Object sphere type shape
    print("init")
    
    # initialization velocity
    sim.setObjectFloatParam(sphere, sim.shapefloatparam_init_velocity_x,1)
    sim.setObjectFloatParam(sphere, sim.shapefloatparam_init_velocity_z,1)

    graph = sim.getObject("/Graph")
    graph_x = sim.addGraphStream(graph,"pos_x", "m", 0, [1,0,0])
    graph_z = sim.addGraphStream(graph,"pos_z", "m", 0, [0,0,1])


def sysCall_actuation():

    print(f"actuation")
    
    # get velocity
    linearVelocity, angularVelocity = sim.getVelocity(sphere)
    print(f"Linear Velocity: {linearVelocity}")
    print(f"Angular Velocity: {angularVelocity}")
    
    # force
    # Fx = -c*vx*sqrt(vx**2+vy**2+vz**2) and so on
    c = 0.25
    vx = linearVelocity[0]
    vy = linearVelocity[1]
    vz = linearVelocity[2]
    
    v = math.sqrt(vx**2+vy**2+vz**2)
    Fx = -c*vx*v
    Fy = -c*vy*v
    Fz = -c*vz*v
    Force = [Fx, Fy, Fz]
    Torque = [0,0,0]
    sim.addForceAndTorque(sphere,Force,Torque)
    
    # relativeToObjectHandle=-1 is relative to the world
    position = sim.getObjectPosition(sphere,-1)
    print(f"x = {position[0]}")
    print(f"z = {position[2]}")
    
    # add value to graph stream
    sim.setGraphStreamValue(graph, graph_x, position[0])
    sim.setGraphStreamValue(graph, graph_z, position[2])
    
    pass

def sysCall_sensing():
    print("sensing")
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
