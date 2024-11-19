ip_address = "localhost"
project_identifier = "P3A"
import sys
sys.path.append('../')

from Common.hardware_project_library import *
from Common.barcode_checker import *
from Common.standalone_actuator_lib import *

bot = qbot()
hardware = True
arm = qarm(project_identifier, ip_address, hardware)
table = servo_table(ip_address, None, hardware)
scanner = barcode_checker()

# STUDENT CODE BEGINS
first = True

while True:
    result = scanner.barcode_check()
    print(result)

    arm.move_arm(0.0, -0.408, 0.234)
    time.sleep(0.5)

    if first:
        arm.control_gripper(45)
        first = False
    else:
        arm.control_gripper(5)

    if "rejection" in result.lower():
        arm.move_arm(0.0, 0.454, 0.228)
        arm.control_gripper(-5)
    else:
        arm.move_arm(0.412, -0.21, 0.407)
        arm.control_gripper(-5)

    table.rotate_table_speed(0.2)
    table.stop()
    table.rotate_table_angle(90)
