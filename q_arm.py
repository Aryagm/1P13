import sys
sys.path.append('../')

from Common.hardware_project_library import *
from Common.barcode_checker import *

# Initialize hardware and peripherals
hardware = True
arm = qarm(project_identifier, ip_address, hardware)
table = servo_table(ip_address, None, hardware)
scanner = barcode_checker()

# STUDENT CODE BEGINS
first = True

while True:
    result = scanner.barcode_check()
    arm.move_arm(0.0, -0.298, 0.2)
    time.sleep(0.5)
    
    if first:
        arm.control_gripper(43)
        first = False
    else:
        arm.control_gripper(5)
    
    arm.rotate_shoulder(-10)
    arm.rotate_elbow(-20)
    
    if "rejection" in result:
        arm.rotate_base(45)
        arm.rotate_elbow(50)
    else:
        arm.rotate_base(90)
        arm.rotate_elbow(50)
        arm.control_gripper(-5)
        table.rotate_table_speed(0.2)
        table.stop()
        table.rotate_table_angle(90)
