def move_up(control_pins, pitch_degree_to_step):
    GPIO.setmode(GPIO.BOARD)
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0) 
    halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
    ]
    for i in range(int(pitch_degree_to_step)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0015)
    GPIO.cleanup()

def move_down(control_pins, pitch_degree_to_step):
    GPIO.setmode(GPIO.BOARD)
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0) 
    halfstep_seq = [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0]
    ]
    for i in range(int(pitch_degree_to_step)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0015)
    GPIO.cleanup()

def move_left(control_pins, yaw_degree_to_step):
    GPIO.setmode(GPIO.BOARD)
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0) 
    halfstep_seq = [
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1],
    [1,0,0,1]
    ]
    for i in range(int(yaw_degree_to_step)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0015)
    GPIO.cleanup()

def move_right(control_pins, yaw_degree_to_step):
    GPIO.setmode(GPIO.BOARD)
    for pin in control_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0) 
    halfstep_seq = [
    [1,0,0,1],
    [0,0,0,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,1,1,0],
    [0,1,0,0],
    [1,1,0,0],
    [1,0,0,0]
    ]
    for i in range(int(yaw_degree_to_step)):
        for halfstep in range(8):
          for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
            time.sleep(0.0015)
    GPIO.cleanup()