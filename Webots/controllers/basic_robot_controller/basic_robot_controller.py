from controller import Robot
from controller import Motor
import math

# High level functions
def move_forward(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(max_speed)

def move_back():
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(-max_speed)

def turn_left(): 
    left_motor.setVelocity(-max_speed)
    right_motor.setVelocity(max_speed)

def turn_right(): 
    left_motor.setVelocity(max_speed)
    right_motor.setVelocity(-max_speed)

def drive_forward(angle, inRadians = False): 
    if inRadians: 
        angle *= 57.295   #//180/3.14 = 57
    if angle > 90 or angle < -90:
        pass
    elif angle >= 0:
        left_motor.setVelocity(max_speed)
        right_motor.setVelocity( max_speed * math.sin((angle + 45) / 28.648) )
    else:
        left_motor.setVelocity(max_speed * math.sin((-angle + 45) / 28.648) )
    right_motor.setVelocity(max_speed)

def set_camera_position(rotation):
    camera_motor.setPosition(rotation)
    
def get_camera_position():
    return camera_motor.getTargetPosition()

def reset_motors():
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    camera_motor.setVelocity(0)
    
    
    
#main function
if __name__ == "__main__":
    #Create the Robot instance.
    robot = Robot()
    
    #Variables
    time_step = 64
    max_speed = 0.5
    camera_min_position =  0.65 #lowest position
    camera_max_position = -1 #highest position
    camera_default_position = 0 #base position
    
    #Set up motor/track wheels
    left_motor = robot.getDevice("left_motor")
    right_motor = robot.getDevice("right_motor")
    left_motor.setPosition(math.inf)
    right_motor.setPosition(math.inf)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    
    #Set up camera and camera motor
    camera = robot.getDevice("camera_camera")
    camera.enable(time_step)
    width = camera.getWidth()
    height = camera.getWidth()
    
    #Setting maximum rotational values of camera motor
    camera_motor = robot.getDevice("camera_rotational_motor")
    camera_motor.maxPosition = camera_max_position
    camera_motor.minPosition = camera_min_position

    #Main Loop while simulation is running
    while robot.step(time_step) != -1:
        #Code goes here       
        
        
        
        pass #end of code region
                
    #End of AI
    reset_motors()
    del robot
    pass  # EXIT_SUCCESS