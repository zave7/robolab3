import math 

def sysCall_init():
    sim = require('sim')

    global vision
    vision = sim.getObject("/Vision_sensor")

    global graph
    global graph_red
    global graph_green
    global graph_blue
    
    graph = sim.getObject("/Graph")
    graph_red = sim.addGraphStream(graph, "red", 5, 0, [1,0,0])
    graph_green = sim.addGraphStream(graph, "green", 5, 0, [0,1,0])
    graph_blue = sim.addGraphStream(graph, "blue", 5, 0, [0,0,1])

def sysCall_actuation():
    # put your actuation code here
    pass

def sysCall_sensing():
    
    # auxValues: 15 auxiliary values:
    # the minimum of {intensity, red, green, blue, depth value}
    # the maximum of {intensity, red, green, blue, depth value}
    # and the average of {intensity, red, green, blue, depth value}
    result, packet1, packet2 = sim.readVisionSensor(vision)
    
    avg_red = packet1[11]
    avg_green = packet1[12]
    avg_blue = packet1[13]
    avg = math.sqrt(avg_red**2 + avg_green**2 + avg_blue**2)
    
    red = avg_red/avg
    green = avg_green/avg
    blue = avg_blue/avg
    print(f"red {red},\tgreen {green},\tblue {blue}")
    
    sim.setGraphStreamValue(graph, graph_red, red)
    sim.setGraphStreamValue(graph, graph_green, green)
    sim.setGraphStreamValue(graph, graph_blue, blue)
    
    

def sysCall_cleanup():
    # do some clean-up here
    pass

# See the user manual or the available code snippets for additional callback functions and details
