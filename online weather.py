import pandas as pd 
import numpy as np 
import csv
import plotly.express as px
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



print ('hello world again 4!')


def temperature(temp):
    df = pd.read_csv(temp, sep=";")
    fig = px.line(df, x="Datum", y="Lufttemperatur", title='Temperature over time')
    fig.show()

def interval_temp(temp):
    #exempel på datum: 2020-12-28
    df = pd.read_csv(temp, sep=";")
    df = df.set_index("Datum")
    interval1 = input("Enter the first date: ")
    interval2 = input ("Enter the second date: ")
    df = df.loc[interval1:interval2, :]
    df = df.reset_index()
    fig = px.line(df, x="Datum", y="Lufttemperatur", title='Temperature over time')
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


# print("hello")


temperature("temp1.csv")
interval_temp("temp.csv")