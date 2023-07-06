#test code

def optimal_x_dir(old_pos_x,new_pos_x):
    optimal_path = new_pos_x - old_pos_x
        #simple test to see if a path less than 180 exists by subtracting
    if abs(optimal_path) <= 180:
        if optimal_path > 0:
                #direction simply states which direction the star locator is to turn in 
            direction = "cw"
        elif optimal_path < 0:
            direction = "ccw"
        else:
            direction = "stationary"
        fail = "N"

    else:
            #creation of "key" for more algorith that crosses top of circle
        fail = "Y"
        #if path is >180 optimal path must cross top of circle. This algorith crosses the "top" of circle

    while fail == "Y":
        if old_pos_x > 180:
            optimal_path = (360 - old_pos_x) + (new_pos_x - 0)
            direction = "cw"
            fail = "N"
        else:
            optimal_path = (old_pos_x - 0) + (360 - new_pos_x)
            direction = "ccw"
            fail = "N"
    yaw_direction = direction
    yaw_degrees = optimal_path
    return yaw_direction

def optimal_x_deg(old_pos_x,new_pos_x):
    optimal_path = new_pos_x - old_pos_x
        #simple test to see if a path less than 180 exists by subtracting
    if abs(optimal_path) <= 180:
        if optimal_path > 0:
                #direction simply states which direction the star locator is to turn in 
            direction = "cw"
        elif optimal_path < 0:
            direction = "ccw"
        else:
            direction = "stationary"
        fail = "N"

    else:
            #creation of "key" for more algorith that crosses top of circle
        fail = "Y"
        #if path is >180 optimal path must cross top of circle. This algorith crosses the "top" of circle

    while fail == "Y":
        if old_pos_x > 180:
            optimal_path = (360 - old_pos_x) + (new_pos_x - 0)
            direction = "cw"
            fail = "N"
        else:
            optimal_path = (old_pos_x - 0) + (360 - new_pos_x)
            direction = "ccw"
            fail = "N"
    yaw_degrees = optimal_path
    return yaw_degrees