import pandas as pd 
import numpy as np 
import csv
import plotly.express as px

def menu():
    choices = input('''
    Welcome to Group 5 weather program! Please choose one of the options below:
        A: View selected Attribute over time
        B: Print current data 
        C: Add manual data
        D: Build decision tree
        E: Add new observation
        F: Classify test data
        G: Quit 
        ''').upper()
    R_choices = ("A","B","C","D","E","F","G")
    while choices not in R_choices:
        print("You have to choose one of the options above")
        choices = input('''
        A: View selected Attribute over time
        B: Print current data 
        C: Add manual data
        D: Build decision tree
        E: Add new observation
        F: Classify test data
        G: Quit 
        ''').upper()
    return choices
menus = menu()
# def read_temp():

#     list_temperature = []
#     with open('temp.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             list_temperature.append(row)
#     print(list_temperature)
#     return list_temperature

# def read_sunshine():

#     list_sunshine = []
#     with open('solskenstid.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             list_sunshine.append(row)
#     print(list_sunshine)
#     return list_sunshine

# def read_rain():
#     list_rain = []
#     with open('nederbörd.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             list_rain.append(row)
#     print(list_rain)
#     return list_rain



def Attribute_over_time(Attribute):
    if Attribute == "Temperature":
        df = pd.read_csv("Temperature day.csv", sep=";")
    elif Attribute == "Sunshine":
        df = pd.read_csv("Sunshine.csv", sep=";")
    elif Attribute == "Downfall":
        df = pd.read_csv("Downfall day.csv", sep=";")
    fig = px.line(df, x="Datum", y=Attribute, title= Attribute + " over time")
    fig.show()

def interval_day(Attribute):
    #exempel på datum: 2020-12-28
    if Attribute == "Temperature":
        df = pd.read_csv("Temperature day.csv", sep=";")
    elif Attribute == "Sunshine":
        df = pd.read_csv("Sunshine.csv", sep=";")
    elif Attribute == "Downfall":
        df = pd.read_csv("Downfall day.csv", sep=";")
    df = df.set_index("Datum")
    interval1 = input("Enter the first date: ")
    interval2 = input ("Enter the second date: ")
    df = df.loc[interval1:interval2, :]
    df = df.reset_index()
    fig = px.line(df, x="Datum", y=Attribute, title=Attribute + " over time")
    fig.show()


def interval_hour(temp, hours):
    #Gör om valt värde till ett index som sedan adderas med antal timmar eller hours, som user väljer själv. Dessa görs sedan om igen till ett värde utifrån indexet och man får en ny range.
    if Attribute == "Temperature":
        df = pd.read_csv("Temperature hourly.csv", sep=";")
    elif Attribute == "Sunshine":
        df = pd.read_csv("Sunshine.csv", sep=";")
    elif Attribute == "Downfall":
        df = pd.read_csv("Downfall hourly.csv", sep=";")
    df1 = df.set_index("Datum")
    interval1 = input("Enter the first date: ") # 2020-01-10 
    slice_start = int(df1.index.get_loc(interval1).start) #2020-01-10 = index(285) 285, 310 == slice_start = int(285)
    df1 = df1.iloc[slice_start:(slice_start + hours), :] #om du ger interger värde så får du fram ett värde på det indexet. ":" = interval. Till 285 + 48
    df1 = df1.reset_index()
    new_df = pd.DataFrame(df1[Attribute])
    fig = px.line(new_df, x = new_df.index, y=Attribute, title="Interval between " + interval1 + " to " + str(df.iloc[(slice_start+hours)][0]) , labels={"index":"Hours"})
    fig.show()


# def sunshine(list_sunshine):



# def rain(list_rain):





# def main():
#     readfiles()=list_rain,list_sunshine,list_temperature
#     answer = ""
#     while answer != "5":
#         str(input("what do you want to do?"))
#         print("1. Show temperature graph")
#         print("2. Show sunshine graph")
#         print("3. Show rain graph")

#         if answer == "1":
#             temperature(list_temperature)
#         if answer == "2":
#             temperature(list_temperature)
#         if answer == "3":
#             temperature(list_temperature)

# main()


while menus != "":

    if menus == "A":
        Attribute = input("Choose an attribute you want to view [Temperature, Sunshine, Downfall]: ")
        Attribute_over_time(Attribute)
        menus = menu()
    elif menus == "B":
        Attribute = input("Choose an attribute you want to view [Temperature, Sunshine, Downfall]: ")
        interval_day(Attribute)
        menus = menu()
    elif menus == "C":
        Attribute = input("Choose an attribute you want to view in hours [Temperature, Sunshine, Downfall]: ")
        hours = int(input("Select over how many hours you want to view: "))
        interval_hour(Attribute, hours)
        menus = menu()
    # elif menus == "D":
    #     d_tree = build_decision_tree(d_f)
    #     menus = menu()
    # elif menus == "E":
    #     t_data = add_observation(d_f, test_data_df)
    #     menus = menu()
    # elif menus == "F":
    #     print(Classify(t_data, d_tree, d_f))
    #     menus = menu()
    # elif menus == "G":
    #     inp = input("Are you sure? Yes/No: ")
    #     if inp == "yes" or inp == "Yes":
    #         break
    #     elif inp == "no" or inp == "No":
    #         menus = menu()

# print("hello")


# temperature("temp1.csv")
# interval_temp("lufttemp_dygn.csv")
#interval_hour("temp.csv", 48)


#### blabla = index ????
#### search blabla == index
#### index + 48 == intervall på 48h

