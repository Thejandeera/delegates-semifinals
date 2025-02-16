from controller import Robot, Motor, DistanceSensor

# Time step of the simulation
TIME_STEP = 64

# Create the Robot instance
robot = Robot()

# Initialize motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Initialize distance sensors
sensors = []
sensor_names = ['ds_left', 'ds_right', 'ds_front']
for name in sensor_names:
    sensor = robot.getDevice(name)
    sensor.enable(TIME_STEP)
    sensors.append(sensor)

# Define maximum speed
MAX_SPEED = 6.28

def read_sensors():
    return [sensor.getValue() for sensor in sensors]

def set_motor_speeds(left_speed, right_speed):
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

# Main loop
while robot.step(TIME_STEP) != -1:
    # Read sensor values
    left_sensor, right_sensor, front_sensor = read_sensors()
    
    # Simple maze-solving logic
    if front_sensor > 800:
        # If there's a wall in front, turn right
        set_motor_speeds(MAX_SPEED, -MAX_SPEED)
    elif left_sensor < 800:
        # If there's no wall on the left, turn left
        set_motor_speeds(MAX_SPEED / 2, MAX_SPEED)
    else:
        # Otherwise, move forward
        set_motor_speeds(MAX_SPEED, MAX_SPEED)

    # Add more sophisticated logic as needed

# Cleanup code if necessary
