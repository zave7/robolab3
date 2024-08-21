def sysCall_init():
    sim = require('sim')

    global joint_left
    global joint_right
    global point
    global chassis
    global point_trace
    global graph
    global graph_x
    global graph_y

    # load left, right joints
    joint_right = sim.getObject("/Joint_right")
    joint_left = sim.getObject("/Joint_left")
    
    # set 
    sim.setObjectInt32Param(joint_left, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
    sim.setObjectInt32Param(joint_right, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)
    
    # set joint velocity
    sim.setJointTargetVelocity(joint_left, 2)
    sim.setJointTargetVelocity(joint_right, 2)
    
    # get object
    point = sim.getObject("/Point")
    chassis = sim.getObject("/Chassis")
    
    # make trace drawing object
    point_trace = sim.addDrawingObject(sim.drawing_linestrip, 5, 0, -1, 100_000, [1,0,0])
    
    # add graph, graphstream
    graph = sim.getObject("/Graph")
    graph_x = sim.addGraphStream(graph, "x", "m", 1)
    graph_y = sim.addGraphStream(graph, "y", "m", 1)
    sim.addGraphCurve(graph, "x/y", 2, [graph_x, graph_y], [0,0], "x by m", 0, [1, 0, 0], 2)
    
def sysCall_actuation():
    t = sim.getSimulationTime()
    if t>3:
        sim.setJointTargetVelocity(joint_left, 5)
        
    # print point position
    point_position = sim.getObjectPosition(point, -1)
    print(f"x = {str(point_position[0])} y = {str(point_position[1])}")

    eulerAngles = sim.getObjectOrientation(chassis, sim.handle_world)
    print(f"angle = {str(eulerAngles[2])}")

    sim.addDrawingObjectItem(point_trace, point_position)

    sim.setGraphStreamValue(graph, graph_x, point_position[0])
    sim.setGraphStreamValue(graph, graph_y, point_position[1])

def sysCall_sensing():
    # put your sensing code here
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
