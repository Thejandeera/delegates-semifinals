"""drive_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

if __name__ == "__main__":

    
    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = 64
    max_speed = 6.28
    
    #Creating motor object
    left_motor = robot.getDevice('motor_1')
    right_motor = robot.getDevice('motor_2')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    length_side = 0.25
    wheel_radius = 0.025
    
    linear_velocity = wheel_radius * max_speed
    duration_time = length_side / linear_velocity
    start_time = robot.getTime()
    
    # angle_of_rotation = 6.28/num_side
    # distance_between_wheels = 0.090
    # rate_of_rotation = (2)
    
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
    
        # current_time = robot.getTime()
        
        left_speed = max_speed
        right_speed = max_speed
        
        # if(current_time >= start_time + duration_time):
            # left_speed = 0
            # right_speed = 0
    
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    # Enter here exit cleanup code.
    