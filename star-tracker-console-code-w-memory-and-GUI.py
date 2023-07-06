#Rohan Sonakya 07/05/2023 4:37
    #Next task: do full tests with star tracker



from tkinter import *
import moving_functions as mf
import optimal_path_algorithm as opa

STEP_PER_DEGREE = (512*225)/360

class MyWindow:
  
    def move(self):
            #old vals
            

            with open("C:\\Users\\sonak\\Documents\\SVLC\\Star Tracker\\Code\\code-w-memory-transport-from-previous\positions.csv", 'r', encoding='UTF8') as f:
                    #get last line (most recent position)
                last_pos = str((f.readlines()[-1]))
                    #remove parenthsis and return from csv position data
                last_pos_clean = last_pos[1:-2]
                print(last_pos_clean)
                last_pos = []
                last_pos = last_pos_clean.split(",")
                old_pos_x = float(last_pos[0])
                old_pos_y = float(last_pos[1])
            print(old_pos_x)
            print(old_pos_y)
            self.oldposdsply.delete(0,END)
                #display old position in window
            self.oldposdsply.insert(END, str(f'''({old_pos_x},{old_pos_y})'''))

            #ask values


            new_pos = self.newposentry.get()
            new_pos_to_write = new_pos
            print(new_pos)
            new_pos_clean = new_pos[1:-1]
            print(new_pos_clean)
            new_pos = []
            new_pos = new_pos_clean.split(",")
            new_pos_x = float(last_pos[0])
            new_pos_y = float(last_pos[1])
            print(new_pos_x)


            #write new values to csv file
            with open("C:\\Users\\sonak\\Documents\\SVLC\\Star Tracker\\Code\\code-w-memory-transport-from-previous\positions.csv", 'a', encoding='UTF8') as f:
                f.write(str(new_pos_to_write)+"\n")

            #sol for x direction and degrees

            yaw_direction = opa.optimal_x_dir(old_pos_x,new_pos_x)
            yaw_degrees = opa.optimal_x_deg(old_pos_x,new_pos_x)



            #sol for y direction and degrees

            pitch_degrees = abs(float(new_pos_y-old_pos_y))


            




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

    def reset(self):
        with open("C:\\Users\\sonak\\Documents\\SVLC\\Star Tracker\\Code\\code-w-memory-transport-from-previous\positions.csv", 'w', encoding='UTF8') as f:
            f.truncate()
            f.write("(0,0)\n")
            f.close
        

  #GUI
    def __init__(self, win):

        #old position title
        self.oldposlbl=Label(window, text="Old Position:", fg='red', font=("Helvetica", 16))
        self.oldposlbl.place(x=55, y=10)

        #new position title
        self.newposlbl=Label(window, text="New Position:", fg='red', font=("Helvetica", 16))
        self.newposlbl.place(x=55, y=75)

        #old position display
        self.oldposdsply=Entry(window, text="Dees?", bd=4)
        self.oldposdsply.place(x=55, y=45)

        #new position display
        self.newposentry=Entry(window, text="Degrees?", bd=8)
        self.newposentry.place(x=55, y=110)

        #button to reset csv position file to zero
        self.btn_reset=Button(window, text="Reset", fg='blue')
        self.btn_reset=Button(win, text='reset', command=self.reset)
        self.btn_reset.place(x=75, y=150)


        #button to start movement
        self.btn_move=Button(window, text="Run", fg='blue')
        self.btn_move=Button(win, text='move', command=self.move)
        self.btn_move.place(x=145, y=150)

 


#Display GUI
window = Tk()
mywin=MyWindow(window)
window.title('Star Locator Program')
window.geometry("250x200+10+20")
window.mainloop()