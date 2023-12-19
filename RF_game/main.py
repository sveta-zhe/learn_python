import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("Districts of the Russian Federation")
image = "RF_map.gif"
screen.addshape(image)
turtle.shape(image)

# with open('rf.csv', 'r', encoding='UTF-8') as f:
#     data = csv.DictReader(f, delimiter=';', skipinitialspace=True)
    # for row in data:
    #     print(row)

data = pandas.read_csv("rf.csv", delimiter=';')
all_districts = data.district.to_list()
guessed_districts = []

while len(guessed_districts) < 13:
    answer_district = screen.textinput(title=f"{len(guessed_districts)}/12 Федеральных округов",
                                       prompt="Напишите название следующего Федерального округа").title()
    print(answer_district)

    if answer_district == "Exit":
        missing_districts = []
        for district in all_districts:
            if district not in guessed_districts:
                missing_districts.append(district)
        new_data = pandas.DataFrame(missing_districts)
        new_data.to_csv("districts_to_learn.csv")

        break
    if answer_district in all_districts:
        guessed_districts.append(answer_district)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        district_data = data[data.district == answer_district]
        t.goto(int(district_data.x), int(district_data.y))
        t.write(answer_district)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
screen.exitonclick()
