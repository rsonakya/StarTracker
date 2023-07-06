#Rohan Sonakya 07/02/2023 1:41
    #DONE next task: have old pos be read from csv file and new be written
        #-in order to keep working create button/code that will reset csv to 0,0
            #-store steps, not degrees <-- not sure if it matters

import moving_functions as mf
import optimal_path_algorithm as opa
import csv

STEP_PER_DEGREE = (512*225)/360


#old vals

with open("C:\\Users\\sonak\\Documents\\SVLC\\Star Tracker\\Code\\code-w-memory-transport-from-previous\positions.csv", 'r', encoding='UTF8') as f:
        #get last line (most recent position)
    last_pos = str((f.readlines()[-1]))
        #remove parenthsis from csv position data
    last_pos_clean = last_pos[1:-2]
    print(last_pos_clean)
    last_pos = []
    last_pos = last_pos_clean.split(",")
    old_pos_x = float(last_pos[0])
    old_pos_y = float(last_pos[1])
print(old_pos_x)
print(old_pos_y)


#ask values

print("Where would you like to go?")

new_pos_x = float(input("x value: "))
new_pos_y = float(input("y value: "))

#sol for x direction and degrees

yaw_direction = opa.optimal_x_dir(old_pos_x,new_pos_x)
yaw_degrees = opa.optimal_x_deg(old_pos_x,new_pos_x)



#sol for y direction and degrees

pitch_degrees = abs(float(new_pos_y-old_pos_y))


#write new values to csv file
with open("C:\\Users\\sonak\\Documents\\SVLC\\Star Tracker\\Code\\code-w-memory-transport-from-previous\positions.csv", 'a', encoding='UTF8') as f:
    f.write(f'''({new_pos_x},{new_pos_y})''')
    f.write("\n")

if pitch_degrees > 0:
    pitch_direction = "Up"
else:
    pitch_direction = "Down"


#Print val moves in GUI
print(str(pitch_direction) +str(pitch_degrees) + str(yaw_direction)+ str(yaw_degrees))

#Vals for motor to move
pitch_degree_to_step = float(pitch_degrees) * STEP_PER_DEGREE
yaw_degree_to_step = float(yaw_degrees) * STEP_PER_DEGREE


#Move up
if pitch_direction == "Up":
    control_pins = [7,11,13,15]
    mf.move_up(control_pins,pitch_degree_to_step)
    print (str(pitch_degree_to_step) + "Up")
#Move down
else:
    control_pins = [7,11,13,15]
    mf.move_down(control_pins,pitch_degree_to_step)
    print (str(pitch_degree_to_step) + "Down")
#Move left
if yaw_direction == "Left":
    control_pins = [31,33,35,37]
    mf.move_left(control_pins,yaw_degree_to_step)
    print (str(yaw_degree_to_step) + "Left")
#Move right
else:
    control_pins = [31,33,35,37]
    mf.move_right(control_pins,yaw_degree_to_step)
    print (str(yaw_degree_to_step) + "Right")