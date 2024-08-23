def sysCall_init():
    sim = require('sim')

    global proximity

    proximity = sim.getObject("/Proximity_sensor")
    
    global graph
    global graph_distance
    graph = sim.getObject("/Graph")
    graph_distance = sim.addGraphStream(graph, "distance", 5, 0, [1,0,0])

def sysCall_actuation():
    # put your actuation code here
    pass

def sysCall_sensing():
    
    result, distance, point, obj, n = sim.readProximitySensor(proximity)
    print(f"result {result}")
    print(f"distance {distance}")
    
    sim.setGraphStreamValue(graph, graph_distance, distance)

def sysCall_cleanup():
    # do some clean-up here
    pass

