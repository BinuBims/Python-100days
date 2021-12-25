import turtle, pandas as pd

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
states_df = pd.read_csv("50_states.csv")
wrong = 0
i = 0
for i in range(50):
    answer_state = screen.textinput(title="Guess the state", prompt="What's anohter state's name?")
    
    if answer_state.capitalize()==states_df["state"]:
        state_name = states_df[answer_state.capitalize()==states_df["state"]].state
        X = int(states_df[answer_state.capitalize()==states_df["state"]].x)
        Y = int(states_df[answer_state.capitalize()==states_df["state"]].y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(X,Y)
        t.write(answer_state.capitalize())
    else:
        wrong +=1
    i += 1
