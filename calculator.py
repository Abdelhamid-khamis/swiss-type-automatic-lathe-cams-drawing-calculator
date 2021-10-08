
excel_file = {
    "Release Collet" : "C",
    "Head Stock Backward" : "I",
    "Clamp Collet" : "C",
    "Rear Tool Backward" : "I",
    "Front Tool Forward" : "I",
    "Head Stock Forward" : "W",
    "Rest" : "I"
}

# Constant values
play = 0.2
overcut = 0.5
parting_off_width = 2.5 # the width of the parting off tool
initial_diameter = 18   # will be a user input
total_travel = 51       # will be a user input
number_of_headstock_movements = 5 # will be a user input  or 
                                    # will be done using some kind of (string/object) manipulation

#### Cams Calculations
####------------------

### Head stock cam calculations
###----------------------------

## Head stock cam movements
headstock_backward_total_length = total_travel + play

headstock_forward_lengths_list = []
default_values_for_headstock_forward_length = [3,23,10,5,10]    # will be a user input through a loop

for counter1 in range(number_of_headstock_movements):
    headstock_forward_length = default_values_for_headstock_forward_length[counter1]
    headstock_forward_lengths_list.append(headstock_forward_length)

## Head stock cam Heights --> cam heights 1:1 , (100,30)r1
# constant values
head_stock_r_max = 100
head_stock_scale = 1


headstock_backward_cam_height = head_stock_r_max - headstock_backward_total_length
headstock_backward_cam_height_eqn = f"{headstock_backward_cam_height} = {head_stock_r_max} - {headstock_backward_total_length}"

changing_variable = headstock_backward_cam_height

headstock_forward_movements_list = []

for counter2 in range(number_of_headstock_movements):
    changing_variable = changing_variable + (headstock_forward_lengths_list[counter2] * head_stock_scale )
    
    
"""لسه محتار هحط الاسترينج ولا االانتجر وهحطهم ف ليست ولا ديكشنرى"""