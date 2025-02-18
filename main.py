import pandas
import turtle


FILE_NAME = "50_states.csv"
STATE_FONT = ("Courier", 8, "normal")

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialize Variables
score = 0
data = pandas.read_csv(FILE_NAME)
data_states = []

# Get Total States
total_states = len(data['state'])
states = data['state']

# While the score is less than total state score.
while score < total_states:
    answer_state = screen.textinput(title=f"{score}/{total_states} States Correct", prompt="Write a State Name")
    if answer_state == "Exit":
        break

    correct_state = data[states == answer_state]
    if correct_state.size > 0:
        correct_state = correct_state.iloc[0]
        if correct_state['state'] not in data_states:
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