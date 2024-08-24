speedRange = [-0.1, 0.1]

def sysCall_init():
    # do some initialization here
    sim = require("sim")
    simUI = require("simUI")
    
    global bill
    global speed
    bill = sim.getObject('/Bill')
    
    xml = '<ui title="'+sim.getObjectAlias(bill,1)+' speed" closeable="false" resizeable="false" activate="false">'+ \
    '<hslider minimum="0" maximum="100" on-change="speedChange_callback" id="1"/>'+ \
    '<label text="" style="* {margin-left: 300px;}"/>'+ \
    '</ui>'
    
    ui = simUI.create(xml)
    speed = 0 #speedRange[0] #0.5* (speedRange[0]+speedRange[1])
    speed_scale100 = 100*(speed-speedRange[0])/(-speedRange[0]+speedRange[1])
    simUI.setSliderValue(ui,1,speed_scale100)

def speedChange_callback(ui, id, speed_scale100):
    global speed
    speed = speedRange[0] + speed_scale100*(speedRange[1]-speedRange[0])/100
    
def sysCall_actuation():
    # put your actuation code here
    position = sim.getObjectPosition(bill,-1)
    #speed = 0.0001;
    t = sim.getSimulationTime()
    position[0] += speed*0.001*t
    sim.setObjectPosition(bill,-1,position)
    pass

def sysCall_sensing():
    # put your sensing code here
    pass

def sysCall_cleanup():
    # do some clean-up here
    pass
