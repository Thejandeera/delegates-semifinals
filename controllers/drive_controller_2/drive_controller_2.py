"""drive_controller_2 controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
import math

def run_robot(robot):
    
    timestep = 64
    max_speed = 6.28
    
    left_motor = robot.getDevice('motor_1')
    right_motor = robot.getDevice('motor_2')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    #Position sensors
    left_ps = robot.getDevice('ps_1')
    left_ps.enable(timestep)
    right_ps = robot.getDevice('ps_2')
    right_ps.enable(timestep)
    
    #compute the linnear length
    wheel_radius = 0.025
    distance_between_wheels = 0.09
    wheel_cirm = 2 * 3.14 * wheel_radius
    encoder_unit = wheel_cirm / 6.28
    
    ps_values = [0, 0]
    last_ps_values = [0, 0]
    
    dist_values = [0, 0]
    
    #robot position
    robot_pose = [0 , 0, 0] # x, y, theta
    
    
    while robot.step(timestep) != -1:
        left_speed = max_speed
        right_speed = max_speed
        
        ps_values[0] = left_ps.getValue()
        ps_values[1] = right_ps.getValue()
        
        print('-------------------------------------------------')
        print(f"left pos: {ps_values[0]} right pos: {ps_values[1]}")
        
        for ind in range(2):
            diff = ps_values[ind] - last_ps_values[ind]
            if abs(diff) < 0.001:
                diff = 0
                ps_values[ind] = last_ps_values[ind]
            dist_values[ind] = ps_values[ind] * encoder_unit
        
        print(f"left dist: {dist_values[0]} right dis: {dist_values[1]}")
        
        #compute linear and angulart velocity for robot
        v = (dist_values[0] + dist_values[1]) / 2.0
        w = (dist_values[0] - dist_values[1]) / distance_between_wheels
        
        dt = 1
        robot_pose[2] += (w * dt)
        vx = v * math.cos(robot_pose[2])
        vy = v * math.sin(robot_pose[2])
        
        robot_pose[0] += (vx * dt)
        robot_pose[1] += (vy * dt)
        
        print(f"x: {robot_pose[0]} y: {robot_pose[1]} angle: {robot_pose[2]}")
        
        # if robot_pose[0] >= 2.5:
            # left_speed = 0
            # right_speed = 0 
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
        for ind in range(2):
            last_ps_values[ind] = ps_values[ind] 
        
if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)