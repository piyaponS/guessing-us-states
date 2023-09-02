import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')

all_states = data["state"].to_list()
guessed_states = []

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name").title()

    if answer_state == "Exit":
        break  # Exit the game if the player types "Exit"
        turtle.write("Game over!!", align="center", font=("Arial", 24, "normal"))


    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data['state'] == answer_state]
        x = int(state_data['x'].iloc[0])  
        y = int(state_data['y'].iloc[0]) 

        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.goto(x, y)
        state_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))

        if len(guessed_states) == len(all_states):
            is_game_on = False
            turtle.write("You win!!", align="center", font=("Arial", 24, "normal"))



# Save the guessed states to a CSV file
output = pd.DataFrame(guessed_states)
output.to_csv("learn.csv")
turtle.exitonclick()
