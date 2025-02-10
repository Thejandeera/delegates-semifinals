import pathlib
from urdf2webots.importer import convertUrdfContent
robot_description = pathlib.Path('./Robot.urdf').read_text()
convertUrdfContent(input = robot_description, robotName="robot")
