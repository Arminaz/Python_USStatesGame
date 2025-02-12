import pandas
import turtle

# Screen setup

FILE_NAME = "50_states.csv"
STATE_FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
data = pandas.read_csv(FILE_NAME)

# Get Total States
total_states = len(data['state'])
states = data['state']

# State Names
data_states = []

while score < total_states:
    answer_state = screen.textinput(title=f"{score}/{total_states} States Correct", prompt="Write a State Name")
    correct_state = data[states == answer_state].iloc[0]
    if correct_state.size > 0 and correct_state['state'] not in data_states:
        
        state_name = correct_state['state']
        score += 1

        # Add the State name to the gif image
        state = turtle.Turtle()
        state.penup()
        state.hideturtle()
        state.goto(correct_state['x'], correct_state['y'])
        state.write(state_name, move=False, align="center", font=STATE_FONT)
        data_states.append(state_name)


screen.exitonclick()