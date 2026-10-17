
workpiece_height = 185.0 # mm
workpiece_width = 254.0 # mm

cutting_speed = 200 # mm/minute
cutting_head_width = 25.4 # mm. 1"
cutting_depth_per_pass = 0.25
passes = 2
plunge_speed = cutting_speed

header = """(Face leveling passes vertical bottom to top (x = 0 to 254mm, y = 0 to 185mm, tool is 1\" (25.4mm) wide).)
( Origin: true bottom-left corner of the workpiece)
( Zero the machine at that corner, then jog to corner of workpiece before running this file. )"""

# header
print(header)
# start of job
print("G21 ( mm )")
print("G90 ( absolute )")
print("G0 Z5.000")
print("M3 S12000 ( turn motor on, ignored if spindle speed is set manually )")
print("G0 X0 Y0 ( move gantry to origin if not already there)")

# start of cutting
x = 0.0
y = workpiece_height + cutting_head_width + 3 # make sure that cutting head does not plunge into wood, but starts well above it.
cutting_width = cutting_head_width * 0.85
z = -cutting_depth_per_pass
for pass_ in range(passes): # pass_ to distinguish it from keyword pass
    while x < workpiece_width:
        print(f"G0 X{x} Y{y} Z5.0000 ( Go to start of next vertical cut)")
        print(f"G1 Z{z} F{plunge_speed} ( Lower gantry )")
        print(f"G1 X{x} Y{0} F{cutting_speed} (cut from top to bottom low x to high x)")
        print("G0 Z5.000 (raise gantry)")
        x += cutting_width
    z -= cutting_depth_per_pass

# End of Job
print("G0 Z5.000")
print("M5")
print("M2")
print("G0 Z5.000")

