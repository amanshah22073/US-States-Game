import pandas as pd
import turtle


tim = turtle.Turtle()
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=1000, height=800 )
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()


while len(guessed_states) <= 50:
    answer = screen.textinput(title = f"Correct States : {len(guessed_states)}/50" , prompt ="Enter the name of the state")
    if answer.lower() == "quit":
        break 
    if answer.title() in all_states and answer.title() not in guessed_states:
        guessed_states.append(answer.title())
        x_corr , y_corr = int(data[data.state == answer.title()]['x']) , int(data[data.state == answer.title()]['y'])
        tim.penup()
        tim.goto(x_corr , y_corr)
        tim.speed(2)
        tim.write(answer.title())
    
tim2 = turtle.Turtle()
screen2 = turtle.Screen()
screen2.title("Here are the answers for you")
screen2.setup(width=1000, height=800)
screen2.addshape(image)
turtle.shape(image)
for i in data['state']:
    if i not in guessed_states:
        x_corr , y_corr = int(data[data.state == i]['x']) , int(data[data.state == i]['y'])
        tim2.penup()
        tim2.goto(x_corr , y_corr)
        tim2.speed(1)
        tim2.write(i.title())
